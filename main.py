# Importing the 'data' dictionary from the 'data' module.
from data import data

# Function to search for vehicles by make.
# It takes a make (string) as input and returns a list of vehicles of that make.
def search_make(make):
    # The make is converted to lowercase to ensure case-insensitive matching.
    # 'get' is used to safely retrieve data to avoid KeyError if the make is not found.
    return data.get(make.lower())

# Function to search for vehicles by model within a given list of models.
# It takes a list of models and a model (string) to search for.
def search_model(models, model):
    # List comprehension is used to filter and return all models that match the input model.
    return [m for m in models if m[0].lower() == model.lower()]

# Function to search for vehicles by year within a given list of models.
# It takes a list of models and a year (integer) to search for.
def search_year(models, year):
    # List comprehension to filter and return all models that match the input year.
    return [m for m in models if m[1] == year]

# Function to search for a vehicle by color within a given list of models.
# It takes a list of models and a color (string) to search for.
def search_color(models, color):
    # Loop through each model in the list.
    for m in models:
        # Check if the color matches the input color (case-insensitive).
        if m[2].lower() == color.lower():
            # Return the first matching model.
            return m
    # Return None if no match is found.
    return None

# Function to format the vehicle details into a readable multi-line string.
# It takes a vehicle (list) as input.
def format_vehicle_details(vehicle):
    # Formatting the vehicle details using f-string for better readability.
    return (
        f"Model: {vehicle[0]}\n"
        f"Year: {vehicle[1]}\n"
        f"Color: {vehicle[2]}\n"
        f"Trim: {vehicle[3]}\n"
        f"Price: {vehicle[4]}"
    )

# Main function to run the vehicle search program.
def main():
    # Loop to handle vehicle make input.
    while True:
        make_input = input("Enter the make of the vehicle (e.g., 'Toyota', 'Ford'): ")
        make_results = search_make(make_input)

        # Check if any vehicles are found for the input make.
        if make_results:
            # Break the loop if vehicles are found.
            break
        else:
            # Prompt the user to try a different make if no vehicles are found.
            print(f"No vehicles found for make '{make_input.title()}'. Please try a different make.")

    # Loop to handle vehicle model input.
    while True:
        model_input = input("Enter the model you are searching for: ")
        model_results = search_model(make_results, model_input)

        if model_results:
            break
        else:
            print(f"No models found for '{model_input.title()}'. Please try a different model.")

    # Loop to handle vehicle year input.

    while True:
        try:
            year_input = int(input("Enter the year of the vehicle: "))
            year_results = search_year(model_results, year_input)

            if year_results:
                break
            else:
                print(f"No vehicles found for year '{year_input}'. Please try a different year.")
        except ValueError:
            # Handle invalid input (not an integer).
            print("Please enter a valid year.")

    # Loop to handle vehicle color input.
    while True:
        color_input = input("Enter the color preference: ")
        final_result = search_color(year_results, color_input)

        if final_result:
            # Format and print the final vehicle details if a match is found.
            formatted_result = format_vehicle_details(final_result)
            print(f"Details for your selected vehicle:\n{formatted_result}")
            break
        else:
            # Prompt the user to try a different color if no vehicles are found.
            print(f"No vehicles found in color '{color_input.title()}'. Please try a different color.")

# Check if the script is run directly (not imported) and then call main.
if __name__ == "__main__":
    main()
