""" 
Create a function that estimates the weight loss of a person 
using a certain weight loss program with their gender, 
current weight and how many weeks they plan to do the program as input. 
If the person follows the weight loss program, 
men can lose 1.5% of their body weight per week 
while women can lose 1.2% of their body weight per week. 

The possible inputs are:
Gender: 'M' for Male, 'F' for Female
Current weight: integer above 0
Number of weeks: integer above 0

Return the estimated weight after the specified number of weeks.
"""

def gender_func():
    gender = input("Enter your gender (M/F): ")
    while gender.upper() not in 'MF':
        print(f"{gender} is not a valid input!")
        gender = input("Enter your gender (M/F): ")
    gender = gender.upper()
    return gender

def weight_func():
    current_weight = input("Enter your current weight in kg: ")
    while current_weight.isdigit() == False or int(current_weight) < 0:
        print(f"{current_weight} is not a valid input!")
        current_weight = input("Enter your current weight in kg: ")
    current_weight = float(current_weight)
    return current_weight

def weeks_func():
    weeks = input("How many weeks do you plan to use the weight loss program? (Enter a number): ")
    while weeks.isdigit() == False or int(weeks) <= 0:
        print(f"{weeks} is not a valid input!")
        weeks = input("How many weeks do you plan to use the weight loss program? (Enter a number): ")
    weeks = int(weeks)
    return weeks

def est_weight_func(gender, current_weight, weeks):
    est_weight = None
    if gender == 'M':
        est_weight = current_weight
        for i in range(1, weeks+1):
            est_weight = (est_weight * 0.985) 
    elif gender == 'F':
        est_weight = current_weight
        for i in range(1, weeks+1):
            est_weight = (est_weight * 0.988) 
    est_weight = round(est_weight, 2)
    return est_weight

def weight_loss_calc():

    gender = gender_func()
    current_weight = weight_func()
    weeks = weeks_func()
    est_weight = est_weight_func(gender, current_weight, weeks)

    return_string = f"""
Your current weight is {current_weight}kgs.
If you follow the weight loss program for {weeks} weeks,
your estimated weight will be {est_weight}kgs."""
    return return_string

print(weight_loss_calc())