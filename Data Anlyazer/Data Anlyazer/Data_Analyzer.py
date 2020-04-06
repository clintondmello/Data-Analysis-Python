import matplotlib.pyplot as plt
from matplotlib import interactive
import numpy as np
import pandas as pd

gasdata = pd.read_csv('./Data/gas_prices.csv')
selectiveData = plt.figure(0) 
plt.figure(figsize=(8,5))
plt.xticks(gasdata.Year[::2])
plt.xlabel('Year')
plt.ylabel('US Dollars')
plt.title('Gas Prices Range (in USD)')
plt.plot(gasdata['Year'], gasdata['USA'],'r.',label='United States of America')
plt.plot(gasdata['Year'],gasdata['Mexico'],'g.-', label='Mexico')
plt.plot(gasdata['Year'],gasdata['South Korea'],'y.--', label='South Korea')
plt.plot(gasdata['Year'],gasdata['Germany'],'b.-', label='Germany')
plt.legend()

automappedData  = plt.figure(1)
plt.figure(figsize=(8,5))
plt.xticks(gasdata.Year[::2])
plt.xlabel('Year')
plt.ylabel('US Dollars')
plt.title('Gas Prices Range (in USD)')
for country in gasdata:
    if country != 'Year':
        plt.plot(gasdata.Year,gasdata[country],label=country)
plt.legend()
plt.show()




