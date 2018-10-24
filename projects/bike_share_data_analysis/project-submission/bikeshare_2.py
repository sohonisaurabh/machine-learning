import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ["chicago", "new york city", "washington"]
months = ["jan", "feb", "mar", "apr", "may", "jun"]
days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
monthsDisplayMap = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June"
}
daysDisplayMap = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday",
    "sat": "Saturday",
    "sun": "Sunday"
}



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
    while(1):
        city = input("Which city from Chicago, New york city and Washington you want to explore?: ")
        city = city.lower().strip()
        print(city)
        if (city in cities):
            break;
        else:
            print("Oops! That is not a valid city. Please try again.")
    
    # get user input for month (all, january, february, ... , june)
    while(1):
        month = input("Apply filter for month? Enter one from Jan, Feb, Mar, Apr, May, Jun or all for no filter: ")
        month = month.lower().strip()
        if (month in (months + ["all"])):
            break;
        else:
            print("Oops! That is not a valid month. Please try again.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while(1):
        day = input("Apply filter for day? Enter one from Sun, Mon, Tue, Wed, Thu, Fri, Sat or all for no filter: ")
        day = day.lower().strip()
        if (day in (days + ["all"])):
            break;
        else:
            print("Oops! That is not a valid day. Please try again.")


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

    #1 - Load data frame
    df = pd.read_csv(CITY_DATA[city])

    showBrief = input("\nDo you want to view few lines of raw data? Enter yes or no: ")
    if(showBrief == "yes"):
        print(df.head())

    #2 - Convert start time and end time to pandas date_time
    df["Start Time"] = pd.to_datetime(df['Start Time'])
    df["End Time"] = pd.to_datetime(df["End Time"])

    #3 - Extract months and days
    df["Month"] = df["Start Time"].dt.month
    df["Day"] = df["Start Time"].dt.day

    #4 - Apply month filter

    if (month != None and month != "all"):
        monthIndex = months.index(month) + 1
        df = df[df["Month"] == monthIndex]

    #5 - Apply day filter

    if (day != None and day != "all"):
        dayIndex = days.index(day) + 1
        df = df[df["Day"] == dayIndex]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month_Idx = df["Month"].mode()[0]
    print("\nMost common month is: ", monthsDisplayMap[months[most_common_month_Idx - 1]])


    # display the most common day of week
    most_common_day_Idx = df["Start Time"].dt.dayofweek.mode()[0]
    print("\nMost common day of week is: ", daysDisplayMap[days[most_common_day_Idx]])


    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    print("\nMost common hour of day is: ", df["hour"].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("\nMost commonly used start station is: ", df["Start Station"].mode()[0])

    # display most commonly used end station
    print("\nMost commonly used end station is: ", df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    df["trip"] = df["Start Station"].combine(df["End Station"], lambda x1, x2: x1 + " -- to --> " + x2)
    print("\nMost frequent combination of start and end trip is: ", df["trip"].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df["Trip Duration"].sum()
    min, sec = divmod(total_duration, 60);
    hour, min = divmod(min, 60);
    print('\nTotal travel time is: {} hours, {} minutes and {} seconds.'.format(int(hour), int(min), int(sec)))

    # display mean travel time
    avg_duration = df["Trip Duration"].mean()
    min, sec = divmod(avg_duration, 60);
    hour, min = divmod(min, 60);
    print('\nAverage travel time is: {} hours, {} minutes and {} seconds.'.format(int(hour), int(min), int(sec)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("\nCounts of user types are given below: ")
    print(df["User Type"].value_counts())


    # Display counts of gender
    if ("Gender" in df):
        print(df["Gender"].value_counts())
    else:
        print("Gender count data is not available for this city.")


    # Display earliest, most recent, and most common year of birth
    if ("Birth Year" in df):
        print("Earliest birth year is: ", int(df["Birth Year"].min()))
        print("Most Recent birth year is: ", int(df["Birth Year"].max()))
        print("Most common birth year is: ", int(df["Birth Year"].mode()[0]))
    else:
        print("Birth year data is not available for this city.")


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
