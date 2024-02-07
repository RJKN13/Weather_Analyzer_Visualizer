# Import pandas library to the project
import pandas as pd
# Import pyplot interface from matplotlib library for plotting purpose
import matplotlib.pyplot as plt

# Read weather data from csv file
weather_data = pd.read_csv('weather_data.csv')
print(weather_data)

row_dict = {
    '1': "Location",
    '2': "Temperature",
    '3': "Precipitation",
    '4': "WindSpeed"
}

print("Welcome to Weather Analyzer & Visualization!")

# Created visualize_menu() to display options for user interaction.
# User can choose to visualize all weather properties from csv file like Temperature,
# Precipitation, WindSpeed for 2 locations (Location_A, Location_B) by selecting option '4'
# User can also choose to visualize one single property by selecting either 1,2,3 options.
# Option E will exit the visualize_menu.
# visualize() is called, based on the option choosed that matches the case.
def visualize_menu():
    print("Welcome to Weather Visualizer!")
    option = ""
    while option == "":
        option = input("Select 1.Temperature, 2.Precipitation, 3.WindSpeed, 4.All, E.To exit: ")
        match option.lower():
            case "1":
                visualize("Temperature")
                option = ""

            case "2":
                visualize("Precipitation")
                option = ""

            case "3":
                visualize("WindSpeed")
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
                selected_column = input("Which column do you want to sort: 1.Location, 2.Temperature, 3.Precipitation, 4.WindSpeed?: ")
                column_order = input("Do you want to sort in ascending order or descending order? 'a' or 'd': ")
                sort(selected_column, column_order)
                option = ""

            case "2":
                filter_column = input("Which column do you want to filter: 2.Temperature, 3.Precipitation, 4.WindSpeed? ")
                filter_value = int(input("Enter the value: "))
                filter_order = input("Do you want to filter </> on the filter value: ")
                filter_data(filter_column, filter_value, filter_order)
                option = ""

            case "3":
                location_name = input("Location Name: ")
                temperature = int(input("Temperature: "))
                precipitation = int(input("Precipitation: "))
                wind_speed = int(input("WindSpeed: "))
                new_row = {
                    "Location": location_name,
                    "Temperature": temperature,
                    "Precipitation": precipitation,
                    "WindSpeed": wind_speed
                }
                add_row(new_row)
                option = ""

            case "4":
                row_index = int(input("Which row do you want to delete: "))
                delete_row(row_index)
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


# Sort the df weather_data using sort_values() by passing 2 arguments column_name, ascending flag
# User entered data reads a number as key, which is interpreted from row_dict dictionary
def sort(column_name, ascending):
    flag = ""
    if ascending == 'a':
        flag = True
    else:
        flag = False
    print(row_dict[column_name], flag)

    df = weather_data.sort_values(by=row_dict[column_name], ascending=flag)
    print(df)

# Filter the df weather_data using filter_data()
# Based on the user input to filter the data in </> by filter_value
# User entered data reads a number as key(column_name), which is interpreted from row_dict dictionary
def filter_data(column_name, filter_value, filter_order):
    if filter_order == "<":
        filtered_df = weather_data[weather_data[row_dict[column_name]] < filter_value]
    else:
        filtered_df = weather_data[weather_data[row_dict[column_name]] > filter_value]
    print(filtered_df)


# Based on the user input, data can be added into csv file.
def add_row(new_row):
    # load weather_data into a DataFrame object
    df = pd.DataFrame(weather_data)
    # concat the 2 data frames df, df for new_row
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    # write data frame to CSV file
    df.to_csv('weather_data.csv', mode='w', index=False)
    # print message
    print("Data appended successfully!")

# Based on the user input, which is row index, drop the row from the dataframe and update the csv file.
def delete_row(selected_row):
    # load weather_data into a DataFrame object
    df = pd.DataFrame(weather_data)
    # Delete row based on the user input, using drop()
    df = df.drop(selected_row)
    # write data frame to CSV file
    df.to_csv('weather_data.csv', mode='w', index=False)
    print(df)


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