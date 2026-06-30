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




st.title('Raw tables used.')

#st.sidebar.success("Select a page.")







game_info_df=pd.read_csv("chess_wc_history_game_info.csv")
#game_moves_df=pd.read_csv("chess_wc_history_moves.csv")
eco_codes_df=pd.read_csv("eco_codes.csv")












st.write('Debugging stuff')
st.dataframe(game_info_df)
st.dataframe(eco_codes_df)
