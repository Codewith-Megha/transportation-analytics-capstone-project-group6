# 🚖 NYC Transportation Analytics Pipeline

An end-to-end Data Engineering project that processes, transforms, stores, and analyzes New York City Taxi Trip data using Python and PostgreSQL.

This project demonstrates a complete ETL pipeline, data validation, feature engineering, SQL analytics, and an interactive dashboard for transportation insights.

---

## Project Architecture

```
NYC TLC Parquet Files
        │
        ▼
Data Ingestion
        │
        ▼
Schema Standardization
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Data Validation
        │
        ▼
PostgreSQL Database
        │
        ▼
SQL Analytics
        │
        ▼
Interactive Dashboard
        │
        ▼
Machine Learning
```

---

## Features

### ETL Pipeline
- Read multiple NYC Taxi datasets
- Process multiple months automatically
- Standardize schemas across datasets
- Clean missing and inconsistent data
- Validate transformed data
- Generate analytical features
- Detailed logging

### Datasets Supported

- Yellow Taxi
- Green Taxi
- For-Hire Vehicle (FHV)

---

## Technologies Used

### Programming
- Python 3.x

### Data Processing
- Pandas
- NumPy
- PyArrow

### Database
- PostgreSQL
- SQLAlchemy
- Psycopg2

### Visualization
- Plotly
- Streamlit

### Version Control
- Git
- GitHub

---

## Project Structure

```
transportation-analytics-capstone-project-group6/
│
├── config/
├── data/
│   └── raw/
│
├── logs/
│
├── src/
│   ├── etl/
│   ├── database/
│   ├── dashboard/
│   ├── analytics/
│   ├── logger.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Dataset

This project uses the official NYC Taxi & Limousine Commission (TLC) Trip Record Data.

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

The datasets are **not included** in this repository because of their large size.

---

## Current Status

- ✅ Data Ingestion
- ✅ Schema Standardization
- ✅ Data Cleaning
- ✅ Feature Engineering
- ✅ Data Validation
- 🔄 PostgreSQL Integration
- 🔄 SQL Analytics
- 🔄 Dashboard
- 🔄 Machine Learning

---

## Future Enhancements

- Interactive Streamlit Dashboard
- Predictive Trip Analytics
- Travel Demand Forecasting
- Docker Deployment
- Cloud Database Integration (AWS)

---

## Author

**Megha Pandey**

M.Tech (Data Engineering)
Indian Institute of Technology Jodhpur