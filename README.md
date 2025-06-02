# 🩺 Medical Market Segmentation & ML Prediction Dashboard

A Streamlit web application for interactive **Exploratory Data Analysis (EDA)**, **Unsupervised Clustering**, and **Machine Learning-based Test Result Prediction** using healthcare datasets.

## 🚀 Live Demo

👉 **Try the App Now:**  
🔗 [Medical Market Segmentation Streamlit App](https://medical-market-segmentation-ff9uvi74rde62kjgi4knjg.streamlit.app/)


## 🔍 Features

### 📊 EDA & Clustering
- Interactive filters for **Gender** and **Age Range**
- Visualizations for:
  - Patient demographics by **Age Group** and **Gender**
  - **Average Billing Amounts** across groups
  - **Admission Types** by Gender
  - Top **Medical Conditions**
- Unsupervised Clustering (KMeans + PCA) for **patient segmentation** based on Age and Billing
- Cluster profiling dashboard with averages and cluster size

### 🤖 ML Model Predictions
- Predicts **Test Results** (Normal, Abnormal, Inconclusive)
- Preprocesses and encodes features automatically
- Handles missing values with imputation
- Trains and evaluates multiple ML models:
  - Logistic Regression
  - K-Nearest Neighbors
  - Decision Tree
  - Random Forest
- Displays accuracy and confusion matrix for each model
- Highlights the best-performing model

---
### 🗂 Sample Dataset Structure

| Name           | Gender | Age | Billing Amount | Admission Type | Medical Condition | Test Results | Date of Admission | Discharge Date |
|----------------|--------|-----|----------------|----------------|-------------------|--------------|-------------------|----------------|
| John Doe       | Male   | 45  | 3200.50        | Emergency      | Hypertension      | Normal       | 2023-01-15        | 2023-01-18     |
| Jane Smith     | Female | 60  | 4500.75        | Routine        | Diabetes          | Abnormal     | 2023-02-10        | 2023-02-14     |
| Sam Williams   | Male   | 35  | 2800.00        | Emergency      | Asthma            | Inconclusive | 2023-03-05        | 2023-03-07     |
| Lisa Johnson   | Female | 50  | 5200.25        | Urgent         | Heart Disease     | Normal       | 2023-04-12        | 2023-04-17     |
| Robert King    | Male   | 70  | 6100.90        | Routine        | Stroke            | Abnormal     | 2023-05-01        | 2023-05-06     |
| Emily Brown    | Female | 28  | 2500.00        | Emergency      | Allergy           | Normal       | 2023-06-20        | 2023-06-22     |
| Michael Scott  | Male   | 55  | 4300.10        | Urgent         | Arthritis         | Inconclusive | 2023-07-15        | 2023-07-20     |
| Angela White   | Female | 48  | 4700.80        | Routine        | Diabetes          | Abnormal     | 2023-08-10        | 2023-08-15     |
| Daniel Green   | Male   | 33  | 3600.30        | Emergency      | Asthma            | Normal       | 2023-09-12        | 2023-09-14     |
| Sophie Turner  | Female | 38  | 3100.00        | Urgent         | Hypertension      | Normal       | 2023-10-01        | 2023-10-05     |

## ⚙️ Tech Stack

- **Python** – Core programming language  
- **Streamlit** – UI and interaction  
- **scikit-learn** – ML models and preprocessing  
- **Pandas, Seaborn, Matplotlib** – Data analysis and visualization  

---

## 🙌 Acknowledgments

- Built for medical data insights, patient segmentation, and diagnostic result classification  
- Inspired by real-world healthcare analytics applications  
---
## 📬 Contact

For questions or collaborations, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/aniket-gupta-90b49725a/) or [Email](aniket25287@gmail.com).
