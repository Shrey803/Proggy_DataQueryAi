import plotly.express as px
import plotly.graph_objects as go

class ChartGenerator:
    @staticmethod
    def create_chart(data, chart_type, x_column, y_column, title=""):
        """Generates a chart based on the selected type."""
        if data is None or data.empty:
            return go.Figure().update_layout(title="No data available for visualization")

        if x_column not in data.columns or y_column not in data.columns:
            raise ValueError(f"Columns '{x_column}' or '{y_column}' not found in data.")

        chart_type = chart_type.lower()

        if chart_type == "bar":
            fig = px.bar(data, x=x_column, y=y_column, title=title)
        elif chart_type == "line":
            fig = px.line(data, x=x_column, y=y_column, title=title)
        elif chart_type == "scatter":
            fig = px.scatter(data, x=x_column, y=y_column, title=title)
        elif chart_type == "pie":
            fig = px.pie(data, values=y_column, names=x_column, title=title)
        else:
            fig = px.bar(data, x=x_column, y=y_column, title=title)  # Default to bar chart

        return fig
