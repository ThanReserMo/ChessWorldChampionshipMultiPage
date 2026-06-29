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




st.title('Search a player\'s games between two dates!')

#st.sidebar.success("Select a page.")




start_date=st.date_input(label="Start Date",value='1866-01-01', min_value=datetime.date(year=1865, month=12, day=31), max_value=datetime.date(year=2022, month=12, day=31))
end_date=st.date_input(label='End date',value='2022-01-01', min_value=datetime.date(year=1866, month=12, day=31), max_value=datetime.date(year=2022, month=12, day=31))

start_date=pd.Timestamp(start_date)
end_date=pd.Timestamp(end_date)




game_info_df=pd.read_csv("chess_wc_history_game_info.csv")
#game_moves_df=pd.read_csv("chess_wc_history_moves.csv")
eco_codes_df=pd.read_csv("eco_codes.csv")


#https://stackoverflow.com/questions/37504672/pandas-dataframe-return-first-word-in-string-for-column
game_info_df.winner=game_info_df.winner.str.split(',').str[0]
game_info_df.white=game_info_df.white.str.split(',').str[0]
game_info_df.black=game_info_df.black.str.split(',').str[0]
game_info_df.loser=game_info_df.loser.str.split(',').str[0]


#https://stackoverflow.com/questions/49110156/finding-unique-combinations-of-columns-from-a-dataframe
game_and_eco=game_info_df[['game_id','eco']].drop_duplicates()

#https://stackoverflow.com/questions/53106428/pandas-merge-returning-only-null-values
game_and_eco_and_name=game_and_eco.merge(eco_codes_df)

game_info_and_name=game_and_eco_and_name.merge(game_info_df)

game_info_and_name['date_played']=pd.to_datetime(game_info_and_name['date_played'],format='%Y.%m.%d',errors='coerce')

games_within_time_period=game_info_and_name[(game_info_and_name.date_played>=start_date)&(game_info_and_name.date_played<=end_date)]

n=st.text_input(label='Enter the number of top openings.',value=5)

top_n_openings=games_within_time_period['eco_name'].value_counts()[:5]

st.write('Top 5 openings')
st.dataframe(top_n_openings)

game_info_for_top_5=games_within_time_period.loc[games_within_time_period.eco_name.isin(top_n_openings.eco_names)]

plt.figure()
opening_countplot=sns.countplot(data=game_info_for_top_5,x='eco_name',hue='result')
#https://stackoverflow.com/questions/26540035/rotate-label-text-in-seaborn
#stackoverflow.com/questions/20335290/matplotlib-plot-set-x-ticks
plt.xticks(rotation=90)
plt.figure(figsize=(12,12))
#https://discuss.streamlit.io/t/code-to-create-chart-with-seaborn-objects/36491
st.pyplot(opening_countplot.figure)


