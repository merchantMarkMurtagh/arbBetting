from lxml import html
from lxml import etree
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
page = requests.get('https://www.oddschecker.com/football/english/premier-league/leicester-v-tottenham/winner', verify=False)
tree = html.fromstring(page.content)

homeTeamName = tree.xpath('//*[@id="t1"]/tr[1]/td[1]/span[1]/@data-name')
awayName = tree.xpath('//*[@id="t1"]/tr[3]/td[1]/span[1]/@data-name')
homeOdd = {}
drawOdd = {}
awayOdd = {}

for i in range(2, 10):
	home = '//*[@id="t1"]/tr[1]/td[' + str(i) +']/text()'
	draw = '//*[@id="t1"]/tr[2]/td['+ str(i) +']/text()'
	away = '//*[@id="t1"]/tr[3]/td['+ str(i) +']/text()'
	bookie = '//*[@id="oddsTableContainer"]/table/thead/tr[4]/td['+str(i)+']/aside/a/@title'
	homeTeam = tree.xpath(home)
	drawTeam = tree.xpath(draw)
	awayTeam = tree.xpath(away)
	bookieName = tree.xpath(bookie)
	homeOdd[bookieName[0]]=homeTeam[0]
	drawOdd[bookieName[0]]=drawTeam[0]
	awayOdd[bookieName[0]]=awayTeam[0]


#bookie 
#//*[@id="oddsTableContainer"]/table/thead/tr[4]/td[2]/aside/a/title
# #win 
# //*[@id="t1"]/tr[1]/td[2]

# #draw
# //*[@id="t1"]/tr[2]/td[2]

# #lose 
# //*[@id="t1"]/tr[3]/td[2]
