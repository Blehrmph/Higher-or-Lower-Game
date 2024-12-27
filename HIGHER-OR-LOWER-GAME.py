from HigherOrLower_Game.game_data import data
from art import logo, vs
import random


def message(score):
    print(f"Sorry, that's wrong. Final score: {score}")

def new_page():
    print("\n"*20)

random_person = random.choice(data)
score=0
smth=True
while smth:
    print(logo)
    if score>0:
        print(f"You're right! Current score: {score}.")

    random_person2 = random.choice(data)

    print(f"Compare A: {random_person['name']}, a {random_person['description']}, from {random_person['country']}. ")
    print(vs)
    print(f"Against: {random_person2['name']}, a {random_person2['description']}, from {random_person2['country']}. ")
    answer=input("Who has more followers? Type 'A' or 'B':")
    if answer=='A':
        if random_person['follower_count']>=random_person2['follower_count']:
            score+=1
            random_person=random_person2
            new_page()
        elif random_person['follower_count']<random_person2['follower_count']:
            smth=False
            new_page()
            print(logo)
            message(score)

    elif answer=='B':
        if random_person['follower_count']<=random_person2['follower_count']:
            score+=1
            random_person = random_person2
            new_page()
        elif random_person['follower_count']>random_person2['follower_count']:
            smth=False
            new_page()
            print(logo)
            message(score)
    else:
        smth=False
        new_page()
        print(logo)
        message(score)


