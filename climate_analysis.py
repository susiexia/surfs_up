# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
get_ipython().magic('matplotlib inline')
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


# %%
import numpy as np
import pandas as pd


# %%
import datetime as dt

# %% [markdown]
# # Reflect Tables into SQLAlchemy ORM

# %%
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# %%
engine = create_engine('sqlite:///hawaii.sqlite')

# %%
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect = True)

# %%
# We can view all of the classes that automap found
Base.classes.keys()

# %%
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# %%
# Create our session (link) from Python to the DB
session = Session(engine)

# %% [markdown]
# # Exploratory Climate Analysis

# %%
# Design a query to retrieve the last 12 months of precipitation data and plot the results. 
#Starting from the last data point in the database. 

# Calculate the date (a date point) one year from the last date in data set.
perv_year = dt.date(2017,8,23) - dt.timedelta(days=365)

# Perform a query to retrieve the data and precipitation scores
results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= perv_year)
print(results.all())


# Save the query results as a Pandas DataFrame and set the index to the date column
df = pd.DataFrame(results, columns=['date', 'precipitation'])
df.set_index(df['date'], inplace= True)
print(df.to_string(index= False))

# Sort the dataframe by date
df = df.sort_index()
print(df.to_string(index=False))
# %%
# Use Pandas Plotting with Matplotlib to plot the data
df.plot()

# %%
# Use Pandas to calcualte the summary statistics for the precipitation data
df.describe()
# %%
# How many stations are available in this dataset?


# %%
# What are the most active stations?
# List the stations and the counts in descending order.


# %%
# Using the station id from the previous query, calculate the lowest temperature recorded, 
# highest temperature recorded, and average temperature most active station?


# %%
# Choose the station with the highest number of temperature observations.
# Query the last 12 months of temperature observation data for this station and plot the results as a histogram


# %%
# Write a function called `calc_temps` that will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates

# %% [markdown]
# # Challenge

# %%



