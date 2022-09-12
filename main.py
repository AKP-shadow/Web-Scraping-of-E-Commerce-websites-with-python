 
from autoscraper import AutoScraper
import json
page_url = 'https://www.amazon.in/s?k=laptop'

elements =["ASUS VivoBook 15 (2021), 15.6-inch (39.62 cm) HD, Dual Core Intel Celeron N4020, Thin and Light Laptop (4GB RAM/256GB SSD/Integrated Graphics/Windows 11 Home/Transparent Silver/1.8 Kg), X515MA-BR011W",
'25,990 ', '1,711','https://www.amazon.in/ASUS-15-6-inch-Integrated-Transparent-X515MA-BR011W/dp/B09SGGB687/ref=sr_1_3?keywords=laptop&qid=1662879498&sr=8-3']

scraper =  AutoScraper()
result = scraper.build(page_url,elements)

result = scraper.get_result_similar(page_url,grouped=True)


# print(result)

grp_list = [name for name in result]


scraper.set_rule_aliases({grp_list[0]:'title',grp_list[1]:'price',grp_list[2]:'url'})
scraper.keep_rules([grp_list[0],grp_list[1],grp_list[2]])
scraper.save('amz-search-results')


result  = scraper.get_result_similar('https://www.amazon.in/s?k=acer+laptop',group_by_alias=True)
with open('results.json','w+') as results:
    results.write(json.dumps(result ,indent=4))
print(result ['title'])

