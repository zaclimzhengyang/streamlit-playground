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
sequence_input = "DNA Query \nTJNKJGNKJCNKJANCKJNKGJNKANCKJNKJTNKJNGKJNC\nLKEDMFLKEMGLKMTKMCKMKGMLKAMKMGKMKGMKCMKTMKMA \nGGGKGMKGMGKMGKMGKGMKMCKAAAAAAMKCMKMKMKMKMAKMHBRHUHTUH"

# sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=150)

sequence = sequence.splitlines()
# skip the sequence name (first line)
sequence
sequence = sequence[1:]
sequence
# concatenate list to string
sequence = ' * '.join(sequence)

st.write("""
***
""")

# prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

# 1. print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

# 2. print text
st.subheader("2. Print text")
st.write("There are " + str(X['A']) + ' adenine (A)')
st.write("There are " + str(X['T']) + ' thymine (T)')
st.write("There are " + str(X['G']) + ' adeline (guanine) (G)')
st.write("There are " + str(X['C']) + ' thymine (cytosine) (C)')

# 3. display dataframe
st.subheader("3. Display Dataframe")
df = pd.DataFrame.from_dict(X, orient="index")
df = df.rename({0: "count"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns = {"index": "nucleotide"})
st.write(df)

# 4. display bar chart using altair
st.subheader("4. Display Bar Chart")
p = alt.Chart(df).mark_bar().encode(
    x="nucleotide",
    y="count"
)

# widen the bar chart
p = p.properties(
    width=alt.Step(50)
)

# display
st.write(p)