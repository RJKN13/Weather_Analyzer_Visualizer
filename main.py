# Import pandas library to the project
import pandas as pd
# Import pyplot interface from matplotlib library for plotting purpose
import matplotlib.pyplot as plt

# Read weather data from csv file
weather_data = pd.read_csv('weather_data.csv')

print("Welcome to Weather Analyzer & Visualization!")

# Created visualize_menu() to display options for user interaction.
# User can choose to visualize all weather properties from csv file like Temperature,
# Precipitation, Wind_Speed for 2 locations (Location_A, Location_B) by selecting option '4'
# User can also choose to visualize one single property by selecting either 1,2,3 options.
# Option E will exit the visualize_menu.
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
                print("Returning to the main screen!")


# Created analyze_menu() to display options for user interaction.
# User can choose to analyze weather data from csv file like Sort, Filter, Add & Delete.
# Sort: User can sort the data by column either asc or dsc.
# Filter: User can filter the data by column & value.
# Add Row: Enables app to add new data in a row, can be reserved for admins(todo).
# Delete Row: Enables app to delete a row, can be reserved for admins(todo).
# Option E will exit the analyze_menu.
def analyze_menu():
    print("Welcome to Weather Analyzer!")
    option = ""
    while option == "":
        option = input("Select 1.Sort Values, 2.Filter Data, 3.Adding Row,"
                       " 4.Delete Row, E.To exit: ")
        match option.lower():
            case "1":
                selected_column = input("Which column do you want to sort: 1.Location, 2.Temperature, 3.Precipitation, 4.Wind_Speed?: ")
                column_order = input("Do you want to sort in ascending order or descending order? 'a' or 'd': ")
                print(selected_column, column_order)

                option = ""

            case "2":
                filter_column = input("Which column do you want to filter: 1.Location, 2.Temperature, 3.Precipitation, 4.Wind_Speed? ")
                print(filter_column)
                option = ""

            case "3":
                location_name = input("Location Name: ")
                temperature = int(input("Temperature: "))
                precipitation = int(input("Precipitation: "))
                wind_speed = int(input("Wind_Speed': "))
                print(location_name, temperature, precipitation, wind_speed)
                option = ""

            case "4":
                row_index = int(input("Which row do you want to delete: "))
                print(row_index)
                option = ""

            case "E":
                option = "Z"
                print("Returning to the main screen!")


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
# option 'a' to analyze data
# option 'e' to exit the app
option = ""
while option == "":
    option = input("Do you want to analyze or visualize data, select 'a' or 'v' or 'e' to exit: ").lower()
    if option == "v":
        visualize_menu()
    elif option == "a":
        analyze_menu()
    elif option == "e":
        print("Thanks for using!")
        break
    option = ""