import requests
import numpy as np
import pandas as pd

shot_chart_url = "https://stats.nba.com/stats/shotchartdetail?Period=0&VsConference=&LeagueID=00&LastNGames=0&TeamID=1610612741&PlayerPosition=&Location=&Outcome=&ContextMeasure=FGA&DateFrom=&StartPeriod=&DateTo=&OpponentTeamID=0&ContextFilter=&RangeType=&Season=1996-97&AheadBehind=&PlayerID=0&EndRange=&VsDivision=&PointDiff=&RookieYear=&GameSegment=&Month=0&ClutchTime=&StartRange=&EndPeriod=&SeasonType=Playoffs&SeasonSegment=&GameID="

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/124 (KHTML, like Gecko) Safari/125'}
# Get the webpage containing the data
response = requests.get(shot_chart_url, headers=headers)
# Grab the headers to be used as column headers for our DataFrame
headers = response.json()['resultSets'][0]['headers']
# Grab the shot chart data
shots = response.json()['resultSets'][0]['rowSet']

np.savetxt("9697.csv", shots, delimiter=",", fmt='%s')


