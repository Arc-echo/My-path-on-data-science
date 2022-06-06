# 2015 Flight Delays and Cancellations

Using the data sets download from Kaggle: https://www.kaggle.com/datasets/usdot/flight-delays, exploring the distribution of operated and delayed flights.

## Average Departure Delay Of Each Airline Per Airport

By grouping and calculating the delayed rate and operated rate, we can find out which airport and airline has the higher delayed rate.

Also with comparing the data by pairplot, the distribution for above two elements is obviously shown.

### Rate Per Session For Operated Flights Only

Seperate the departure time into different sessions to see the rate of departure sessions by different airports.
The dataframe has been reshaped into a pivot table for easier to read.
