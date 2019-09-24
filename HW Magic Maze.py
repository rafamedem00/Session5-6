import random
print("You are trapped in the magic maze. Now try to escape. Good luck!")
directions = ["N", "S", "E", "W"]
answer = "Which way do you want to go?" + random.choice(directions)
secret_escape_combination = ["S", "S", "N", "W", "E", "S"]
moves = 1
lives = 3
if moves == [11, 21, 31]:
    lives = lives - 1
    print("You lost a live. You are now left with " + str(lives) + " lives. Try again!")

for i in secret_escape_combination:
    while answer == secret_escape_combination[secret_escape_combination.index(i)] is False:
        print("Start again.")
        x = x + 1
        if lives == 0:
            print("You are dead! Better luck next time!")
            break
        if answer == secret_escape_combination(i):
            i= i + 1
            if i < len(secret_escape_combination):
               print("Good! Which way do you want to go next?")
            else:
                print("Well done! You have managed to escape from the magic maze!")
