import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york', 'washington']
choices = ['month', 'day', 'both', 'non']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

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


    print('-'*100)
    return city, month, day

def getMonth():
    month = input('Which month? January, February, March, April, May or June? \n').lower()
    while not month in months:
        month = input('Invalid month ... Please select a valid month\n').lower()
    return month

def getDay():
    day = input('Which day? Sunday, Monday, Tuesday, Wednesday or Thursday? \n').lower()
    while not day in days:
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

    ## read the file of the selected city
    df = pd.read_csv(CITY_DATA[city])

    # convert the start time column into datatime type
    df['Start Time']= pd.to_datetime(df['Start Time'])

    # make new columns of month and day from the start time column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month)
        df = df[df['month'] == month]
    
    if day != 'all':
        # filter by day of week to create the new dataframe
        day = days.index(day) - 1
        df = df[df['day_of_week'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is', months[most_common_month])

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day is', days[most_common_day +1])


    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is', most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station is', most_common_end_station)

    # display most frequent combination of start station and end station trip
    df["common ste"] = '(' + df['Start Station'] + ') to (' +  df['End Station'] + ')'
    most_common_ste_combination = df["common ste"].mode()[0]
    print('The most frequent combination of start station and end station trip is', most_common_ste_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].count()
    print('Total travel time is', total_travel_time)

    # display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average travel time is', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Subscribers:', user_types[0],
        '\nCustomers:', user_types[1])

    # Display counts of gender
    user_gender = df['Gender'].value_counts()
    print('Males:', user_gender[0],
        '\nFemales:', user_gender[1])


    # Display earliest, most recent, and most common year of birth
    most_common_yob = df['Birth Year'].mode()[0]
    most_recent_yob = df['Birth Year'].max()
    earliest_yob = df['Birth Year'].min()

    print('earliest birth year {} \nmost recent birth year {} \nmost common birth year {}'.format(earliest_yob,most_recent_yob,most_common_yob))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
