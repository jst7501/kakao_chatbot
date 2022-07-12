import pandas as pd
import requests
from urllib import parse

apiKey = 'RGAPI-26d90cb3-1cb7-4f3b-bab9-b63b9e36bda1'
username = '광배쿤'  # 유저아이디
# champ = 'Udyr' # 원하는 챔프(머신러닝결과값)

id = parse.quote(username)  # 아이디를 URL 인코딩

url = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + \
    id + '?api_key=' + apiKey  # puuid값을 가져오기 위한 주소
r = requests.get(url)
r = r.json()
puuid = r['puuid']  # 해당 유저의 puuid 값 가져오기

# 랭크 n경기 매치아이디 가져오기
n = str(10)
rankUrl = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/' + \
    puuid + '/ids?queue=420&type=ranked&start=0&count='+n+'&api_key=' + apiKey
r = requests.get(rankUrl)
r = r.json()

rankId = r
print(rankId)


win = []
deaths = []
kills = []
assists = []
championName = []
for i in rankId:
    url = 'https://asia.api.riotgames.com/lol/match/v5/matches/' + i + '?api_key=' + apiKey
    r = requests.get(url)
    r = r.json()
    info = r['info']  # 전체 데이터에서 info를 추출
    part = info['participants']  # info 데이터에서 유저들의 정보 추출
    for j in range(0, 10):  # 총 10명의 유저중 내가 원하는 puuid값을 가진 유저를 추출
        if part[j]['puuid'] == puuid:
            # if part[j]['championName'] == champ: # 유저가 champ를 플레이했던 매치데이터를 추출
            win.append(part[j]['win'])
            deaths.append(part[j]['deaths'])
            kills.append(part[j]['kills'])
            assists.append(part[j]['assists'])
            championName.append(part[j]['championName'])
            # 승리, 킬뎃값 넣어주기
print(assists)

games = len(win)
df = pd.DataFrame(win)
df['win'] = win
df['kills'] = kills
df['assists'] = assists
df['deaths'] = deaths
df['championName'] = championName

df['KA'] = (df['kills']+df['assists'])
# print(df['KA']/df['deaths'])
df['KDA'] = df['KA'] / df['deaths']
df = df.drop(columns=0)
print(username + '님의 최근' + str(games) + '경기 ' + '의 퍼포먼스는?')
for i in range(0, games):
    print(str(i+1) + '경기: '+df['championName'][i] + str(df['kills'][i]) + '킬 ' + str(df['deaths']
          [i]) + '데스,'+str(df['assists'][i])+'어시스트로, KDA' + str(round(df['KDA'][i], 1)) + '를 달성하셨습니다.')
    print('챔피언 이미지', 'http://ddragon.leagueoflegends.com/cdn/12.12.1/img/champion/' +
          df['championName'][i]+'.png')
    if df['KDA'][i] < 3:
        print('해당 게임에서 ' + username + ' 님의 ' + ' 실력은' + ' [ 재앙 ] 입니다!')
    else:
        print('쫌 침. ')
