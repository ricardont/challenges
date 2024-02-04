# 1 Red cards
# Join players - matches by match id
# filter only events containing *R*
# count red cards, group by country, by match
# average red cards by country
import pandas as pd 
import markdown
import os

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
    df_avg_max = df_avg.nlargest(3, "RedCount")
    code =  '''
        df = Players() </br>
        df.fillna('', inplace=True) </br>
        df_count = df[df['Event'].str.contains('R')].groupby(['Team Initials', 'MatchID'])['Event'].size().reset_index(name='RedCount') </br>
        df_avg = df_count.groupby('Team Initials')['RedCount'].mean('RedAvg').reset_index() </br>
        df_avg_max = df_avg.nlargest(3, "RedCount") </br>
    '''
    out = {}
    out["data"] = df_avg_max
    out["code"] = code
    return out
def md():
    markdown_file = 'world_cup/data_analyst_world_cup.md'
    html_content = ''
    with open(markdown_file) as f:     
        html_content = markdown.markdown(f.read())   
    file = open("world_cup/data_analyst_world_cup.html", "w")
    file.write(html_content)
    file.close()
    return  html_content   