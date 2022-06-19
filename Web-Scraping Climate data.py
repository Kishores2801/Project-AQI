# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 12:14:44 2022

@author: Kishore
"""


# importing packages for scraping
import os # operating system
import time # to check time taken for scraping
import requests # this package will help us to download the html files
from datetime import date
import sys

# to change to different cities we can update ws-434660 to value you get for that specific city in the url
# the link used here
current_year = date.today().year+1

def retrieve_html():
    # loops for years
    for year in range(2013,2022):
        # loops for month
        for month in range(1,13):
            # 
            if (month<10):
                url="https://en.tutiempo.net/climate/0{}-{}/ws-434660.html".format(month,year)
            else:
                url="https://en.tutiempo.net/climate/{}-{}/ws-434660.html".format(month,year)
        
        
        
            # this will help us to get all values
            texts=requests.get(url)
            # encoding the html text with utf=8
            text_utf=texts.text.encode("utf=8")
            
            
            
            # check whether the path exist or not if not create one 
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
                
                
            # write the Html in each folder
            with open("Data/Html_Data/{}/{}.html".format(year,month), "wb") as output: # "write byte"
                       output.write(text_utf)
     
    
        sys.stdout.flush()

# time taken
if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print ("Time Taken - {}".format(stop_time-start_time))
    
    
    