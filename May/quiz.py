# Ask the user 3 questions, keep track of how many they get right, print their score at the end.
# You pick the questions — make them about anything you want.
score = 0
answer1 = input("what colour is my home? ").lower()
if answer1 == "yellow":
    print("correct!")
    score += 1 #test if int is needed
else:
    print("wrong!")

answer2 = input("what city do i live in? ").lower()
if answer2 in ["helsinki", "helsingfors"]:
    print("correct!")
    score += 1
else:
    print("wrong!")

answer3 = input("how many siblings do i have? ").lower()
if answer3 in ["1", "one"]:
    print("correct!")
    score += 1
else:
    print("wrong!")

if score >= 3:
    print(f"well done! you got {score} points!")
elif score == 2:
    print(f"decent, you got {score} points.")
else:
    print(f"you could've done better, you got {score} points.")

