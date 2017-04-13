# -*- coding: UTF-8 -*-
from datetime import date
import tushare as ts
import json


hq = ts.get_today_all()
hq = hq[['code', 'name', 'changepercent', 'trade', 'volume', 'turnoverratio']].sort_values('changepercent', ascending=False)
adf = hq.head(15)
print adf
print type(adf)
template = "aa.docx"
document = ts.MailMerge(template)
print(document.get_merge_fields())
# heads = {'today':'{:%Y-%m-%d}'.formate(date.today()),
heads = {'today':'2017-3-8',
    'sh':'3253.43',
    'shp':'0.06%',
    'sz':'10443.73',
    'sh':'0.11%',
    'cyb':'1938.44',
    'cybp':'0.65%',}
document.merge(**heads)
# document.merge_rows('code', json.loads(adf.to_json(orient='records', force_ascii=False)))
document.write('aa.docx')



