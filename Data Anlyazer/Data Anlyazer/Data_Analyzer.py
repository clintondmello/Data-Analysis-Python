import matplotlib.pyplot as plt
from matplotlib import interactive
import numpy as np
import pandas as pd

gasdata = pd.read_csv('./Data/gas_prices.csv')
selectiveData = plt.figure(0) 
plt.figure(figsize=(8,5))
plt.xticks(gasdata.Year[::2].tolist())
plt.xlabel('Year')
plt.ylabel('US Dollars')
plt.title('Gas Prices Range (in USD)',fontdict ={'fontweight':'bold'})
plt.plot(gasdata['Year'], gasdata['USA'],'r.',label='United States of America')
plt.plot(gasdata['Year'],gasdata['Mexico'],'g.-', label='Mexico')
plt.plot(gasdata['Year'],gasdata['South Korea'],'y.--', label='South Korea')
plt.plot(gasdata['Year'],gasdata['Germany'],'b.-', label='Germany')
plt.legend()
plt.savefig('Gas Prices Over Time(USA,Mexico,South Korea, Germany).png',dpi=300)

automappedData = plt.figure(1)
plt.figure(figsize=(8,5))
plt.xticks(gasdata.Year[::2].tolist())
plt.xlabel('Year')
plt.ylabel('US Dollars')
plt.title('Gas Prices Range (in USD)',fontdict ={'fontweight':'bold'})
for country in gasdata:
    if country != 'Year':
        plt.plot(gasdata.Year,gasdata[country],label=country)
plt.legend()
plt.savefig('Gas Prices Over Time.png',dpi=300)

fifaPlayerSkillStats = plt.figure(3)
fifaData = pd.read_csv('./Data/fifa_data.csv')
bins = [40,50,60,70,80,90,100]
plt.hist(fifaData.Overall,bins=bins)
plt.xticks(bins)
plt.xlabel('Skill Level')
plt.ylabel('No. of Players')
plt.title('Player Stats FIFA')
plt.savefig('FIFA Players Skill Stats.png',dpi=300)

fifaPlayerPreferredFootStats = plt.figure(4)
leftPreferredFootPlayers = fifaData.loc[fifaData['Preferred Foot'] == 'Left'].count()[0]
rightPreferredFootPlayers = fifaData.loc[fifaData['Preferred Foot'] == 'Right'].count()[0]
labels = ['Left Foot','Right Foot']
plt.pie([leftPreferredFootPlayers,rightPreferredFootPlayers],labels =labels,autopct = '%.2f %%')
plt.title('Players Foot Preference')
plt.savefig('FIFA Players Foot Preferences.png',dpi=300)

fifaPlayerWeightCategories = plt.figure(5)
plt.style.use('ggplot')
fifaData.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifaData.Weight]
lightCategoryPlayers = fifaData.loc[fifaData.Weight < 125].count()[0]
mediumLightCategoryPlayers = fifaData.loc[(fifaData.Weight >= 125) & (fifaData.Weight < 150)].count()[0]
mediumCategoryPlayers = fifaData.loc[(fifaData.Weight >= 150) & (fifaData.Weight < 175)].count()[0]
mediumHeavyCategoryPlayers = fifaData.loc[(fifaData.Weight >= 175) & (fifaData.Weight < 200)].count()[0]
heavyCategoryPlayers = fifaData.loc[(fifaData.Weight >= 200)].count()[0]
weightCategories = [lightCategoryPlayers,mediumLightCategoryPlayers,mediumCategoryPlayers,mediumHeavyCategoryPlayers,heavyCategoryPlayers]
labels = ['Under 125 lbs','125-150 lbs','150-175 lbs','175-200 lbs','Over 200 lbs']
explode = [.1,.1,.1,.1,.1]
plt.pie(weightCategories,labels=labels,autopct = '%.2f %%',pctdistance = 0.8,explode = explode)
plt.title('Players Weight Distributions')
plt.savefig('FIFA Players Weight Distributions.png',dpi=300)

fifaClubsPerformanceStats = plt.figure(6)
plt.style.use('default')
barcelonaStats = fifaData.loc[fifaData.Club == 'FC Barcelona']['Overall'] 
realMadridStats = fifaData.loc[fifaData.Club == 'Real Madrid']['Overall'] 
nerStats = fifaData.loc[fifaData.Club == 'New England Revolution']['Overall'] 
labels = ['FC Barcelona','Real Madrid','NE Revolution']
boxes = plt.boxplot([barcelonaStats,realMadridStats,nerStats],labels=labels,patch_artist =True)
for  box in boxes['boxes']:
    box.set(color='#4286f4',linewidth=2)
    box.set(facecolor='#e0e0e0')
plt.title('FIFA Team Stats')
plt.ylabel('FIFA Overall Rating')
plt.savefig('FIFA Overall Club Ratings.png',dpi=300)
plt.show()




