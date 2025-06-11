import math
import streamlit as st

st.markdown("HELLO")
st.markdown("# HELLO")
st.markdown("HELLO JAMIAT")
st.markdown("## HELLO")
st.markdown("### HELLO")
st.markdown("#### HELLO")
st.markdown("##### HELLO")
st.markdown("###### HELLO")

#rite the length of the two shorter side of a right angle triangle as parameter

st.title("hypotenuse calculator")
st.number_input("enter your hypotenuse value",value=0)
st.number_input("enter your opposite value", value=0)

#function to calculate hypotenuse

def calculate_hypotenuse(adj, opp):
    return math.sqrt(adj ** 2 + opp ** 2)

# button to trigger calculation
    if st.button("calculate hypotenuse"):
    hypotenuse = calculate_hypotenuse(adj, opp)
    st.success(f"the length of the hypotenuse is: {hypotenuse:.2f}")