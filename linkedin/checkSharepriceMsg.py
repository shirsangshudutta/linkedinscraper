from nsetools import Nse
from pprint import pprint
import pandas as pd
from datetime import date,datetime,timedelta
from nsepy import get_history
from twilio.rest import Client
msg=''
nse = Nse()
df = pd.read_csv('C:\\Users\\pc\\Desktop\\stocks.csv')
i=0

for index, row in df.iterrows():
    print(row['Stock'], row['qty'])
# stk=df['Stock'].values
# for x in stk:
    q = nse.get_quote(row['Stock'])
#     # print("Company: " + q['companyName'])
#     # print("Buy Price : " + str(q['buyPrice1']))

#     # print(type(q))
#     # print(q['symbol'])
#     tot=0
#     print(x)

    today_tot=q['lastPrice']*row['qty']
    print('Sym',q['symbol'],'LTP',q['lastPrice'],'qty:',row['qty'],'Total:',today_tot)
    print('Today total is ',today_tot)
    # present = datetime.now()
    # # pres=present.strftime('%y,%m,%d')
    # yesterday = present - timedelta(1)
    # yes=yesterday.strftime('%y,%m,%d')
    # print('Present :',pres,'yesterday :',yes)
    # print(type(yes))
    present = date.today()
    print('present',present)
    yesterday = present - timedelta(days = 1)
    print("Yesterday was: ", yesterday)
    sbin = get_history(symbol=q['symbol'],
                   start=yesterday,
                   end=present)
    for index, row1 in sbin.iterrows():
        prev=row1['Prev Close']
    # prev_tot=row['qty']*prev
        # print('prev_tot',prev)    	
# # # print(q['symbol'],q['lastPrice'])exit
        prev_tot=prev*row['qty']
        print('yesterday total is ',prev_tot)
        diff=today_tot-prev_tot
        print('Difference',diff)
        if (diff>500) :
            msg=msg+q['symbol']+' '+str(diff)+ '\n'
            print(msg)
            # importing the client from the twilio
            # Your Account Sid and Auth Token from twilio account
            # account_sid = 'ACee9a295608ede8515069f2ba6ade1819'
            # auth_token = '7bb97de672e81a159fbe2c75dfa03484'
            # instantiating the Client
        #     client = Client(account_sid, auth_token)
        # # sending message
        #     message = client.messages.create(body=msg, from_='+16075245277', to='+917003772119')
            # printing the sid after success
            # print(message.sid)
account_sid = 'ACee9a295608ede8515069f2ba6ade1819'
auth_token = '7bb97de672e81a159fbe2c75dfa03484'            
client = Client(account_sid, auth_token)
    # sending message
message = client.messages.create(body=msg, from_='+16075245277',to='+917003772119')  
print(message.sid)

 
