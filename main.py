import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl



mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False


st.title("Preditivo de Turnover")

y = [10, 20, 30, 40]
x = ['Marcio', 'Regiane', 'Zach', 'Sr Renato']

df = pd.DataFrame({'x':x, 'y':y})

fig, ax = plt.subplots()
ax.bar(df['x'], df['y'])


st.pyplot(fig)

