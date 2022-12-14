import random


def valid_response (str_input):
    validated_response = str_input
    valid_response=False
    while valid_response != True:
        if str_input == "yes":
            valid_response = True
            validated_response = "yes"
        elif str_input == "no":
            valid_response = True
            validated_response = "no"
        else:
            valid_response = False
            str_input = input ("That is an invalid response please only type yes or no.")     
    return (validated_response)



# lists

destination_list = ['the art museum', 'the park', 'the beach', 'the mountains', 'the history museum']

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


destination = random_destination_generator ()
restaurant = random_restaurant_generator ()
transportation = random_transportation_generator ()
entertainment = random_entertainment_generator ()

user_happy = False
while user_happy != True:
    user_confirm = input("Are you happy with your trip? yes or no?")
    user_confirm = valid_response (user_confirm)
    
    
    if user_confirm == "no":
        
        confirm_destination = input ("Are you happy with your destination? yes or no?")
        confirm_destination = valid_response (confirm_destination)
        if confirm_destination == "yes":
            confirm_destination = True
            print ("Perfect! Let's continue.")
        else:
            confirm_destination = False
            while confirm_destination != True:
                destination = random_destination_generator ()
                confirm_destination = input("Are you happy with your new destination? yes or no?")
                confirm_destination = valid_response (confirm_destination)
                if confirm_destination == "yes":
                    confirm_destination = True
                    print ("Perfect! Let's continue.")
                    
                else:
                    confirm_destination = False
                    

        confirm_restaurant = input ("Are you happy with your restaurant? yes or no?")
        confirm_restaurant = valid_response (confirm_restaurant)
        if confirm_restaurant == "yes":
            confirm_restaurant = True
            print ("Perfect! Let's continue.")
        else:
            confirm_restaurant = False
            while confirm_restaurant != True:
                restaurant = random_restaurant_generator ()
                confirm_restaurant = input("Are you happy with your new restaurant? yes or no?")
                confirm_restaurant = valid_response (confirm_restaurant)
                if confirm_restaurant == "yes":
                    confirm_restaurant = True
                    print ("Perfect! Let's continue.")
                else:
                    confirm_restaurant = False
                    

        confirm_transport = input ("Are you happy with your method of transportation? yes or no?")
        confirm_transport = valid_response (confirm_transport)
        if confirm_transport == "yes":
            confirm_transport = True
            print ("Perfect! Let's continue.")
        else:
            confirm_transport = False
            while confirm_transport == False:
                transportation = random_transportation_generator ()
                confirm_transport = input("Are you happy with your new method of transportation? yes or no?")
                confirm_transport = valid_response (confirm_transport)
                if confirm_transport == "yes":
                    confirm_transport = True
                    print ("Perfect! Let's continue.")
                else:
                    confirm_transport = False

        confirm_entertainment = input ("Are you happy with your entertainment? yes or no?")
        confirm_entertainment = valid_response (confirm_entertainment)
        if confirm_entertainment == "yes":
            confirm_entertainment = True
            print ("Perfect! Let's continue.")
        else:
            confirm_entertainment = False
            while confirm_entertainment == False:
                entertainment = random_entertainment_generator ()
                confirm_entertainment = input("Are you happy with your new entertainment? yes or no?")
                confirm_entertainment = valid_response (confirm_entertainment)
                if confirm_entertainment == "yes":
                    confirm_entertainment = True
                    print ("Perfect! Let's continue.")
                else:
                    confirm_entertainment = False
                        
    
    else:
        user_happy = True
        print (f"Have fun on your trip to {destination} by {transportation} where you will eat delicious {restaurant} food and enjoy {entertainment}!!")








        
        

        

