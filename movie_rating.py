# movie_rating.py - A Simple Movie Rating Checker
# Author: Wesley
# Date: [Today's Date]
# Description: A Python program that checks movie ratings based on user age.

# Get user information
user_name = input("What's your name? ")
age = input("How old are you? ")

# Validate and convert age input
while not age.isdigit():  # Ensures user enters a valid number
    print("Please enter a valid age (numbers only).")
    age = input("How old are you? ")

age = int(age)  # Convert age from string to integer

# Determine what movies the user can watch
print(f"\nHi {user_name}! Based on your age, you can watch:")

if age < 13:
    print("- G rated movies")
    print("- PG rated movies")
    print("\nYou're too young for PG-13 and R-rated movies.")
elif 13 <= age < 17:
    print("- G rated movies")
    print("- PG rated movies")
    print("- PG-13 rated movies")
    print("\nCome back in a few years to watch R-rated movies!")
else:
    print("- G rated movies")
    print("- PG rated movies")
    print("- PG-13 rated movies")
    print("- R-rated movies")
    print("\nYou're old enough to watch any movie!")

# Bonus Challenge: Ask about a specific movie
print("\n🎬 Bonus: Let's check if you can watch a specific movie!")

movie_title = "Deadpool"
movie_rating = "R"

print(f"\nThe movie '{movie_title}' is rated {movie_rating}.")
watch_movie = input(f"Do you want to watch '{movie_title}'? (yes/no): ").strip().lower()

if watch_movie == "yes":
    if age >= 17:
        print(f"Great! You are old enough to watch '{movie_title}'. Enjoy!")
    else:
        print(f"Sorry, you're too young to watch '{movie_title}'. Try something else!")
else:
    print("No worries! Pick another movie and enjoy!")

print("\nThanks for using the Movie Rating Checker! 🎥")
