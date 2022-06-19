# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:35:18 2022

@author: Kishore
"""

"""

Open weather API is used for this Data collection

"""

# Importing requests and json
import requests, json
import sys
import time
import pandas as pd
import os

#from collections import defaultdict

# base url
Base_Url="http://api.openweathermap.org/data/2.5/air_pollution/history?"

# city conisdered - Colombo
Latitude="6.9270786"
Longitude="79.86124300000006"



# beginning Time stamp
beginning_points = [1356978600, 1388514600, 1420050600, 
             1451586600, 1483209000, 1514745000,
             1546281000, 1577817000, 1609439400]




# end Time stamp

end_points = [1388514600, 1420050600, 1451586600, 
       1483209000, 1514745000, 1546281000, 
       1577817000, 1609439400, 1640975400]


points= ["&start=1356978600&end=1388514600", "&start=1388514600&end=1420050600", "&start=1420050600&end=1451586600", 
         "&start=1451586600&end=1483209000", "&start=1483209000&end=1514745000", "&start=1514745000&end=1546281000", 
         "&start=1546281000&end=1577817000", "&start=1577817000&end=1609439400", "&start=1609439400&end=1640975400", ]



# Api_key
Key="9f2a63eaeb2b998f653f2afe32b7a484"


# creating a for loop for getting data from multiple years
Urls = []

# years List
years = [2013,2014,2015,2016,2017,2018,2019,2020,2021]


dt = []
co= []
no= []
no2= []
o3 = []
so2 =[]
pm2_5 =[]
pm10 = []
nh3 = []
AQI = []

for point in points:
    Url = Base_Url + "lat=" + Latitude + "&lon=" + Longitude + point + "&appid=" + Key
        
    Urls.append(Url)
    
    
    
#print(Urls)


#  Creating a loop for collecting data from each url
def api_call():
    for Url in Urls:
        # HTTP request
        response=requests.get(Url)
        # checking the status code of the request
        if response.status_code == 200:
            
            # loop for saving files as years
            for year in years:
                # getting data in the json format
                data = response.json()
                main=data['list']
                print("JSON created for {}".format(year))


            
    
                    
    
    
                    
                    # saving the json file
                with open ("Data/API_Data/Json Dumps/{}.json".format(year),"w",encoding="utf-8") as json_file:
                    json.dump(main,json_file)
                    print("JSON saved for {}".format(year))
                        
                        
                    # reading each json
                dumped_data="D:/Studies/My Projects/Data Science/Air Quality Indicator Prediction/Data/API_Data/Json Dumps/{}.json".format(year)
                   
                Jsdata = json.load(open(dumped_data))
                print("JSON loaded for {}".format(year))
                    
                    
                i=0
                    
    
                for i in range(len(main)):
                        dt.append(Jsdata[i]["dt"])
                        co.append(Jsdata[i]["components"]["co"])
                        no.append(Jsdata[i]["components"]["no"])
                        no2.append(Jsdata[i]["components"]["no2"])
                        o3.append(Jsdata[i]["components"]["o3"])
                        so2.append(Jsdata[i]["components"]["so2"])
                        pm2_5.append(Jsdata[i]["components"]["pm2_5"])
                        pm10.append(Jsdata[i]["components"]["pm10"])
                        nh3.append(Jsdata[i]["components"]["nh3"])
                        AQI.append(Jsdata[i]["main"]["aqi"])    
                        
                        
                i=i+1
    
                    
                    
                    
                    
                    
                df = pd.DataFrame()
                df['datetime'] = dt
                df['co'] = co
                df['no'] = no
                df['no2'] = no2
                df['o3'] = o3
                df['so2'] = so2
                df['pm2_5'] = pm2_5
                df['pm10'] = pm10
                df['nh3'] = nh3
                df['AQI'] = AQI   
                
                #wirte CSV for each years
                df.to_csv(r"Data/API_Data/Full_AQI.csv")
               
                        
                        
                     
                    
                        
                     
                    
                    #df=json_normalize(Jsdata, "components" ["co", "no", "no2", "o3", "so2", "pm2_5", "pm10", "nh3"],max_level=1)
                    #df = json_normalize(Jsdata)
                    
    
                
                    
            
                    
               
                            
               
                            
                
            sys.stdout.flush()
            


# time taken
if __name__=="__main__":
    start_time=time.time()
    api_call()
    stop_time=time.time()
    print ("Time Taken - {}".format(stop_time-start_time))
        

                     
        
        
        

        
        
    
    
    
    



