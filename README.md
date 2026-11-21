# 🚢 Titanic Survival Analytics – Final Data Analytics Project

## Project Overview

This project presents an end-to-end data analytics case study using the Titanic passenger dataset.

The project combines data cleaning, exploratory data analysis, data visualization and interactive dashboard development to investigate passenger survival patterns and identify meaningful insights.

Developed as the final project of the Data Analyst Internship at **SWYNEX Technologies**.

## 🎯 Problem Statement

The objective of this project is to analyze Titanic passenger data and understand how passenger characteristics such as gender, age, passenger class, fare and family size were associated with survival outcomes.

The analysis aims to identify patterns, explore relationships between variables and communicate findings through an interactive dashboard.

## 📂 Project Structure

```text
SWYNEX-Final-Data-Analytics-Project/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── assets/
│   └── titanic_header.png
│
├── data/
│   └── titanic_cleaned.csv
│
├── notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   └── 02_Exploratory_Data_Analysis.ipynb
│
├── visuals/
│   ├── 01_survival_analysis.png
│   ├── 02_gender_survival.png
│   ├── 03_class_survival.png
│   ├── 04_age_survival.png
│   ├── 05_fare_distribution.png
│   ├── 06_fare_outliers.png
│   ├── 07_family_size.png
│   ├── 08_embarkation_port.png
│   ├── 09_correlation_heatmap.png
│   └── 10_gender_class.png
│
└── reports/
    └── Final_Case_Study.md
```

## 📊 Project Workflow

### 1. Data Cleaning

- Inspected the Titanic dataset.
- Handled missing values.
- Checked and removed duplicate records.
- Reviewed and corrected data types.
- Prepared the cleaned dataset for analysis.

### 2. Exploratory Data Analysis

Performed analysis on:

- Overall passenger survival.
- Gender-based survival.
- Passenger class survival.
- Age distribution and survival.
- Fare distribution and outlier detection.
- Family size and survival.
- Embarkation port distribution.
- Correlation between numerical variables.
- Gender and passenger class comparison.

### 3. Interactive Dashboard

Developed an interactive dashboard using Streamlit and Plotly.

Dashboard features include:

- Interactive passenger filters.
- Dynamic KPI cards.
- Survival analysis visualizations.
- Passenger demographic analysis.
- Family and travel analysis.
- Advanced analytical heatmaps.

## 🔍 Key Findings

- Overall survival rate was approximately 38.38%.
- Female passengers had a higher survival rate than male passengers.
- First-class passengers had a higher survival rate than passengers in second and third class.
- Passenger family size showed differences in survival patterns.
- Survival rates varied across embarkation ports.

These findings describe patterns in the historical dataset and do not establish causation.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

## 🌐 Live Project

**Interactive Dashboard:**

https://swynex-titanic-dashboard.streamlit.app/

**Project Website:**

https://divyacgowda.github.io/SWYNEX-Interactive-Titanic-Dashboard/

## 💻 Run Locally

Clone the repository:

```bash
git clone https://github.com/divyacgowda/SWYNEX-Final-Data-Analytics-Project.git
```

Navigate into the project folder:

```bash
cd SWYNEX-Final-Data-Analytics-Project
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard:

```bash
streamlit run app.py
```

## 🎓 Internship

Completed as part of the Data Analyst Internship at **SWYNEX Technologies**.

## 👩‍💻 Author

**Divya Gowda**

Computer Science Engineering Student

GitHub: https://github.com/divyacgowda

---

*An end-to-end journey from raw data preparation to interactive analytics and insights.*