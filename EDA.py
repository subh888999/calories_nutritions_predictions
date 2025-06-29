import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io

def run_EDA(df):
    st.sidebar.markdown("📊 :blue[Exploratory Data Analysis]")
    eda_type = st.sidebar.selectbox("Select EDA Type", ["Univariate", "Bivariate", "Multivariate"])

    st.subheader("📌 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📋 Dataset Info")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.subheader("🧭 Missing Values")
    st.write(df.isnull().sum())

    st.subheader("🔁 Duplicate Rows")
    st.write(df.duplicated().sum())

    st.subheader("📈 Descriptive Statistics")
    st.write(df.describe(include='all'))

    # Univariate Analysis
    if eda_type == "Univariate":
        st.header("📊 Univariate Analysis")
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        selected_col = st.selectbox("Select a numeric column", numeric_cols)

        fig, ax = plt.subplots(1, 2, figsize=(14, 4))
        sns.histplot(df[selected_col], kde=True, ax=ax[0], color='skyblue')
        ax[0].set_title(f"Distribution of {selected_col}")

        sns.boxplot(x=df[selected_col], ax=ax[1], color='orange')
        ax[1].set_title(f"Boxplot of {selected_col}")

        st.pyplot(fig)

    # Bivariate Analysis
    elif eda_type == "Bivariate":
        st.header("📊 Bivariate Analysis")
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        num_feature = st.selectbox("Select a numeric feature", numeric_cols)
        cat_feature = st.selectbox("Select a categorical feature", ['Gender', 'Activity_Level', 'Fitness_Goal'])

        plt.figure(figsize=(14, 6))
        sns.boxplot(x=cat_feature, y=num_feature, data=df, palette="Set2")
        plt.xticks(rotation=45)
        plt.title(f"{num_feature} vs {cat_feature}")
        st.pyplot(plt)

    # Multivariate Analysis
    elif eda_type == "Multivariate":
        st.header("📊 Multivariate Analysis")

        st.subheader("📉 Correlation Heatmap (Numerical Features)")
        fig, ax = plt.subplots(figsize=(10, 6))
        numeric_df = df.select_dtypes(include='number')
        corr = numeric_df.corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        st.pyplot(fig)
