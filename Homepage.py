import streamlit as st
import pandas as pd
import chess.pgn
from converter.pgn_data import PGNData
from Openix import ChessOpeningsLibrary
import datetime
import io
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('dark_background')




st.title('Hello!')

st.write('This is a personal data analysis and engineering project using data from the Chess World Championship.')


url = "https://www.kaggle.com/datasets/zq1200/world-chess-championships-1866-to-2021'"

st.markdown("The data set used for this project can be found in this [Kaggle link](%s)! " % url)



st.write('Use the buttons in the sidebar to navigate the site!')



