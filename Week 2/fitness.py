# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (F/M): ")
    birthdate = input("Enter yout birthdate (in this format YYYY-MM-DD): ")
    inches = float(input("Enter your height in US inches: "))
    pounds = float(input("Enter your weight in US pounds: "))

    # Call the compute_age function
    age = compute_age(birthdate)

    # Call the kg_from_lb function 
    weight_in_kilograms = kg_from_lb(pounds)

    # Call the cm_from_in function
    height_in_centimeters = cm_from_in(inches)

    # Call the body_mass_index function
    bmi = body_mass_index(weight_in_kilograms, height_in_centimeters)

    # Call the basal_metabolic_rate function
    bmr = basal_metabolic_rate(gender, weight_in_kilograms, height_in_centimeters , age)
    
    # Print the results for the user to see.
    print(f"Age: {age}")
    print(f"Weight (kg): {weight_in_kilograms:.2f}")
    print(f"Height (cm): {height_in_centimeters:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate: {bmr:.0f}")
    
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    (1 lb = 0.45359237 kg)
    """
    weight_in_kg = pounds * 0.45359237
    return weight_in_kg


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    (1 in = 2.54 cm)
    """
    height_in_cm = inches * 2.54
    return height_in_cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = weight / (height ** 2) * 10000
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.upper() == "F" :
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    elif gender.upper() == "M" :
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr


# Call the main function so that
# this program will start executing.
main()
