logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
               
               
               #To-Do List


#If they get it correct replace choice B with A and bring a new choice to replace choice B
#Make the logo present throughout the gameplay

#Keep the game going until the user get's a comparison wrong
#Show the score while the user is playing and after the user lost
import random
from data import data

#generate two random individuals to compare
user_score = 0
continue_game = 1


def generate_random_name():
    name = []
    
    name.append(random.choice(data))
    name.append(random.choice(data))
    
    return name

name = generate_random_name()


user_input = ""


def switch_person (name): 
    name[0] = name[1]
    name[1] = (random.choice(data))
    print(name)
    return name


def prompt():

    print(logo)

    #Present User with two choices and their descriptions
    print(f"{name[0]['name']}, a {name[0]['description']}, from {name[0]['country']}\n")
    print(vs)
    print(f"{name[1]['name']}, a {name[1]['description']}, from {name[1]['country']}")


    #Ask the user who has more followers
    return input("\nWho has more followers on instagram? \nType 'A' or 'B' (lowercase only): ")



#assigns the follower count to a variable to use
def follower_count(name):
    person_followercount_a = int(name[0]['follower_count']) 
    person_followercount_b = int(name[1]['follower_count'])

    follower_list = [person_followercount_a, person_followercount_b]
    return follower_list
    
#compares the followers and gives either true or false
def compare(user_input, user_score):
    follower_list = follower_count(name)
    
    #Compare the follower count of the two choices and decide which is greater
    if user_input == "a" and follower_list[0] > follower_list[1]:
        return 1
    elif user_input == "b" and follower_list[0] < follower_list[1]:
        return 1
    else: return 2
  



def game(user_input, user_score, name):    
    user_input = prompt()
    result = compare(user_input, user_score)

    #Create a score system that keeps track of how many selections they got correct
    if result == 1:
        user_score += 1
        print(f"\nYou're correct! You're score is now {user_score}")
        return 1
    else: 
        print(f"\nYou lose :( \nYour final score was {user_score}")
        return 0


#switch_person(person_name_a, person_name_b)


while continue_game == 1:
    continue_game = game(user_input, user_score, name)
    name = switch_person(name)
    user_score += 1
    


