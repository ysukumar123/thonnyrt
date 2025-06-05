# Quiz Game
# This will ask the user some questions and check their answers
# Points will be given for each correct answer
# Points will be taken away for wrong answers

score = 0  # Changed score to an integer

# Welcome user to the game
print("Welcome to our Quiz Game!")

# Ask user for their name
name = input("What is your name? ")

print(f"Hey {name}, that's a nice name! Maybe I'll name my kids after you.")

# Ask the first quiz question

# Check the answer

# Assign points
print("\n1. What is Kendrick Lamar's latest album?")
print("a) GNX")
print("b) Damn.")
print("c) good kid, m.A.A.d city")
print("d) Untitled Unmastered")

ans1 = input("Your answer: ").lower().strip()

if ans1 == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong")
    score -= 1

# Ask the second question
# Check answer
# Assign points

print("\n2. What is Travis Scott's real name?")
print("a) Travis Marcus Scott")
print("b) Jacques Webster")
print("c) Tyson Lamar Spielberg")
print("d) Travis Scott")

ans2 = input("Your answer: ").lower().strip()

if ans2 == "b":
    print("You're pretty smart!")
    score += 1
else:
    print("Wrong")
    score -= 1
# Ask the second question
# Check answer
# Assign points
print("\n3. Who was the BillBoard Rap Artist Of the Year in 2015?")
print("a) Eminem")
print("b) Iggy Azalea")
print("c) Drake")
print("d) Young Thug")

ans3 = input("Your answer: ").lower().strip()

if ans3 == "b":
    print("Your a Professional!")
    score += 1
else:
    print("Wrong")
    score -= 1


# Show the final score
# Say thanks for playing
print(f"Your final score is {score}!")
print("Thanks for playing!")
