# 1 Red cards
# Join players - matches by match id
# filter only events containing *R*
# count red cards, group by country, by match
# average red cards by country
import pandas as pd 
def Players():
    df = pd.read_csv('world_cup/WorldCupPlayers.csv')
    return df
