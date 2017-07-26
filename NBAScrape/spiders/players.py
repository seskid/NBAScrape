import scrapy
import re

from NBAScrape.items import NbascrapeItem

class PlayerSpider(scrapy.Spider):
    name = "player"
    
    #def __init__(self,*a,**kw):
    start_urls = [
                  'http://www.spotrac.com/nba/atlanta-hawks/cap/',
                  'http://www.spotrac.com/nba/boston-celtics/cap/',
                  'http://www.spotrac.com/nba/brooklyn-nets/cap/',
                  'http://www.spotrac.com/nba/charlotte-hornets/cap/',
                  'http://www.spotrac.com/nba/chicago-bulls/cap/',
                  'http://www.spotrac.com/nba/cleveland-cavaliers/cap/',
                  'http://www.spotrac.com/nba/dallas-mavericks/cap/',
                  'http://www.spotrac.com/nba/denver-nuggets/cap/',
                  'http://www.spotrac.com/nba/detroit-pistons/cap/',
                  'http://www.spotrac.com/nba/golden-state-warriors/cap/',
                  'http://www.spotrac.com/nba/houston-rockets/cap/',
                  'http://www.spotrac.com/nba/indiana-pacers/cap/',
                  'http://www.spotrac.com/nba/los-angeles-clippers/cap/',
                  'http://www.spotrac.com/nba/los-angeles-lakers/cap/',
                  'http://www.spotrac.com/nba/memphis-grizzlies/cap/',
                  'http://www.spotrac.com/nba/miami-heat/cap/',
                  'http://www.spotrac.com/nba/milwaukee-bucks/cap/',
                  'http://www.spotrac.com/nba/minnesota-timberwolves/cap/',
                  'http://www.spotrac.com/nba/new-orleans-pelicans/cap/',
                  'http://www.spotrac.com/nba/new-york-knicks/cap/',
                  'http://www.spotrac.com/nba/oklahoma-city-thunder/cap/',
                  'http://www.spotrac.com/nba/orlando-magic/cap/',
                  'http://www.spotrac.com/nba/philadelphia-76ers/cap/',
                  'http://www.spotrac.com/nba/phoenix-suns/cap/',
                  'http://www.spotrac.com/nba/portland-trail-blazers/cap/',
                  'http://www.spotrac.com/nba/sacramento-kings/cap/',
                  'http://www.spotrac.com/nba/san-antonio-spurs/cap/',
                  'http://www.spotrac.com/nba/toronto-raptors/cap/',
                  'http://www.spotrac.com/nba/utah-jazz/cap/',
                  'http://www.spotrac.com/nba/washington-wizards/cap/',
                ]

    def parse(self, response):
        item=NbascrapeItem()
        n=1;
        playername=""
        thename=""
        spacePos=0
        salary=""
        rosterCount=""
        baseNum=0;       

        #get number of players under contract
        rosterHeader=response.xpath('.//*[@id="main"]/div[6]/table[1]/thead/tr/th[1]/text()').extract()
        for s in rosterHeader[0]:
            if s.isdigit():
                rosterCount=rosterCount+s        

        for num in range(1,int(rosterCount)+1):
            playername=response.xpath('(.//*[@class="player"]/a/text())[{0}]'.format(num)).extract()
            thename=playername[0]
            spacePos=thename.index(' ')
            item['FirstName']=thename[0:spacePos]
            item['LastName']=thename[spacePos+1:]
            salary=response.xpath('(.//*[@class="cap info"]/text())').extract()
            item['Salary']= re.sub('[$,]','',salary[baseNum])
            item['TeamID']=1+(self.start_urls.index(response.url))

            #skip trade kicker,likely incent, and cap figure 
            baseNum=baseNum+4
            yield item







