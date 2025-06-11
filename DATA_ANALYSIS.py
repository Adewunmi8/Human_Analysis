import pandas as pd

import plotly.express as px
import streamlit as st 
st.title("PERSONALITY")
#create a data frame
df = pd.read_csv("personality_dataset.csv")
#st.table(df)


#code for data inspection 
st.markdown("### FIRST 5 DATA")
pa = df.head(5)
st.write(pa)

st.markdown("### LAST 5 DATA")
we = df.tail(5)
st.write(we)

st.markdown("### DATA DESCRIBE")
my = df.describe()
st.write(my)

st.markdown("### DATA SHAPE")
my = df.shape
st.write(my)

st.markdown("Post_frequency")
my = df['Post_frequency'].describe()
st.write(my)


le = df['Going_outside'].describe()
st.write(le)


st.title("Data_Graph 1")
fig = px.histogram(le, x= 'Going_outside', title = 'graph')
st.plotly_chart(fig, use_container_width=True)

st.title("Personality Distribution Pie Chart")
Personality_count = df['Personality'].value_counts().reset_index()
Personality_count.columns = ["Personality", "Count"]
fig = px.pie(Personality_count, names='Personality', values='Count', title="Personality Distribution")
st.plotly_chart(fig, use_container_width=True)

st.title("Data_Graph 2")
Personality_count = df['Personality']
Personality_count.columns = ["Personality", "Count"]
fig = px.bar(Personality_count, x= 'Personality', title=("graph"))
st.plotly_chart(fig, use_container_width=True)
