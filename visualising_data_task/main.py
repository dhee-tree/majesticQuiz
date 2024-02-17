from visualiser import DataVisualisation
from data import drink_data, sweet_data

def main():
    sweets_data = DataVisualisation(sweet_data, 'Sweet', 'Mass (g)', 'Estimated mass of sweets consumed during a student hackathon.')
    drinks_data = DataVisualisation(drink_data, 'Drink', 'Litre (l)', 'Estimated litres of soft drink consumed at a student hackathon.')

    continue_plotting = True
    while continue_plotting:
        print("Which data would you like to plot?\n1. Sweet data\n2. Drink data\n3. Exit")
        try:
            prompt = "Please enter your choice: "
            user_input = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            if user_input == 1:
                sweets_data.plot_data()
            elif user_input == 2:
                drinks_data.plot_data()
            elif user_input == 3:
                print("Exiting... Goodbye!")
                continue_plotting = False
            else:
                print("Invalid input. Please enter '1', '2' or '3'.")

if __name__ == "__main__":
    main()
