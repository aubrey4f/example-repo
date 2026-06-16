# dictionary to define the cities and flight costs
city_flight_cost = {
    'Cape Town' : 1300,
    'Pretoria' : 1200,
    'Joburg' : 1000
}

# variables for hotel and rental per day costs
hotel_cost_per_day = 600
rental_cost_per_day = 300

def choose_city():
    '''
    Asks the user to choose a city until they choose one in the dictionary

    Returns:
    string: The chosen city
    '''
    while True:
        choice = input('Where are you going? (Cape Town, Pretoria, or Joburg) ')
        if choice in city_flight_cost:
            break

        print(f'{choice} is not a valid option')
    return choice

def get_whole_number(message):
    '''
    Asks the user to enter a whole number until they input a valid whole number

    Parameters:
    message(str): The prompt to be shown to the user

    Returns:
    int: A valid whole number entered by user
    '''
    while True:
        number = input(message)
        if number.isdigit():
            break
        
        print(f'{number} is not a whole number')
    return int(number)

# functions for calculating total hotel, plane, rental, and holiday costs
def hotel_cost(days):
    return days*hotel_cost_per_day

def plane_cost(city):
    return city_flight_cost[city]

def car_rental(days):
    return days*rental_cost_per_day

def holiday_cost(city_flight,num_nights,rental_days):
    total_cost = hotel_cost(num_nights)+plane_cost(city_flight)+car_rental(rental_days)
    return total_cost

# get the user inputs
city_flight = choose_city()
num_nights = get_whole_number('How many nights will you be staying? ')
rental_days = get_whole_number('How many days will you be renting a car? ')

# print the costs
print(f'Flight Cost: {plane_cost(city_flight)}')
print(f'Hotel Cost: {hotel_cost(num_nights)}')
print(f'Rental Cost: {car_rental(rental_days)}')
print(f'Total Cost: {holiday_cost(city_flight,num_nights,rental_days)}')