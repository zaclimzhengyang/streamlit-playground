import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#######################################################
# page title
#######################################################
image = Image.open('dna-logo.jpg')
st.image(image, use_column_width=True)

# *** shows a horizontal line; line break
st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")

#######################################################
# input text box
#######################################################
# st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')
sequence_input = "DNA Query \ntest1 for sequence input \nstart of the second line \n3rd line test"

# sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=150)

sequence = sequence.splitlines()
# skip the sequence name (first line)
sequence
sequence = sequence[1:]
sequence
# concatenate list to string
sequence = ''.join(sequence)

st.write("""
***
""")