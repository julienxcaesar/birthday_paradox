import datetime, random

def get_birthdays(num_birthdays):
    #returns a list of number random dat objects for birthdays
    birthdays = []
    for i in range (num_birthdays):
        #the year is unimportant for the simulation, as long as all the 
        #birthdays have the same year
        start_of_year = datetime.date(2000, 1, 1)

        #get a random day into the year:
        random_num_of_day = datetime.timedelta(random.randint(0, 364)) #change to 365
        birthday = start_of_year + random_num_of_day
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    #return the date object of a bithday that occurs more than once in birthdays list
    if len(birthdays) == len(set(birthdays)):
        return None     #all birthdays are unique, so return None
    
    #compare each birthday to every other birthday:
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1 :]):
            if birthday_a == birthday_b:
                return birthday_a   #return the matching birthday

#Display the intro:
print('''The birthday paradox shows us that in a group of "N" people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random simulation)
to explore this concept. (It's not actually a paradox, its just a surprising result)''')

#set up a tuple of month names in order:
months = ('Jan', 'Feb', 'Mar', 'Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  #keep asking until the user enters a valid amount
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break #user has entered the valid amount
print()

#generate and displays birthdays:
print('Here are', num_bdays, 'birthdays:')
birthdays = get_birthdays(num_bdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #display a comma for each birthday after the first birthday
        print(', ', end='')
    month_name = months[birthday.month - 1]
    date_text = f'{month_name} {birthday.day}'
    print(date_text, end='')
print()
print()

#determine if there are two birthdays that match
match = get_match(birthdays)

#display the results:
print('In this simulation, ', end='')
if match != None:
    month_name = months[match.month - 1]
    date_text = f'{month_name} {match.day}'
    print(f'multiple people have a birthday on {date_text}')
else:
    print('there are no matching birthdays')
print()

# run through 100,000 simulations:
print(f'Generating {num_bdays} random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Lets\'s run another 100,000 simulatiions')
sim_match = 0 # how many simulations had matching birthdays in them
for i in range(100000):
    # report on the progress every 10,000 simulations:
    if i % 10000 == 0:
        print(i, 'simulations run...')
    birthdays = get_birthdays(num_bdays)
    if get_match(birthdays) != None:
        sim_match = sim_match + 1
print('100,000 simulations run')

#display simulation results:
probability = round(sim_match / 100000 * 100, 2)
print(f'''Out of 100,000 simulations of {num_bdays} people there was 
a matching birthday in that group {sim_match} times. This means
that {num_bdays} people have a {probability}% chance of having
a matching birthday in their group. That's probably more than 
you would think!''')

