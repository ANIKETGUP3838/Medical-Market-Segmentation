# medical_segmentation_app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Medical Segmentation EDA", layout="wide")
st.title("🩺 Medical Market Segmentation: Age & Gender EDA")

# Upload dataset
uploaded_file = st.file_uploader("Upload your healthcare_dataset.csv", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Preprocess
    df['Gender'] = df['Gender'].str.strip().str.capitalize()
    age_bins = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    age_labels = ['10–20', '20–30', '30–40', '40–50', '50–60', '60–70', '70–80', '80–90']
    df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

    st.markdown("## 📊 Visual Explorations")

    # 1. Age Group vs Gender Count
    st.markdown("### 🔹 Patient Count by Age Group and Gender")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.countplot(data=df, x='Age Group', hue='Gender', ax=ax1)
    ax1.set_ylabel("Number of Patients")
    ax1.set_xlabel("Age Group")
    st.pyplot(fig1)

    # 2. Billing by Age Group & Gender
    st.markdown("### 🔹 Average Billing Amount by Age Group and Gender")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.barplot(data=df, x='Age Group', y='Billing Amount', hue='Gender', ci='sd', ax=ax2)
    ax2.set_ylabel("Average Billing")
    ax2.set_xlabel("Age Group")
    st.pyplot(fig2)

    # 3. Admission Type by Gender
    st.markdown("### 🔹 Admission Type Distribution by Gender")
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.countplot(data=df, x='Admission Type', hue='Gender', ax=ax3)
    st.pyplot(fig3)

    # 4. Top Conditions by Gender
    st.markdown("### 🔹 Top Medical Conditions by Gender")
    top_conditions = df['Medical Condition'].value_counts().nlargest(6).index
    filtered_df = df[df['Medical Condition'].isin(top_conditions)]
    fig4, ax4 = plt.subplots(figsize=(10, 5))
    sns.countplot(data=filtered_df, y='Medical Condition', hue='Gender', ax=ax4)
    st.pyplot(fig4)

else:
    st.info("Please upload a CSV file to begin analysis.")
