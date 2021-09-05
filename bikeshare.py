import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the dayimport time
 of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = ''
    while cities not in CITY_DATA.keys():  
        cities = input('\nPlease select which city you want to looking for:\nAvilabe cyties (chicago,  new york city, washington)\n').lower()
        if cities.lower() in CITY_DATA:
           city = CITY_DATA[cities.lower()]
        else:
            print('unkown city, please rewrite again')
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month_data = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    months = ''
    while months not in month_data:
        months = input('\nGet it, Now select the month want to search:\n    january, february, march, april, may, june\nYou can select all months by typing "all"\n').lower()
        if months in month_data:
            month = months.lower()
        else:
            print ('Unkkown month..Please check\nAvilabe months betwen junuary to june\n')
  
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_data = [ 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','sunday', 'all']
    days = ''
    while days not in day_data:
        days = input('\nFine, Which day you want to search:\n monday, tuesday, wednesday, thursday, friday, saturday,sunday \nYou can select all days by typing "all"\n').lower()
        if days in day_data:
            day = days.lower()
        else:
            print ('Unkkown day..Please check')
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
    #load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month is: {}'.format(popular_month))
          
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print('Most common day is: {}'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour is: {}'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Common start station is: \n{}\n'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Common end station is: \n{}\n'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to \n')
    combo = df['Start To End'].mode()[0]
    print('The most frequent combination of start station and end station trip is:\n {}\n'.format(combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: {}'.format(total_travel_time)+ ' seconds')
           
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: {}'.format(total_travel_time)+ ' seconds')    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Counts of user types : \n{}\n'.format(user_type))
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('Counts of gender : \n{}\n'.format(gender_counts))
    else:
        print('Sorry: Gender is not included in this city...')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = int(df['Birth Year'].min())
        print('Earliest birth year is: {}'.format(earliest_year))
        recent_year = int(df['Birth Year'].max())
        print('Most recent birth year is: {}'.format(recent_year))
        common_year = int(df['Birth Year'].mode()[0])
        print('Most common birth year is: {}'.format(common_year))
    else:
        print('Sorry: Birth year is not included in this city...')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        if view_data not in ['yes', 'no']:
             view_data = input ('Unkown answer, If you want to display another 5 rows enter "yes"\n If you want to cancle enter "no"').lower()
        elif view_data =='yes':
            start_loc += 5 
            print(df.iloc[start_loc:start_loc + 5]) 
            view_display = input('Do you wish to continue?:').lower()
        if view_display == 'no':
            break
        elif view_data == 'no':
            return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
