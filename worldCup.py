# 1 Red cards
# Join players - matches by match id
# filter only events containing *R*
# count red cards, group by country, by match
# average red cards by country
import pandas as pd 
import markdown
import os
import numpy as np
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

def ComeBack():
    df = Matches()
    come_backs = df[ 
            ((df['Half-time Home Goals'] < df['Half-time Away Goals']) & (df['Home Team Goals'] > df['Away Team Goals'])) |    
            ((df['Half-time Home Goals'] > df['Half-time Away Goals']) & (df['Home Team Goals'] < df['Away Team Goals']))
            ]
    come_backs['winner'] = np.where( come_backs['Home Team Goals'] > come_backs['Away Team Goals'], come_backs['Home Team Name'], come_backs['Away Team Name']) 
    come_back_count = come_backs.groupby('winner')['MatchID'].size().reset_index()
    highest_come_back_count = come_back_count.nlargest(2, "MatchID")
    code = """
        df = Matches()</br>
        come_backs = df[ </br>
            ((df['Half-time Home Goals'] < df['Half-time Away Goals']) & (df['Home Team Goals'] > df['Away Team Goals'])) |    </br>
            ((df['Half-time Home Goals'] > df['Half-time Away Goals']) & (df['Home Team Goals'] < df['Away Team Goals']))</br>
            ]</br>
        come_backs['wnner'] = np.where( come_backs['Home Team Goals'] > come_backs['Away Team Goals'], come_backs['Home Team Name'], come_backs['Away Team Name']) </br>
        come_back_count = come_backs.groupby('winner')['MatchID'].size().reset_index()</br>
        highest_come_back_count = come_back_count.nlargest(2, "MatchID")</br>
    """

    out = {}
    out["data"] = highest_come_back_count
    out["code"] = code
    return out
def champCurse():
    code = """
            # cup to get winner team, matches to get winner team details </br>
    matches = Matches()</br>
    cups     = Cups()</br>
    # join cups to matches by succsor cup and by home and away team'Home Team Name' or 'Away Team Name'</br>
    cups['Year_next_cup'] = cups['Year'] + 4 </br>
    # join winner home team</br>
    df_home = pd.merge(  cups, matches, </br>
                    left_on=['Winner','Year_next_cup'], </br>
                    right_on=['Home Team Name', 'Year']</br>
                )</br>
    # join away home team</br>
    df_away = pd.merge(  cups, matches, </br>
                    left_on=['Winner','Year_next_cup'], </br>
                    right_on=['Away Team Name', 'Year']</br>
                )</br>
    # union both </br>
    df = pd.concat([df_home, df_away])</br>
    # filter non group stages</br>
    df = df[df["Stage"].isin(['Round of 16', 'Quarter-finals', 'Semi-finals','Final'])]    </br>
    df['World Cup Winner'] = df['Country'] + ' - '  + df['Year_x'].astype(str)</br>
    df['Current Year'] = df['Year_y']</br>
    # group by unique cases</br>
    df = df.groupby(['World Cup Winner','Winner'])['Current Year'].unique().reset_index()</br>
    """
    # cup to get winner team, matches to get winner team details 
    matches = Matches()
    cups     = Cups()
    # join cups to matches by succsor cup and by home and away team'Home Team Name' or 'Away Team Name'
    cups['Year_next_cup'] = cups['Year'] + 4 
    # join winner home team
    df_home = pd.merge(  cups, matches, 
                    left_on=['Winner','Year_next_cup'], 
                    right_on=['Home Team Name', 'Year']
                )
    # join away home team
    df_away = pd.merge(  cups, matches, 
                    left_on=['Winner','Year_next_cup'], 
                    right_on=['Away Team Name', 'Year']
                )
    # union both 
    df = pd.concat([df_home, df_away])
    # filter non group stages
    df = df[df["Stage"].isin(['Round of 16', 'Quarter-finals', 'Semi-finals','Final'])]    
    df['World Cup Winner'] = df['Country'] + ' - '  + df['Year_x'].astype(str)
    df['Current Year'] = df['Year_y']
    # group by unique cases
    df = df.groupby(['World Cup Winner','Winner'])['Current Year'].unique().reset_index()
    out = {}
    out["data"] = df
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