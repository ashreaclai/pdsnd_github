import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = [ 'january', 'feburary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

days = [ 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("Please input city name: ").lower()
    
    while city not in ['chicago', 'new york city', 'washington']:
    
        city = input (
        "City if name is invalid! Please input another name: ").lower()
       

    # TO DO: get user input for month (all, january, february, ... , june)

    month = input("Please input month name: ").lower()
 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input("Please input day of week: ").lower()

    print('-'*40)
    return city, month, day



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
   
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: {}".format(
        str(df['month'].mode().values[0]))
         )

    # TO DO: display the most common day of week
    print("The most common day of the week: {}".format(
        str(df['day_of_week'].mode().values[0]))
         )

    # TO DO: display the most common start hour
    print("The most common start hour: {}".format(
        str(df['start_hour'].mode().values[0]))
         )

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    
    # TO DO: display most commonly used start station
    print("The most common start station is: {}".format(
        df['Start Station'].mode().values[0])
    )

    # TO DO: display most commonly used end station
    print("The most common end station is: {}".format(
        df['End Station'].mode().values[0])
    )

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station']+ " " + df['End Station']
    print("The most common start and end station combo is: {}".format(
        df['routes'].mode().values[0])
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['duration'] = df['End Time'] - df['Start Time']
          
    # TO DO: display total travel time
    print("The total travel time is: {}".format(
        str(df['duration'].sum()))
         )

    # TO DO: display mean travel time
    print("the mean travel time is: {}".format(
        str(df['duration'].mean()))
         )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Here are the counts of various user types:")
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    print("Here are the counts of gender:")
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print("The earliest birth year is: {}".format(
        str(int(df['Birth Year'].min())))
    )
    print("The latest birth year is: {}".format(
        str(int(df['Birth Year'].max())))
    )
    print("The most common birth year is: {}".format(
        str(int(df['Birth Year'].mode().values[0])))
    )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
