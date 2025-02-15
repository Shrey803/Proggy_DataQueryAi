
---

# DataQuery AI

DataQuery AI is a Streamlit-based web application that allows users to upload CSV files, ask natural language questions about their data, and generate visualizations. It leverages the TAPAS (Tabular Parser) model for answering questions and Plotly for generating charts.

---

## Features

1. **Natural Language Querying**:
   - Ask questions about your data in plain English.
   - Powered by the TAPAS model for tabular question answering.

2. **Data Visualization**:
   - Generate interactive charts (bar, line, scatter, pie) from your data.
   - Customize charts by selecting columns for the X and Y axes.

3. **CSV File Upload**:
   - Upload your CSV files directly to the app.
   - Preview the uploaded data before querying or visualizing.

4. **User-Friendly Interface**:
   - Built with Streamlit for an intuitive and interactive experience.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or higher
- Required Python libraries (install via `pip`):
  ```bash
  pip install streamlit pandas plotly transformers torch
  ```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/DataQuery-AI.git
   cd DataQuery-AI
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

4. **Access the App**:
   - Open your browser and navigate to `http://localhost:8501`.

---

## Usage

### 1. Upload a CSV File
- Click the "Upload your CSV file" button to upload a CSV file.
- The app will display a preview of the uploaded data.

### 2. Ask a Question
- Enter a natural language question about your data in the text input box.
- Click the "Get Answer" button to see the result.

### 3. Generate Charts
- Select a chart type (bar, line, scatter, pie) from the dropdown menu.
- Choose columns for the X and Y axes.
- Click the "Generate Chart" button to create and display the chart.

---

## Project Structure

```
DataQuery-AI/
├── app.py                  # Main Streamlit application
├── model.py                # DataQueryModel class for query processing
├── visualisation.py        # ChartGenerator class for creating visualizations
├── README.md               # Project documentation
├── requirements.txt        # List of dependencies
└── assets/                 # Directory for static assets (optional)
```

---

## Code Overview

### `app.py`
- The main Streamlit application.
- Handles file uploads, user input, and displays results.

### `model.py`
- Contains the `DataQueryModel` class.
- Uses the TAPAS model for processing natural language queries.

### `visualisation.py`
- Contains the `ChartGenerator` class.
- Generates interactive charts using Plotly.

---

## Example Queries

Here are some example questions you can ask about your data:

1. **Aggregation**:
   - "What is the total sales?"
   - "What is the average age of customers?"

2. **Filtering**:
   - "Show me all records where the age is greater than 30."
   - "List all products with a price above $50."

3. **Visualization**:
   - "Generate a bar chart of sales by region."
   - "Create a pie chart of product categories."

---

## Troubleshooting

### 1. **TypeError: expected string or bytes-like object, got 'int'**
- Ensure all values in your CSV file are strings.
- Use the following code to convert all values to strings:
  ```python
  df = df.applymap(lambda x: str(x) if pd.notna(x) else '')
  ```

### 2. **File Upload Issues**
- Ensure the uploaded file is a valid CSV.
- Check for encoding issues (e.g., use `encoding='utf-8'` when reading the file).

### 3. **Model Not Working**
- Ensure you have an active internet connection to download the TAPAS model.
- Verify that the `transformers` library is installed correctly.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.
## Acknowledgments

- **TAPAS Model**: Developed by Google for tabular question answering.
- **Streamlit**: For building the interactive web app.
- **Plotly**: For creating interactive visualizations.

