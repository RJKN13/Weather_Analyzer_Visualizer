# Import pandas library to the project
import pandas as pd
# Import pyplot interface from matplotlib library for plotting purpose
import matplotlib.pyplot as plt

# Read weather data from csv file
weather_data = pd.read_csv('weather_data.csv')

print("Welcome to Weather Analyzer & Visualization!")

# Created visualize_menu() to display options for user interaction
# User can choose to visualize all weather properties from csv file like Temperature, Precipitation, Wind Speed
# for 2 locations (Location_A, Location_B) by selecting option '4'
# User can also choose to visualize one single property by selecting either 1,2,3 options
# Option E will exit the visualize menu.
# visualize() is called, based on the option choosed that matches the case.
def visualize_menu():
    print("Welcome to Weather Visualizer!")
    option = ""
    while option == "":
        option = input("Select 1.Temperature, 2.Precipitation, 3.Wind_Speed, 4.All, E.To exit: ")
        match option.lower():
            case "1":
                visualize("Temperature")
                option = ""

            case "2":
                visualize("Precipitation")
                option = ""

            case "3":
                visualize("Wind_Speed")
                option = ""

            case "4":
                visualize("All")
                option = ""

            case "E":
                    option = "Z"


# Created visualize() to display weather plotting based on options selected by the user
# from visualize_menu()
def visualize(str):
    # If 'All' is sent, load the weather_data dataframe to specific_columns,
    # else load filtered columns from weather_data dataframe to specific_columns.
    if str == "All":
        specific_columns = weather_data
    else:
        specific_columns = weather_data[["Location", str]]
    print(specific_columns)
    # plot() is invoked to draw 'bar' diagram for specific_columns dataframe
    specific_columns.plot(kind="bar")
    # sets the plot title
    plt.title('Weather Visualization')
    # sets label on x-axis for the plot
    plt.xlabel('Location')
    # sets label on y-axis for the plot
    plt.ylabel(str)
    # to display diagram
    plt.show()

# display options for user interaction
# option 'v' displays visualize_menu()
# TODO option 'a' to analyze data
# option 'e' to exit the app
option = ""
while option == "":
    option = input("Do you want to analyze or visualize data, select 'a' or 'v' or 'e' to exit: ").lower()
    if option == "v":
        visualize_menu()

    elif option == "e":
        print("Thanks for using!")
        break
    option = ""



