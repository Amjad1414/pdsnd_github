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
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data! ')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input('Would you like to see data for (chicago, new york city, or washington)? \n')
    city=city.lower()
    while city not in ['chicago','new york city','washington']:
        print('Please make sure you enter the correct city !')
        city= input('Would you like to see data for (chicago, new york city, or washington)? \n')
        city=city.lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month= input('Which month you like to filter the data with (all, january, february, ..., june)? \n')
    month=month.lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may','june']:
        print('Please make sure you enter the correct month !')
        month= input('Which month you like to filter the data with (all, january, february, ...,june)? \n')
        month=month.lower()
    # TO DO: get user input for day (all, monday, tuesday, ... , sunday)
    day=input('Which day do you like to filter the data with (all,monday, tuesday, ... ,sunday)? \n')
    day=day.lower()
    while day not in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print('Please make sure you enter the correct day !')
        day=input('Which day do you like to filter the data with (all,monday, tuesday, ... ,sunday)? \n')
        day=day.lower()
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
    df= pd.read_csv(CITY_DATA[city]) #load city.csv file
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    #filter by month if applicable
    if month != 'all':
        months=['january', 'february', 'march', 'april', 'may','june']
        month = (months.index(month))+1
        # filter by month to create the dataframe
        df = df.loc[month==df['month']]
    #filter by day if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    count_of_month=df['month'].value_counts()
    common_month=max(count_of_month)
    print('The most common month is: {}, count: {}'.format(count_of_month.loc[count_of_month==common_month].index[0],common_month))
    # TO DO: display the most common day of week
    count_of_day=df['day_of_week'].value_counts()
    common_day=max(count_of_day)
    print('The most common day is: {}, count: {}'.format(count_of_day.loc[count_of_day==common_day].index[0],common_day))
    ## TO DO: display the most common start hour
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['hour']= df['Start Time'].dt.hour
    count_of_hour=df['hour'].value_counts()
    common_hour=max(count_of_hour)
    print('The most common hour is: {}, count: {}'.format(count_of_hour.loc[count_of_hour==common_hour].index[0],common_hour))
    #-----------------------------------------------------
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    count_of_start=df['Start Station'].value_counts()
    max_start=max(count_of_start)
    print('The most popular start station is: {}, count: {}'.format(count_of_start.loc[count_of_start==max_start].index[0],max_start))
    # TO DO: display most commonly used end station
    count_of_end=df['End Station'].value_counts()
    max_count_of_end=max(count_of_end)
    print('The most popular end station is: {}, count: {}'.format(count_of_end.loc[count_of_end==max_count_of_end].index[0],max_count_of_end))
    # TO DO: display most frequent combination of start station and end station trip
    trip_combine_path= df['Start Station']+","+df['End Station']
    count_of_station=trip_combine_path.value_counts()
    popular_station=max(count_of_station)
    print('Trip:({}), count:{}'.format(count_of_station.loc[count_of_station==popular_station].index[0],popular_station))
    #-------------------------------------------------------------
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    trip_duration=np.array(df['Trip Duration'])
    # TO DO: display total travel time
    count_of_trips=np.count_nonzero(trip_duration,axis=0)
    total_duration=trip_duration.sum()
    print('Total Duration:{} ,count:{} '.format(total_duration,count_of_trips))
    # TO DO: display mean travel time
    avg_duration= trip_duration.mean()
    print('Avg Duration: {}'.format(avg_duration))
    #-----------------------------------------------------
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_users=df['User Type'].value_counts()
    print(count_of_users)
    # TO DO: Display counts of gender
    if city != 'washington':
        count_of_gender=df['Gender'].value_counts()
        print(count_of_gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest_birth=df['Birth Year'].min()
        most_recent_birth=df['Birth Year'].iloc[-1]
        count_of_year=df['Birth Year'].value_counts()
        most_commomn_year=count_of_year.max()
        print('Earliest birth year:{} '.format(earliest_birth))
        print('Most recent birth year:{} '.format(most_recent_birth))
        print('Most common birth year:{}'.format(count_of_year.loc[count_of_year==most_commomn_year].index[0]))
        #-------------------------------------------------------------

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw(df):
    """
    Ask the user if he wants to display the data of the bike-share system
    Returns:
        (5) rows of the database each time
    """
    answer=input("Would you like to see the data of bike-share system? Type 'yes' or 'no'\n")
    answer=answer.lower()
    while answer not in ['yes','no']:
        print("Please make sure you enter 'yes' or 'no'")
        answer=input("Would you like to see the data of bike-share system? Type 'yes' or 'no'\n")
        answer=answer.lower()
    counter=0
    while answer=='yes':
        counter+=5
        for i in range(counter):
            row=df.iloc[i]
            print(row)
        answer=input("Would you like to view individual trip data? Type 'yes' or 'no'\n")
        answer=answer.lower()
        while answer not in ['yes','no']:
            print("Please make sure you enter 'yes' or 'no'")
            answer=input("Would you like to view individual trip data? Type 'yes' or 'no'\n")
            answer=answer.lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        restart=restart.lower()
        while restart not in ['yes','no']:
            print("Please make sure you enter 'yes' or 'no' ")
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            restart=restart.lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
    main()
