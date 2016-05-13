filename = "OfxDownload.ofx"
import ofxparse

ofx = ofxparse.OfxParser.parse(file(filename), "lxml")

secs = {}
for s in ofx.security_list:
    secs[s.uniqueid] = s.ticker
types = {4:'Sell', #Sell Stock
3:'Buy', #Buy Stock
2:'Buy', #Reinvest
1:'Sell', #SellMF
0:'Buy'} #Buy MF
form_name = "{aid},{tdate},{sdate},{sec},{type},{units},{price}\n"
with open('out.csv','w') as out:
    txt = form_name.format(aid='apid',
                    tdate='TradeDate',
                    sdate='Date',#SettleDate
                    sec='Symbol',
                    type='Type',
                    units='Shares',
                    price='Price')

    out.write(txt)
    for account in ofx.accounts:
         aid = account.account_id

         for trans in account.statement.transactions:

             sec = secs[trans.security]
             trans.unit_price
             t = types[trans.type]

             txt = form_name.format(aid=aid,
                             tdate=trans.tradeDate,
                             sdate=trans.settleDate,
                             sec=sec,
                             type=t,
                             units=trans.units,
                             price=trans.unit_price)
             out.write( txt)
