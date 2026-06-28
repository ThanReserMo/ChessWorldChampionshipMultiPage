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




st.title('Hi! This is a personal data analysis and engineering project about statistics from the Chess World Championship!')

st.write('The data set used for this project comes from the Kaggle link below!')

st.link_button(label='Kaggle link',url='https://www.kaggle.com/datasets/zq1200/world-chess-championships-1866-to-2021')

st.write('Use the buttons in the sidebar to navigate the site!')



