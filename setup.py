import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()

h = {
    "user-agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

url = "https://resultados.as.com/resultados/futbol/inglaterra/"

resp = requests.get(url, headers=h)

soup = BeautifulSoup(resp.content, "html.parser")

#TEAMS

eq = soup.find_all("a", class_="nombre-equipo")

teams = list()

for e in eq:
    teams.append(e.text.replace("\n",""))

#POINTS

point = soup.find_all("td", class_="destacado")

points = list()

for p in point:
    points.append(p.text.replace("\n",""))

#DATAFRAME

df = pd.DataFrame({"Teams:":teams, "Points:":points} , index=list(range(1,21)))
df.to_csv("./data.csv")

#CREATE .TXT FILE

file = open("Premiere-table-today.txt", "w")
file.write("PREMIERE LEAGUE TABLE - " + str(now.day) + "/" + str(now.month) + "/" + str(now.year) + "\n")
file.write(str(df) + "\n" + "\n" + "\n")
file.close()