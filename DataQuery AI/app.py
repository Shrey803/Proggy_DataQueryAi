import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import logging
import streamlit as st
import pandas as pd
from data_query_model import DataQueryModel
class ChartGenerator:
    @staticmethod
    def create_chart(data, chart_type, x_column, y_column, title=""):
        """Generates a chart based on the selected type."""
        # Input validation
        if data is None or data.empty:
            return go.Figure().update_layout(title="No data available for visualization")

        if not x_column or not y_column:
            return go.Figure().update_layout(title="X or Y column not specified")

        if x_column not in data.columns or y_column not in data.columns:
            return go.Figure().update_layout(title=f"Columns '{x_column}' or '{y_column}' not found in data")

        # Convert chart type to lowercase
        chart_type = chart_type.lower()

        # Map chart types to Plotly Express functions
        chart_functions = {
            "bar": px.bar,
            "line": px.line,
            "scatter": px.scatter,
            "pie": px.pie,
        }

        # Validate chart type
        if chart_type not in chart_functions:
            logging.warning(f"Unsupported chart type: {chart_type}. Defaulting to bar chart.")
            chart_type = "bar"

        # Handle pie charts separately
        if chart_type == "pie":
            try:
                # Ensure y_column is numeric and x_column is categorical
                data[y_column] = pd.to_numeric(data[y_column], errors="coerce")
                fig = chart_functions[chart_type](data, values=y_column, names=x_column, title=title)
            except Exception as e:
                logging.error(f"Error generating pie chart: {e}")
                return go.Figure().update_layout(title="Error generating pie chart")
        else:
            try:
                # Ensure y_column is numeric
                data[y_column] = pd.to_numeric(data[y_column], errors="coerce")
                fig = chart_functions[chart_type](data, x=x_column, y=y_column, title=title)
            except Exception as e:
                logging.error(f"Error generating {chart_type} chart: {e}")
                return go.Figure().update_layout(title=f"Error generating {chart_type} chart")

        return fig

if 'uploaded_file' in st.session_state and st.session_state.uploaded_file:
    df = pd.read_csv(st.session_state.uploaded_file)

    # Convert all column names and values to strings to avoid errors
    df.columns = df.columns.astype(str)  # Ensure column names are strings
    df = df.applymap(lambda x: str(x) if pd.notna(x) else '')  # Ensure all values are strings

    st.write("### Preview of Uploaded Data")
    st.write(df.head())  # Show a preview of the dataset

      # Import the DataQueryModel class
    query_model = DataQueryModel()

    # Query input
    query = st.text_input("Ask a question about your data:")

    if st.button("Get Answer"):
        if query:
            result = query_model.process_query(query, df)
            st.write("### Answer:")
            st.write(result)
        else:
            st.warning("Please enter a question.")