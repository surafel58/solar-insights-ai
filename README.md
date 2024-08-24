# solar-insights-ai

A data-driven project focused on analyzing solar radiation data from various regions to uncover insights for optimizing solar farm installations. This repo includes exploratory data analysis (EDA), statistical modeling, and Streamlit dashboard for data visualization. Developed as part of the "10 Academy: Artificial Intelligence Mastery" challenge.

## Project Structure

solar-insights-ai/
│
├── data/ # Directory containing the datasets \n
│ ├── benin-malanville.csv \n
│ ├── sierraleone-bumbuna.csv
│ └── togo-dapaong_qc.csv
│
├── notebooks/ # Jupyter notebooks for data analysis
│ ├── data_quality_check/
│ │ ├── data_quality_check_benin.ipynb
│ │ ├── data_quality_check_sierralone.ipynb
│ │ └── data_quality_check_togo.ipynb
│ ├── data_understanding/
│ │ ├── data_understanding_benin.ipynb
│ │ ├── data_understanding_sierralone.ipynb
│ │ └── data_understanding_togo.ipynb
│ └── time_series_analysis/
│ ├── time_series_analysis_benin.ipynb
│ ├── time_series_analysis_sierralone.ipynb
│ └── time_series_analysis_togo.ipynb
│
├── scripts/ # Python scripts for data processing and streamlit dashboard
│ ├── data_quality_checks.py
│ └── dashboard.py
│ └── README.md
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/solar-insights-ai.git
   cd solar-insights-ai
   ```

2. **Create and activate a virtual environment**:

   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `.\env\Scripts\activate`
   ```

3. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Streamlit Dashboard

To start the Streamlit dashboard, run the following command:

```sh
streamlit run scripts/dashboard.py
```

### Jupyter Notebooks

The Jupyter notebooks in the `notebooks/` directory provide detailed analysis and data processing steps. You can run these notebooks using Jupyter Lab or Jupyter Notebook.

## Data Quality Checks

The `scripts/data_quality_checks.py` script contains functions for loading datasets, handling anomalies, and performing data quality checks. These functions are used in both the Jupyter notebooks and the Streamlit dashboard.

## Notebooks Overview

### Data Quality Check Notebooks

- **Benin**: `notebooks/data_quality_check/data_quality_check_benin.ipynb`
- **Sierra Leone**: `notebooks/data_quality_check/data_quality_check_sierralone.ipynb`
- **Togo**: `notebooks/data_quality_check/data_quality_check_togo.ipynb`

These notebooks focus on assessing and improving the quality of solar energy data from different regions. Key steps include loading the dataset, examining the data for missing values, handling negative values, identifying and treating outliers, and performing basic data cleaning and preprocessing.

### Data Understanding Notebooks

- **Benin**: `notebooks/data_understanding/data_understanding_benin.ipynb`
- **Sierra Leone**: `notebooks/data_understanding/data_understanding_sierralone.ipynb`
- **Togo**: `notebooks/data_understanding/data_understanding_togo.ipynb`

These notebooks provide insights into the distribution and completeness of the data, including summary statistics and data ranges for various columns.

### Time Series Analysis Notebooks

- **Benin**: `notebooks/time_series_analysis/time_series_analysis_benin.ipynb`
- **Sierra Leone**: `notebooks/time_series_analysis/time_series_analysis_sierralone.ipynb`
- **Togo**: `notebooks/time_series_analysis/time_series_analysis_togo.ipynb`

These notebooks focus on analyzing the time series data for solar irradiance and other environmental factors. They include plots for visualizing trends and patterns over time.
