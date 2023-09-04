import pandas as pd
import matplotlib.pyplot as plt

#This function replaces Nan values in a column with the column title + Unknown.
#Argument: title, (dType pandas.DataFrame)
#           (title is the column name)
#Return: no return
def replace_nans(title):
    df[title]= df[title].fillna(title + ' Unknown')

#Load data and set options to make it easier to display in terminal
df = pd.read_csv('clean_volcano_data.csv')
pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.max_columns', df.shape[1] + 1)

#exploring the data

#Plotting Histogram for volcanoes over year ranges
plt.hist((df['Start Year']))
plt.title('Histogram Showing Eruptions Over Time')
plt.xlabel('Years')
plt.ylabel('No. of Volcano Starting')
plt.show()

#From the plot one can observe that there are many more data points in the past 1000 years,
#it may be  interesting for the user to seperate the data into modern eruption and older eruptions.
#Plotting volcanoes over the past 2021 years:

plt.hist((df['Start Year']), range(2021) )
plt.title('Histogram Showing Eruptions Over Time')
plt.xlabel('Years')
plt.ylabel('No. of Volcano Starting')
plt.show()
#from the finer plot it is clear that more data is available for the past 300 years.


#Scatter plot of lon/lan values.
plt.scatter(df['Longitude'],df['Latitude'])
plt.title('Eruptions Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.xticks(range(-180, 180, 15))
plt.yticks(range(-90, 90, 15))
plt.grid()
plt.figure('map')
plt.show


#checking for outliers for active time:
boxplot = df.boxplot(column=['Lifetime (years)'])
boxplot.plot()
plt.show()
print(df.loc[df['Lifetime (years)'] > 270])

#Longest lifetime is 299 years: some volcanoes can be active for hundreds of years: not an outlier
#Lifetime Nan values can be now replaced with "Unknown"
replace_nans('Lifetime (years)')
print("Nan values:\n" + str(df.isna().sum()))

print('-------------------------------------------------------------------------')
print("Clean data:\n")
print(df.head(25))

df.to_csv('clean_explored_data.csv')