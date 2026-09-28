# EXTRAORDINARY QUIZ: SMART ANIMALS!
print("Let the quiz begin!")

# participant name
username = input("State your name:")
print("Let's go", username)

# points initialisation
points = 0

# trivia 1
t1_ans= input("""Q1: Which of these animals is vastly smarter than the others? \nA. Dolphin, B. Squirell, C. Baboon""")

if t1_ans=="A":
    print("You got it!")
    points = points + 1
else:
    print("The correct answer was A!")

# trivia 2
t2_ans = input("Q2: How does a black bear protect its babies? A. It stares at the intruders , B. It eats them , C. It chases t...")

if t2_ans=="C":
    print("Stunning!")
    points = points + 1
else:
    print("Should have picked C!")

# trivia 3

print("What is the danger that a scorpion poses relative to its size? - pick the best option:")

print("A.2cm")
print("B.13cm")
print("C.20cm")
t3_ans = input("Enter A, B or C!")

if t3_ans=="A":
    print("Spot on! The smaller they are, the worse!")
    points = points + 1
else:
    print("No! The smallest ones are the worst!")

# Results of the game

print("That's the end folks! Great work", username,"!" )
print("Here's how you fared:", points)

if points == 3:
    print("Wow",username,"! You sure know a lot about animals!")
elif points <=1:
    print("Not gonna lie",username,",you really need to brush up on your animal trivia!")
else:
    print("Not bad for a baby",username,"!")

print("Thanks for playing!")