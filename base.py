import requests
from bs4 import BeautifulSoup
import re
import numpy
import pandas as pd


class KenPom:

    def __init__(self, start=2002, end=2003):
        self.start = start
        self.end = end
        self.df = self.scrape_ken()

    def scrape_ken(self):
        """
        :return: DataFrame of KenPom's complete College Rankings / Advanced Stats
        """
        season = self.end

        main_pom = list()

        while season >= self.start:
            url = 'https://kenpom.com/index.php?y=' + str(season)
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'lxml')

            table = soup.table
            table_rows = table.find_all('tr')

            team_rows = list()
            for tr in table_rows:
                td = tr.find_all('td')
                row = [i.text for i in td]
                team_rows.append(row)

            cols = ["Rk", "Team", "Conf", "Record", "AdjEM", "AdjO", "a", "AdjD", "b", "AdjT", "c", "Luck", "d",
                    "SoS AdjEM", "e", "OppO", "f", "OppD", "g", "NCOS AdjEM", "h"]

            ken_pom = pd.DataFrame(team_rows[2:], columns=cols)

            ken_pom.drop(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], axis=1, inplace=True)

            ken_pom['Rk'] = ken_pom['Rk'].astype('float')
            ken_pom['AdjEM'] = ken_pom['AdjEM'].astype('float')
            ken_pom['AdjO'] = ken_pom['AdjO'].astype('float')
            ken_pom['AdjD'] = ken_pom['AdjD'].astype('float')
            ken_pom['AdjT'] = ken_pom['AdjT'].astype('float')
            ken_pom['Luck'] = ken_pom['Luck'].astype('float')
            ken_pom['SoS AdjEM'] = ken_pom['SoS AdjEM'].astype('float')
            ken_pom['OppO'] = ken_pom['OppO'].astype('float')
            ken_pom['OppD'] = ken_pom['OppD'].astype('float')
            ken_pom['NCOS AdjEM'] = ken_pom['NCOS AdjEM'].astype('float')
            ken_pom['Season'] = season

            season -= 1

            main_pom.append(ken_pom)

        final_ken = pd.concat(main_pom)
        final_ken.dropna(axis=0, inplace=True)

        final_ken['Team'] = [re.sub(r'\d+', '', x).strip() for x in final_ken['Team']]

        return final_ken

    def team(self, team):
        return self.df[self.df['Team'] == str(team)]

    def team_record(self, team):
        df = self.df[self.df['Team'] == str(team)]

        seasons = [int(x) for x in df['Season']]

        raw_record = [x.split("-") for x in df['Record']]
        wins = [int(x[0]) for x in raw_record]
        losses = [int(x[1]) for x in raw_record]

        record = pd.DataFrame([seasons, wins, losses]).T
        record.columns = ['Season', 'Wins', 'Losses']
        return record

    def conference(self, conference):
        return self.df[self.df['Conf'] == str(conference)]

    def season(self, season):
        return self.df[self.df['Season'] == int(season)]
