from secrets import choice
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = {'chicago', 'new york', 'washington'}
choices = {'month', 'day', 'both', 'non'}
months = {'all', 'january', 'february', 'march', 'april', 'may', 'june'}
days = {'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('Which city would you like to see data for? Chicago, New York or Washington? \n').lower()
    while not city in cities:
        city = input('Invalid city ... Please select a city from the listed ones \n').lower()

    choice = input('Would you like to sort the data by month, day, both or non? type non for no filters \n').lower()
    while not choice in choices:
        choice = input('Invalid choice ... Please select a choice from the listed ones \n').lower()

    if choice == 'month':
    # get user input for month (all, january, february, ... , june)
        month =  getMonth()
        day = 'all'

    elif choice == 'day':
        month = 'all'
        day = getDay()

    elif choice == 'both':
        month =  getMonth()
        day = getDay()
    else:
        month = 'all'
        day = 'all'


    print(city, month, day)

    print('-'*40)
    return city, month, day


def getMonth():
    month = input('Which month? January, February, March, April, May or June? \n').lower()
    while not month in months:
        month = input('Invalid month ... Please select a valid month\n').lower()
    return month



def getDay():
    day = input('Which day? Sunday, Monday, Tuesday, Wednesday or Thursday? \n').lower()
    while not day in day:
        day = input('Invalid day ... Please select a valid day \n').lower()
    return day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    # while True:
    #     city, month, day = get_filters()
    #     df = load_data(city, month, day)

    #     time_stats(df)
    #     station_stats(df)
    #     trip_duration_stats(df)
    #     user_stats(df)

    #     restart = input('\nWould you like to restart? Enter yes or no.\n')
    #     if restart.lower() != 'yes':
    #         break

    get_filters()


if __name__ == "__main__":
	main()
