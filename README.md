# 🩺 Medical Market Segmentation & ML Prediction Dashboard

A Streamlit web application for interactive **Exploratory Data Analysis (EDA)**, **Unsupervised Clustering**, and **Machine Learning-based Test Result Prediction** using healthcare datasets.

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
