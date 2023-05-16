import requests
import pandas as pd

# Store the area names and data
sarea_list = None
data_list = None


def getInfo() -> None:
    global sarea_list, data_list
    # Get data from the new URL
    url = 'https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv'
    response = requests.get(url)
    response.encoding='utf-8'
    
    if response.ok:
        file = open('a.csv',mode='w',encoding='utf-8',newline='')
        file.write(response.text)
        file.close()

    rowdata =pd.read_csv('a.csv')
    selectdata = rowdata[['country', 'year',
                          'co2', 'coal_co2', 'gas_co2', 'oil_co2', 'trade_co2']]
    
    selectdata = selectdata[selectdata['year'] >= 1991]
    selectdata = selectdata.reset_index(drop=True)
    
    return selectdata










'''def filterWrose3(self.selectdata,numbers) ->list:
    filtered_data = self.selectdata.tail(self.selectdata['co2']) 
'''


'''
selectdata1 = getInfo()
selectdata2 = selectdata1[selectdata1['year'] >= 1991]
selectdata2 = selectdata2.reset_index(drop=True)
print(selectdata2)
selectdata2.to_csv("data2.csv")
    #rowdata.info()
    # Rest of your code...
'''

