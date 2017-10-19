import requests
import json
import sys
import urllib
from bs4 import BeautifulSoup

print('Making request...')
urldict = {
    'College': '',
    'Conference': '',
    'Country': '',
    'DateFrom': '',
    'DateTo': '',
    'Division': '',
    'DraftPick': '',
    'DraftYear': '',
    'GameScope': '',
    'GameSegment': '',
    'Height': '',
    'LastNGames': '0',
    'LeagueID': '0',
    'Location': '',
    'MeasureType': 'Base',
    'Month': '0',
    'OpponentTeamID': '0',
    'Outcome': '',
    'PORound': '0',
    'PaceAdjust': 'N',
    'PerMode': 'PerGame',
    'Period': '0',
    'PlayerExperience': '',
    'PlayerPosition': '',
    'PlusMinus': 'N',
    'Rank': 'N',
    'Season': '2015' + '-' + '16',
    'SeasonSegment': '',
    'SeasonType': 'Regular+Season',
    'ShotClockRange': '',
    'StarterBench': '',
    'TeamID': '0',
    'VsConference': '',
    'VsDivision': '',
    'Weight': ''
}


def get_stats(**kwargs):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    payload = urldict.copy()
    payload.update(kwargs)
    r = requests.get(
        'https://stats.nba.com/stats/leaguedashplayerstats?', params=payload, headers=headers)
    print(r.url)
    try:
        # soup = BeautifulSoup(r, 'html.parser')
        data = json.loads(r.content)
        with open('stats.json', 'w') as f:
            json.dump(data, f)
        # print(json.dumps(data, indent=2, sort_keys=True))

    except requests.exceptions.ConnectionError as err:
        print('There was a problem getting the requested url. ERROR: ', err, r.status_code)
        sys.exit(1)


get_stats()