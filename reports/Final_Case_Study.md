# 🚢 Titanic Survival Analytics – Final Case Study

**Organization:** SWYNEX Technologies  
**Internship:** Data Analyst Internship  
**Project:** Final Data Analytics Project  
**Author:** Divya Gowda

---

## 1. Project Overview

This project presents an end-to-end data analytics case study using the Titanic passenger dataset.

The project combines data cleaning, exploratory data analysis (EDA), data visualization and interactive dashboard development to investigate passenger survival patterns and identify meaningful insights.

The final outcome is an interactive dashboard that presents analytical findings through visualizations, key performance indicators and passenger filters.

## 2. Problem Statement

The Titanic passenger dataset contains information about passengers, including their age, gender, passenger class, ticket fare, family relationships and survival status.

The objective of this project is to analyze the dataset to understand how different passenger characteristics were associated with survival outcomes.

The analysis focuses on identifying patterns across gender, passenger class, age, fare, family size and embarkation port.

## 3. Project Objectives

- Clean and prepare the Titanic dataset for analysis.
- Identify and handle missing values and duplicate records.
- Explore passenger characteristics and survival patterns.
- Perform exploratory data analysis using Python.
- Create meaningful data visualizations.
- Develop an interactive analytics dashboard.
- Present key findings through a structured case study.

## 4. Dataset Information

**Dataset:** Titanic Passenger Dataset  
**Cleaned File:** `titanic_cleaned.csv`  
**Records:** 891 passengers  
**Columns:** 11

The dataset contains passenger information and variables used to investigate survival outcomes.

Important analytical variables include:

- PassengerId
- Survived
- Pclass
- Sex
- Age
- SibSp
- Parch
- Fare
- Embarked

Derived variables and categories were also used during analysis, including passenger class labels, survival status and family size.

## 5. Data Cleaning and Preparation

The initial data preparation was performed using Python and Pandas.

The cleaning process included:

- Inspecting the dataset structure and data types.
- Identifying missing values.
- Handling missing values.
- Checking for duplicate records.
- Reviewing and correcting data types.
- Preparing the cleaned dataset for exploratory analysis.

The `SibSp` and `Parch` columns were converted to integer data types.

**Final data validation:**

| Check | Result |
|---|---:|
| Final records | 891 |
| Final columns | 11 |
| Missing values | 0 |
| Duplicate rows | 0 |

The cleaned dataset was saved as `titanic_cleaned.csv` and reused in the subsequent analysis.

## 6. Exploratory Data Analysis

Exploratory Data Analysis was performed to identify patterns and relationships in passenger survival data.

### 6.1 Overall Survival Analysis

Out of 891 passengers:

- 342 passengers survived.
- 549 passengers did not survive.
- Overall survival rate was 38.38%.
- Non-survival rate was 61.62%.

This indicates that fewer than half of the recorded passengers survived.

### 6.2 Gender-Based Survival Analysis

Survival rates differed considerably by gender.

| Gender | Survival Rate |
|---|---:|
| Female | 74.20% |
| Male | 18.89% |

Female passengers had a considerably higher observed survival rate than male passengers.

### 6.3 Passenger Class Analysis

| Passenger Class | Survival Rate |
|---|---:|
| First Class | 62.96% |
| Second Class | 47.28% |
| Third Class | 24.24% |

Passengers travelling in first class had the highest observed survival rate, while third-class passengers had the lowest.

### 6.4 Age-Based Analysis

The average age comparison showed:

- Average age of survivors: 28.11 years.
- Average age of non-survivors: 29.74 years.

Survival rates also varied across the age groups created during analysis.

| Age Group | Survival Rate |
|---|---:|
| Child | 57.97% |
| Teenager | 42.86% |
| Young Adult | 35.80% |
| Adult | 38.43% |
| Senior | 22.73% |

Children had a higher observed survival rate than the other age groups in this analysis.

### 6.5 Fare Distribution and Outlier Detection

The fare analysis examined ticket price distribution and potential outliers.

- Average ticket fare: 32.20.
- Upper outlier threshold using the IQR method: 65.63.
- Number of identified fare outliers: 116.

The analysis showed that ticket fares were not evenly distributed and included several high-value observations.

### 6.6 Family Size Analysis

Family size was examined to understand its relationship with survival.

| Family Size | Survival Rate |
|---|---:|
| 1 | 30.35% |
| 2 | 55.28% |
| 3 | 57.84% |
| 4 | 72.41% |
| 5 | 20.00% |
| 6 | 13.64% |
| 7 | 33.33% |
| 8 | 0.00% |
| 11 | 0.00% |

Passengers travelling in smaller family groups generally showed different survival patterns from passengers travelling in larger groups.

Some family-size categories contained relatively few observations, so their percentages should be interpreted carefully.

### 6.7 Embarkation Port Analysis

The observed survival rates differed by embarkation port.

| Embarkation Port | Survival Rate |
|---|---:|
| Cherbourg (C) | 55.36% |
| Queenstown (Q) | 38.96% |
| Southampton (S) | 33.90% |

Cherbourg had the highest observed survival rate among the three embarkation ports.

### 6.8 Correlation Analysis

A correlation heatmap was created to explore relationships between numerical passenger variables.

The analysis considered variables such as survival status, passenger class, age, family-related features and fare.

Correlation helps identify linear relationships between numerical variables, but it does not establish causation.

### 6.9 Gender and Passenger Class Comparison

The combined analysis showed different survival patterns across gender and passenger class.

| Passenger Group | Survival Rate |
|---|---:|
| Female – First Class | 96.81% |
| Female – Second Class | 92.11% |
| Female – Third Class | 50.00% |
| Male – First Class | 36.89% |
| Male – Second Class | 15.74% |
| Male – Third Class | 13.54% |

This comparison highlighted substantial differences in observed survival rates across gender and passenger class combinations.

## 7. Interactive Dashboard Development

An interactive dashboard was developed using Streamlit and Plotly.

The dashboard combines the results of the exploratory analysis into a single application.

### Dashboard Features

- Interactive passenger filters.
- Dynamic KPI cards.
- Survival analysis visualizations.
- Passenger demographic analysis.
- Fare and family analysis.
- Embarkation port visualization.
- Correlation heatmap.
- Gender and passenger class heatmap.

The dashboard allows users to explore passenger data and view visual changes based on the selected filters.

### Dashboard Technologies

- Python
- Pandas
- NumPy
- Plotly
- Streamlit

## 8. Key Analytical Insights

The analysis produced the following major observations:

1. The overall passenger survival rate was 38.38%.
2. Female passengers had a substantially higher observed survival rate than male passengers.
3. First-class passengers had a higher survival rate than second- and third-class passengers.
4. Children had a higher survival rate than the other age groups examined.
5. Passengers travelling in smaller family groups showed different survival patterns from larger groups.
6. Survival rates varied across embarkation ports.
7. Gender and passenger class together revealed considerable differences in survival outcomes.

These are observations from the historical dataset and should not be interpreted as proof that any individual characteristic caused survival.

## 9. Project Limitations

- The analysis is based on the available Titanic passenger records.
- Some passenger groups contain fewer observations than others.
- Correlation does not establish causation.
- The findings describe a historical dataset and should not automatically be generalized to other populations or situations.

## 10. Conclusion

This project demonstrates an end-to-end data analytics workflow, beginning with data cleaning and continuing through exploratory data analysis, visualization and interactive dashboard development.

Working on the Titanic dataset provided practical experience in using Python libraries to prepare data, analyze patterns, create visualizations and communicate analytical findings.

The final interactive dashboard brings the analysis together in an accessible format, making the results easier to explore and understand.

Through this project, I strengthened my practical skills in data cleaning, exploratory analysis, data visualization and interactive application development.

## 11. Project Links

**Live Project Website:**  
https://divyacgowda.github.io/SWYNEX-Interactive-Titanic-Dashboard/

**Interactive Dashboard:**  
https://swynex-titanic-dashboard.streamlit.app/

**Previous Project Repository:**  
https://github.com/divyacgowda/SWYNEX-Interactive-Titanic-Dashboard

**Final Project Repository:**  
To be added after publishing Task 4.

---

**Developed by Divya Gowda**  
Data Analyst Intern – SWYNEX Technologies
