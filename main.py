import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

response = requests.get("https://www.basketball-reference.com/leagues/NBA_2023_per_game.html")

soup = BeautifulSoup(response.content, "html.parser")

table = soup.select("tr td[data-stat='player'][csk]")

players = []

for player in table:
    players.append(player.text)

df = pd.DataFrame(players)

print(df)

conn = sqlite3.connect("players.db")

# export df to sql

df.to_sql("players", conn, if_exists="replace")

# now we can read it with db sqlite browser for exemple and see that it works 