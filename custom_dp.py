import streamlit as st
import pandas as pd
import numpy as np
import pickle



kmeans = pickle.load(open('mall_customer.pkl','rb'))

label_encoder,scaler,pca = pickle.load(open('mall_pipeline.pkl','rb'))


st.title("Mall Customer Segmentation")
st.markdown("### Enter Customer Details")

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 70, 30)
income = st.slider("Annual Income (k$)", 15, 150, 60)
score = st.slider("Spending Score (1-100)", 1, 100, 50)

# Prepare input
gender_encoded = label_encoder.transform([gender])[0]
input_df = pd.DataFrame([[gender_encoded, age, income, score]], 
                        columns=["Gender", "Age", "Annual Income (k$)", "Spending Score (1-100)"])

# Scale and apply PCA
scaled_input = scaler.transform(input_df)
pca_input = pca.transform(scaled_input)

# Predict cluster
cluster = kmeans.predict(pca_input)[0]

# Optional: Cluster interpretation
cluster_names = {
    0: "High Income & Low Spending",
    1: "Average Income & Average Spending",
    2: "Average Income & High Spending"
}

# Show result
st.success(f"Predicted Cluster: {cluster} → {cluster_names.get(cluster, 'Unknown')}")


