### 1. Data frame
import numpy as npy
import pandas as pd
from pandas import Series, DataFrame

# Create a data frame using data on a website
import webbrowser
website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
webbrowser.open(website)
nfl_frame = pd.read_clipboard()
nfl_frame

# Explore the data frame
nfl_frame.columns
nfl_frame.Team
nfl_frame['First NFL Season']
DataFrame(nfl_frame,columns=['Team','First NFL Season','Total Games','Stadium'])
nfl_frame.head(3)
nfl_frame.ix[3]

# Add new columns to an existing data frame
nfl_frame['Stadium'] = np.arrange(5)
stadiums = Series(["Levi's Stadium","AT&T Stadium"],index=[4,0])
nfl_frame['Stadium']=stadiums
del nfl_frame['Stadium']

# Create data frames from dictionaries
data = {'City':['SF','LA','NYC'],'Population':[837000,388000,840000]}
city_frame = DataFrame(data)

# Reindex
from numpy.random import randn
ser1 = Series([1,2,3,4],index=['A','B','C','D'])
my_index = ser1.index
ser2 = ser1.reindex(['A','B','C','D','E','F'])
ser2.reindex(['A','B','C','D','E','F','G'],fill_value=0)
ser3 = Series(['USA','Mexico','Canada'],index=[0,5,10])
ser3.reindex(range(15),method='ffill')
dframe = DataFrame(randn(25).reshape((5,5)),index=['A','B','D','E','F'],columns=['col1','col2','col3','col4','col5'])
new_columns = ['col1','col2','col3','col4','col5','col6']
dframe2 = dframe.reindex(['A','B','C','D','E','F']) #### This line and the line below are equivalent to the last line
dframe2.reindex(columns = new_columns) ####
dframe.ix[['A','B','C','D','E','F'],new_columns]
