# High Scores 2.0
# Demonstrates nested sequences

scores = []
# what am i doing wrong for the scores not to be accessing the nested tables? pg 136 of Python Programming for the Absolute Beginner,
choice = None
while choice != "0":

    print(
    """
    High Scores 2.0
        
    0 - Quit
    1 - List Scores
    2 - Add a Score
    """
    )
    choice = input("Choice: ")
    print()
#exit
if choice == "0":
    print("Good-bye.")

# display high-score table
elif choice == "1":
    print("High Scores\n")
    print("NAME\tSCORE")
    for entry in scores:
        score, name = entry
        print(name, "\t", score)

# add a score
elif choice == "2":
    name = input("What is the player's name?: ")
    score = int(input("What score did the player get?: "))
    entry = (score, name)
    scores.append(entry)
    scores.sort(reverse=True)
    scores = scores[:5]  # keep only top 5 scores
#why is my program not keeping the top 5 scores? is there not a database?
# some unkown choice
else:
    print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")