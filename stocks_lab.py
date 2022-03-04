#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:07:30 2022

@author: jesslaudie
"""

import sys
import json
import requests

url = "https://yfapi.net/v6/finance/quote"

stocks = sys.argv[1]

querystring = {"symbols": sys.argv[1]}

headers = {
    'x-api-key': "V8fCXjcbiG1MgpLB48Hlw4SOCvwaNIJb3X7zudpK"}

response = requests.request("GET", url, headers = headers, params = querystring)

data = json.loads(response.text)

try:
    stockName = data['quoteResponse']['result'][0]["longName"]
    price = data['quoteResponse']['result'][0]["regularMarketPrice"]
    print(stockName, ":", price)
except IndexError:
    print("Error: Stock Not Found")
    
    
