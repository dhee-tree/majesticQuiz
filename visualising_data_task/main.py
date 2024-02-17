from visualiser import DataVisualisation
from data import drink_data, sweet_data

def main():
    plot_sweets = DataVisualisation(sweet_data, 'Sweet', 'Mass (g)', 'Estimated mass of sweets consumed during a student hackathon.')
    plot_drinks = DataVisualisation(drink_data, 'Drink', 'Litre', 'Estimated litres of soft drink consumed at a student hackathon.')
    
    plot_drinks.plot_data()

    plot_sweets.plot_data()
    
if __name__ == "__main__":
    main()
