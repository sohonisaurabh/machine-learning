# Bike-share data analysis

This folder contains Python code for implementation of bike share data analysis project.


## Background

First step of every task involving data analysis and inference generation involves careful observation of data. In this step, all data fields or columns are viewed and valuable information pertaining to the task is filtered. Data contained in these columns is then studied using descriptive statistical methods before proceeding to developing machine learning (ML) models for solving the task.

Filtered data required in the step above can be obtained using data wrangling. Few data elements may not required in arriving at the inference are removed and the data is cleaned for garbage values like NANs, empty fields, etc.

Data wrangling was not in scope of this project, the data used was already cleaned.
  

## Problem Statement

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

For this project, use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. Compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

## Project Goal

The goal of this project was to write a python script to interact with user through command prompt and provide answers to the following questions:

1. What is the most popular month for riding a bicycle?
2. What is the most popular day of week (Monday, Tuesday, etc.) for riding a bicycle?
3. What is the most popular hour of day when people ride bicycle?
4. What is the total trip duration and average trip duration of bicycle rides?
5. What is the most popular start station and most popular end station for bicycle rides?
6. What is the most popular trip?
7. What are the counts of each user type? Data contained two types of users viz. Subscribers and Customers
8. What are the counts of gender? This data was only available for Chicago and New York City
9. What is the age of oldest person who rode a bicycle?
10. What is the age of youngest person who rode a bicycle?
11. Riding a bicycle is most common for what age?

These questions had to be answered for one city at a time. Also, the user had an option to filter the data based on month and days of week before getting answers to the above questions.

## Dataset

The data set contained three .csv files, for New York City, Chicago and Washington respectively. Following is a summary of various columns in the provided data set:

All three of the data files contain the same core six (6) columns:
Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
Gender
Birth Year


## Project Implementation

Python 3.7.0 was used to write an interactive script. The script had following methods:

1. load_data() - Loads the for a particular city and filters it by month or day of week if specified by user
2. time_stats() - Makes use of trip time stats like start time, end time and trip duration to provide information on most popular month, day and hour
3. station_stats() - Makes use of start station and end station to provide information on most popular places to ride a bicycle
4. trip_duration_stats() - Makes use of trip duration to calculate total trip duration and average trip duration
5. user_stats() - Makes use of user type and gender data to provide information on age of riders and total male/female riders


## Steps for running the project

### Dependencies

This project requires **Python** and the following Python libraries installed:

- [Pandas](http://pandas.pydata.org/)

### Run command

python bikeshare_2.py

### Sample Output

Screenshot of sample script output for Chicago, with filter on January and all days of week is shown below:

![Sample output](https://raw.githubusercontent.com/sohonisaurabh/machine-learning/master/projects/bike_share_data_analysis/project-submission/sample-output.png)

## References:

Pandas documentation for data frame and data series was referred extensively. One can find links below:

[Pandas Dataframe 0.23.4](http://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.html)

[Pandas Dataseries 0.23.4](https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.Series.html)
  
