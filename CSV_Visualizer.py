import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV Visualizer")
upload_file = st.file_uploader("Select a .csv file type!", type= "csv")

if upload_file is not None:
    dataframe = pd.read_csv(upload_file)
    subtitle = st.subheader("Data Preview")
    st.write(dataframe.head())
    
    st.subheader("Data summery")
    st.write(dataframe.describe())
    
    st.subheader("Fliter Data!")
    columns = dataframe.columns.tolist()
    selected_column = st.selectbox("Select Column to filter by:", columns)
    unique_value = dataframe[selected_column].unique()
    selected_value = st.selectbox("Select Value",unique_value)
    
    filtered_df = dataframe[dataframe[selected_column] == selected_value]
    st.write(filtered_df)
    
    st.subheader("Plot Data")
    x_column = st.selectbox("select x-axis column",columns)
    y_column = st.selectbox("select y-axis column",columns)
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Waiting for file upload")