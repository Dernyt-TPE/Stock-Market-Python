from datetime import date, timedelta
from nsepy.history import get_price_list
import pandas as pd
import datetime
import calendar


prices_current ={}
prices_previous={}



prices_current = get_price_list(dt=date(2021,7,30))
prices_previous = get_price_list(dt=date(2021,7,29))

df_current = pd.DataFrame(prices_current)
df_previous = pd.DataFrame(prices_previous)

prices_dict  = {}
details_dict  = {}

# def subDay(sub):
#     sub_day = int(sub[0:2])
#     sub_month = int(sub[3:5])
#     if (sub_month == '01' or sub_month=='03' or sub_month=='05' or sub_month=='07' or sub_month=='08' or sub_month=='10' or sub_month=='12'):
#         if(sub_day == '01'):
#             print("us")
    


# def findDay(date):
#     subDay(date)
#     day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    
#     return (calendar.day_name[day])


# def get_prev_trading_date(da):
    
#     day=findDay(da)
#     if (day=='Sunday' or day=='Saturday'):
#         print('Holiday Occured')
    



def get_trading_info(ticket):
    cell=""
    for i in range(0,1516):
        cell=df_current['SYMBOL'].values[i]
        if(cell.__eq__(ticket)):
            # print(df['OPEN'].values[i])
            details_dict={'open': df_current['OPEN'].values[i],
                          'high': df_current['HIGH'].values[i],
                          'low': df_current['LOW'].values[i],
                          'close': df_current['CLOSE'].values[i],
                          'prev_open': df_previous['OPEN'].values[i],
                          'prev_high': df_previous['HIGH'].values[i],
                          'prev_low': df_previous['LOW'].values[i],
                          'prev_close': df_previous['CLOSE'].values[i]}
            return details_dict


def display_information(final):
    df = pd.DataFrame(final)

    df.to_csv('Python - Stock Market Data by Pranjal.csv')
    print("\n Your CSV file is Saved at this file's location named 'Python - Stock Market Data by Pranjal.csv' !!")


symbol_names = input("Enter names separated by space for a list: symbol_names = ").split()
print('\n')
# dat = input("Enter the current current date (Example format: 31 07 2021) :" )

# dat2 = input("Enter the previous trading date (Example format: 31 07 2021) :" )






for name in symbol_names:
    name=name.upper()
    k=get_trading_info(name)
    prices_dict[name] = k
    
    
print(prices_dict)

display_information(prices_dict)



