import requests
import json
import sys
from models import Player


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
    'LeagueID': '00',
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
    'Season': '',
    'SeasonSegment': '',
    'SeasonType': '',
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
        'http://stats.nba.com/stats/leaguedashplayerstats?', params=payload, headers=headers)
    print(r.url)
    try:
        with open('stats.json', 'w') as f:
            data = json.loads(f.read())
            for row in data['rowSet']:
                row = zip(data['headers'], row)
                Player.objects.create(
                    player_id=row['player_id'],
                    player_name=row['player_name'],
                    team_id=row['team_id'],
                    team_abbreviation=row['team_abbreviation'],
                    age=row['name'],
                    gp=row['gp'],
                    w=row['w'],
                    l=row['l'],
                    w_pct=row['w_pct'],
                    min=row['min'],
                    fgm=row['fgm'],
                    fga=row['fga'],
                    fg_pct=row['fg_pct'],
                    fg3m=row['fg3m'],
                    fg3a=row['fg3a'],
                    fg3_pct=row['fg3_pct'],
                    ftm=row['ftm'],
                    fta=row['fta'],
                    ft_pct=row['ft_pct'],
                    oreb=row['oreb'],
                    dreb=row['dreb'],
                    reb=row['reb'],
                    ast=row['ast'],
                    tov=row['tov'],
                    stl=row['stl'],
                    blk=row['blk'],
                    blka=row['blka'],
                    pf=row['pf'],
                    pfd=row['pfd'],
                    pts=row['pts'],
                    plus_minus=row['plus_minus'],
                    nba_fantasy_pts=row['nba_fantasy_pts'],
                    dd2=row['dd2'],
                    td3=row['td3'],
                    gp_rank=row['gp_rank'],
                    w_rank=row['w_rank'],
                    l_rank=row['l_rank'],
                    w_pct_rank=row['w_pct_rank'],
                    min_rank=row['min_rank'],
                    fgm_rank=row['fgm_rank'],
                    fga_rank=row['fga_rank'],
                    fg_pct_rank=row['fg_pct_rank'],
                    fg3m_rank=row['fg3m_rank'],
                    fg3a_rank=row['fg3a_rank'],
                    fg3_pct_rank=row['fg3_pct_rank'],
                    ftm_rank=row['ftm_rank'],
                    fta_rank=row['fta_rank'],
                    ft_pct_rank=row['ft_pct_rank'],
                    oreb_rank=row['oreb_rank'],
                    dreb_rank=row['dreb_rank'],
                    reb_rank=row['reb_rank'],
                    ast_rank=row['ast_rank'],
                    tov_rank=row['tov_rank'],
                    stl_rank=row['stl_rank'],
                    blk_rank=row['blk_rank'],
                    blka_rank=row['blka_rank'],
                    pf_rank=row['pf_rank'],
                    pfd_rank=row['pfd_rank'],
                    pts_rank=row['pts_rank'],
                    plus_minus_rank=row['plus_minus_rank'],
                    nba_fantasy_pts_rank=row['nba_fantasy_pts_rank'],
                    dd2_rank=row['dd2_rank'],
                    td3_rank=row['td3_rank'],
                    cfid=row['cfid'],
                    cfparams=row['cfparams']
                )

    except requests.exceptions.ConnectionError as err:
        print('There was a problem getting the requested url. ERROR: ', err, r.status_code)
        sys.exit(1)


get_stats(Season='2017-18', SeasonType='Regular Season')
