# Weather_Analyzer_Visualizer

Detailed description of application:

Functional description: The app is enabled to analyze and visualize the weather data from a csv file. User interaction is enabled so that the user can choose different options during analysis and visualization. Below are the detailed feature of the app.
•	Main Menu: The main menu gives 2 options to the user to choose between analysis and visualization. If ‘a’ is chosen analysis menu will be displayed. If ‘v’ is chosen visualize menu will be displayed. App can be exited with option ‘e’.

•	Analyze Menu: This menu offers the below options to the user to choose:

1.	Sort Values: User can be able to sort the weather data on properties like Location, Temperature, Precipitation, Wind Speed either in asc or desc order.

2.	Filter Data: Weather data can be filtered by the user on columns such as Temperature, Precipitation, Wind Speed on values. Results are limited based on the user selection </>




3.	Adding Rows: Weather data for a new location can be added with this feature where the app enables users to add properties.

4.	Deleting Rows: Row can be deleted from the weather data based on the row index.


5.	‘e’ for Exit
   
Visualize Menu: This menu offers the below options to the user to choose.  Based on the selected option, a bar graph will be displayed to the user comparing the data between the Locations on x-axis and selected option data on y-axis.
1.	Temperature
2.	Precipitation
3.	Wind Speed
4.	All
5.	‘E’ for exit


Technical description: 
‘main.py’ imports pandas and matplotlib libraries to analyze and visualize the weather data. Properties like Temperature, Precipitation, Wind Speed are analysed and visualized between locations from the ‘weather_data.csv’
After loading the csv file into the dataframe, user has options to choose between analyse and visualize. Choosing ‘a’ will invoke ‘analyze_menu()’ and ‘v’ will invoke ‘visualize_menu()’ and ‘e’ exits the application.

•	Analyze_menu(): User can choose between different data analysis properties like sort, filter, add, delete. User choice is matched with ‘match-case’ statement and below functions are invoked.  

•	sort(selected_column, column_order): Sorts the df weather_data using sort_values() by passing 2 arguments column_name, ascending flag. User entered data, reads a number as key, which is interpreted from row_dict dictionary.

•	filter_data(filter_column, filter_value, filter_order): Filters the df weather_data using pandas filter functionality. Based on the user input to filter the data in </> by filter_value. User entered data reads a number as key(column_name), which is interpreted from row_dict dictionary.

•	add_row(new_row): Based on the user input, data can be added into csv file. pd.concat() is used to concat new data to the existing data and the updated dataframe is written to csv file using df.to_csv()

•	delete_row(row_index): Based on the user input, which is row index, drop the row from the dataframe using df.drop() and updated dataframe is written to csv file using df.to_csv()
