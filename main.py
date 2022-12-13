import random

# lists

destination_list = ['art museum', 'park', 'beach', 'mountains', 'history museum']

restaurant_list = ['Italian', 'Mexican', 'German', 'American', 'Asian Fusian', 'Chinese', 'Thai', 'Korean', 'Indian']

transportation_list = ['bus', 'car', 'plane', 'train', 'bike', 'foot']

entertainment_list = ['live theater', 'a movie', 'a famous street performer', 'a musical', 'mountain climbing', 'sky diving', 'snowboarding', 'yoga', 'a boxing match', 'a football game', 'a baseball game']

#functions

def random_destination_generator ():
    destination= random.choice (destination_list)
    print (f"Your destination for your day trip is {destination}")

def random_restaurant_generator ():
    restaurant= random.choice (restaurant_list)
    print (f"you will be dining on some delicious {restaurant} food")

def random_transportation_generator ():
    transportation= random.choice (transportation_list)
    print (f"You will be arriving by {transportation} ")

def random_entertainment_generator ():
    entertainment= random.choice (entertainment_list)
    print (f"While there, you will be enjoying {entertainment}")


def random_trip_generator ():
    random_destination_generator ()
    random_restaurant_generator ()
    random_transportation_generator ()
    random_entertainment_generator ()

random_trip_generator ()


def confirm_your_trip ():
    user_confirm = input("Are you happy with your trip arriving by {transportation} to {destination}, feasting on {restaurant} food, and enjoying {entertainment}?/n Yes or no? ")
    while user_confirm == "no":
        confirm_destination = ("Are you happy with your destination? yes or no?")
        if confirm_destination == "yes":
            continue
        elif confirm_destination == "no":
            def random_destination_generator ():
                confirm_destination = input ("How about we go to {destination} instead? yes or no? ")
        else:
            print ("That is an invalid response")
            confirm_your_trip ()



