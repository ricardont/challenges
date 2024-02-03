# 1 Red cards
# Join players - matches by match id
# filter only events containing *R*
# count red cards, group by country, by match
# average red cards by country
import pandas as pd 

def Players():
    df = pd.read_csv('world_cup/WorldCupPlayers.csv')
    return df

def Matches():
    df = pd.read_csv('world_cup/WorldCupMatches.csv')
    return df

def Cups():
    df = pd.read_csv('world_cup/WorldCups.csv')
    return df

def RedFlagsAvg():
    df = Players()
    df.fillna('', inplace=True)
    df_count = df[df['Event'].str.contains('R')].groupby(['Team Initials', 'MatchID'])['Event'].size().reset_index(name='RedCount')
    df_avg = df_count.groupby('Team Initials')['RedCount'].mean('RedAvg').reset_index()
    df_avg_max = df_avg['RedCount'].nlargest(2).reset_index()
    return df_avg_max
    

# df =  df[df['Event'].str.contains('R')]
# red_flags_count = Matches().groupby('Category')['Value'].count().