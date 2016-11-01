# -*- coding: UTF-8 -*-
import urllib2, json

nba_url = 'http://china.nba.com/static/data/scores/miniscoreboard.json'

def get_nba():
    request = urllib2.Request(nba_url)
    response = urllib2.urlopen(request)
    content = response.read()

    if content:
        try:
            result = json.loads(str(content))
        except:
            return None
        return result
    return None

def nba():
    nba_info = get_nba()
    if nba_info == None:
        return None
    games = nba_info['payload']['today']['games']
    if len(games) == 0:
        return None
    results = []
    for game in games:
        awayTeam = game['awayTeam']['profile']['name'].encode('utf-8')
        awayScore = game['boxscore']['awayScore']
        homeTeam = game['homeTeam']['profile']['name'].encode('utf-8')
        homeScore = game['boxscore']['homeScore']
        status = game['boxscore']['statusDesc'].encode('utf-8')
        sting = awayTeam + ' @ ' + homeTeam + ' '+ str(awayScore) + ' : ' + str(homeScore) + '  ' + status
        results.append(sting.decode('utf-8'))
    return results