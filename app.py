import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load the dataset
df = pd.read_csv('zomato_dataset.csv')

# Streamlit app title
st.title("Zomato Dataset Exploratory Data Analysis")

# Display the dataframe
st.subheader("Dataset")
st.write(df.head())

# Count Plot of Various Locations
st.subheader("Count Plot of Various Locations")
plt.figure(figsize=(16, 10))
ax = sb.countplot(y=df['location'])
st.pyplot(plt.gcf())  # Display the plot in Streamlit
plt.clf()  # Clear the current figure

# Visualizing 'online_order'
st.subheader("Distribution of Online Order")
plt.figure(figsize=(6, 6))
sb.countplot(x=df['online_order'])
st.pyplot(plt.gcf())
plt.clf()

# Visualizing 'book_table'
st.subheader("Distribution of Book Table")
plt.figure(figsize=(6, 6))
sb.countplot(x=df['book_table'])
st.pyplot(plt.gcf())
plt.clf()

# Visualizing 'online_order' vs 'rate'
st.subheader("Online Order vs Rate")
plt.figure(figsize=(6, 6))
sb.boxplot(x='online_order', y='rate', data=df)
st.pyplot(plt.gcf())
plt.clf()

# Visualizing 'book_table' vs 'rate'
st.subheader("Book Table vs Rate")
plt.figure(figsize=(6, 6))
sb.boxplot(x='book_table', y='rate', data=df)
st.pyplot(plt.gcf())
plt.clf()