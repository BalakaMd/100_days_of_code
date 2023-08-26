from random import choice
from replit import clear
# from art import sad_logo, vs, logo

instagram_accounts = {"Cristiano Ronaldo": [598, "Footballer"], "Lionel Messi": [481, "Footballer"],
                      "Selena Gomez": [427, "Musician, actress, producer and businesswoman"],
                      "Kim Kardashian": [363, "Television personality, model and businesswoman"],
                      "Beyonce": [315, "Musician and businesswoman"], "Nike": [302, "Sportswear multinational"],
                      "National Geographic": [282, "Magazine"], "Neymar": [211, "Footballer"],
                      "Taylor Swift": [269, "Musician"], "Jennifer Lopez": [250, "Musician and actress"],
                      "Maria Balakina": [9999, "The most famous woman in the World"],
                      "Katy Perry": [204, "Musician and businesswoman"],
                      "LeBron James": [157, "Basketball player"],
                      "Rihanna": [195, "Musician and businesswoman	"],
                      "Drake": [141, "Musician"], "Vin Diesel": [98.2, "Actor"],
                      "UEFA Champions League": [107, "Club football competition	"],
                      "NASA": [94.5, "Space agency"], "Snoop Dogg": [80.4, "Musician"],
                      "NBA": [82.5, "Professional basketball league"]
                      }
list_of_famous = [x for x in instagram_accounts.keys()]


def play_game():
    first_account = choice(list_of_famous)
    second_account = choice(list_of_famous)
    game_score = 0
    # print(logo)
    while True:
        print(f"Compare A: {first_account}, {instagram_accounts[first_account][1]}")
        # print(vs)
        print(f"Against B: {second_account}, {instagram_accounts[second_account][1]}")
        user_input = input("Who has more followers? 'A' or 'B' : ").lower()
        if (user_input == "a" and instagram_accounts[first_account][0] > instagram_accounts[second_account][0]) \
                or (user_input == "b" and instagram_accounts[second_account][0] > instagram_accounts[first_account][0]):
            clear()
            # print(logo)
            game_score += 1
            first_account = second_account
            second_account = choice(list_of_famous)
            print(f"You're right!. Current score is {game_score}\n")
            print(f"{first_account} with {instagram_accounts[first_account][0]} millions followers")
            print(f"And {second_account} with {instagram_accounts[second_account][0]} millions followers\n")
        else:
            clear()
            print("Sorry, that's wrong")
            print(f"{first_account} with {instagram_accounts[first_account][0]} millions followers.")
            print(f"And {second_account} with {instagram_accounts[second_account][0]} millions followers.")
            # print(sad_logo)
            break
    repeat = input("Try again? ").lower()
    print(repeat)
    if repeat in ["Yes", 'y']:
        play_game()


play_game()
