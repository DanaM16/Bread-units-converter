from datetime import datetime
import json

"""This is a simple program which converts carbohydrates into bread units using the formula: 30 grams of 
carbohydrates = 1 bread unit, and saves them into .txt file with date and time.
This formula is used in Continuous Subcutaneous Insulin Infusion or Insulin Pump."""

# Set current date and time
now = datetime.now()
current_time = now.strftime("%A, %d of %B %Y at %X")

# User's input of carbs
while True:

    try:
        carbs = int(input("Enter grams of carbohydrates: "))

        # Converting to bread units
        bread = carbs / 30
        bread = round(bread, 1)

        # Calculated bread units
        print(f"{carbs} grams of carbohydrate is {bread} bread units.")

        # Text for "history.txt" file
        memory = f"{bread} bread units were injected on {current_time}"

        # Create and append the record to the "history.txt" file
        with open("history.txt", "a") as history_file:
            history_file.write(json.dumps(memory))
            history_file.write("\n")

            # Break the while loop
            break

    except ValueError:
        # Print the error message
        print("Please enter only numbers!")
