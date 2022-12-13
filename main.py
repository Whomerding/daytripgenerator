import random

# lists

destination_list = ['art museum', 'park', 'beach', 'mountains', 'history museum']

restaurant_list = ['Italian', 'Mexican', 'German', 'American', 'Asian Fusian', 'Chinese', 'Thai', 'Korean', 'Indian']

transportation_list = ['bus', 'car', 'plane', 'train', 'bike', 'foot']

entertainment_list = ['live theater', 'a movie', 'a famous street performer', 'a musical', 'mountain climbing', 'sky diving', 'snowboarding', 'yoga', 'a boxing match', 'a football game', 'a baseball game']

#functions

def random_destination_generator ():
    destination = random.choice (destination_list) 
    print (f"Your destination for your day trip is {destination}")
    return (destination)

def random_restaurant_generator ():
    restaurant = random.choice (restaurant_list)
    print (f"you will be dining on some delicious {restaurant} food")
    return (restaurant)

def random_transportation_generator ():
    transportation = random.choice (transportation_list)
    print (f"You will be arriving by {transportation} ")
    return (transportation)

def random_entertainment_generator ():
    entertainment = random.choice (entertainment_list)
    print (f"While there, you will be enjoying {entertainment}")
    return (entertainment)

    
def confirm_your_trip ():
    destination = random_destination_generator ()
    restaurant = random_restaurant_generator ()
    transportation = random_transportation_generator ()
    entertainment = random_entertainment_generator ()
    user_confirm = input("Are you happy with your trip? yes or no?")

    if user_confirm == "no":
            
        confirm_destination = input ("Are you happy with your destination? yes or no?")    

        while confirm_destination == "no":
            destination = random_destination_generator ()
            confirm_destination = input ("Are you happy with your destination now? yes or no?")
        
        confirm_restaurant = input ("Are you happy with your restaurant selection?yes or no?")
        while confirm_restaurant == "no":
            restaurant = random_restaurant_generator ()
            confirm_restaurant = input ("Are you happy with your restaurant selection now?yes or no?")

        confirm_transport = input ("Are you happy with your transportation selection?yes or no?")
        while confirm_transport == "no":
            transportation = random_transportation_generator ()
            confirm_transport = input ("Are you happy with your transportation selection now?yes or no?")

        confirm_entertainment = input ("Are you happy with your entertainment selection?yes or no?")
        while confirm_entertainment == "no":
            entertainment = random_entertainment_generator ()
            confirm_entertainment = input ("Are you happy with your entertainment selection now?yes or no?")
        
        user_confirm = input("Are you happy with your trip? yes or no?")
     
    elif user_confirm == "yes":
        print (f"Have fun on your trip to {destination} by {transportation} where you will eat delicious {restaurant} food and enjoy {entertainment}!!")
    else:
        print("That is not a valid response")   



confirm_your_trip ()

        
        

        

