import pandas as pd
import matplotlib.pyplot as plt

#This function makes it easier to display the counts of unique data in columns and minimises the code used. Nothing returned. 
#Argument: colummn_name, (dType pandas.DataFrame)
#           (Column name of the data wou want to get information about)
#Return: no return
def column_data(column_name):
    print(column_name + " data")
    print(df[column_name].value_counts())
    print('\n')

#The following function is needed to format the seperate date columns in preperation for concatanation. 
#Dates are change from float to int for better presentation. Nans are converted to 0s first though because they cause errors
#when converted to int. The 0s(nans) are then converted to unknown eg Start Month Unknown.
#Argument: title, (dType pandas.DataFrame)
#           (title is the column name)
#Return: no return
def format_nans(title):
    df[title]= df[title].fillna(0)
    df[title] = df[title].astype(int)
    df[title] = df[title].replace(0, title + ' Unknown')

#print information about the data
#Argument: no Args
#Return: no return
def info():
    print("Data + info:")
    print(df.shape)
    print(df.head(5)) 
    print(df.columns)
    df.info()
    

#Load data and set options to make it easier to display in terminal
df = pd.read_csv('VolcanoData.csv', skiprows=1)
pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.max_columns', df.shape[1] + 1)

#Print information about the data and part of the data itself:
info()


#Testing the columns to see which data to delete and which to keep:
print('--------------Unique data types (and count) in each column--------------')
column_data('Eruption Category') #keep
column_data('VEI') #keep but replace Nans with unknown
column_data('VEI Modifier') #delete
column_data('Start Year Modifier') #delete all modifer data
column_data('Start Year Uncertainty') #delete all uncertainty data
column_data('Evidence Method (dating)') #keep
column_data('Start Month') #Some months are 0. change to 1
print('------------------------------------------------------------------------')
#Some start and end dates are 0. 0 is not a date and will be replaced by 1.
df['Start Month'] = df['Start Month'].replace(0,1)
df['Start Day'] = df['Start Day'].replace(0,1)
df['End Month'] = df['End Month'].replace(0,1)
df['End Day'] = df['End Day'].replace(0,1)

#check
print("0s replaced")
column_data('Start Month') 
column_data('Start Day') 
column_data('End Month') 
column_data('End Day') 

#There are no more "0"s
print('------------------------------------------------------------------------')

print("Exploring missing values:")
print("Null Values")
print(df.isnull().sum())
print("\n Nan Values")
print(df.isna().sum())

#Delete area of activity data: coordinates and name are enough. Too many Nans in area.
#Data map may/ may not include VEI number based on search filters applied so all will be kept.

print("Data shape before deleting columns:"+ str(df.shape))

#delete all modifier and uncertainty columns. Eruption number, volcano number and area of activity are also not neededed. The rest are useful columns.
df = df.drop(['VEI Modifier', 'Start Year Modifier', 'Start Year Uncertainty','Start Day Modifier', 'Start Day Uncertainty', 'End Year Modifier',\
     'End Year Uncertainty','End Day Modifier', 'End Day Uncertainty', 'Volcano Number', 'Eruption Number', 'Area of Activity'], axis=1)

#delete nan start year columns
df = df[df['Start Year'].notna()]

print("Data shape after deleting columns:"+ str(df.shape))
print('------------------------------------------------------------------------')

print("Data shape before deleting duplicates:"+ str(df.shape))
df.drop_duplicates(inplace=True)
print("Data shape after deleting duplicates:"+ str(df.shape)) #No duplicates

print('-------------------------------------------------------------------------')
print("Data shape before deleting rows with missing data:"+ str(df.shape))
df = df.dropna(thresh= 7, axis=0) #remove rows which miss more than half of the data
print("Data shape after deleting rows with missing data:"+ str(df.shape))

print('-------------------------------------------------------------------------')

#After the data has bean cleaned it will be explored. However, part of the exploration should be done before the
#Nans are removed as it may be difficult to subtract the values afterwards.

df['Lifetime (years)'] = df['End Year'] - df['Start Year']

#Formatting dates using a function and then concatanating into single column
#to_datetime() could not be used becaue it only goes down to 1677

#Year has no nans so is converted to int directly
df['Start Year'] = df['Start Year'].astype(int)

format_nans('Start Month')
format_nans('Start Day')
format_nans('End Year')
format_nans('End Month')
format_nans('End Day')

#Concatanating dates:
df['Start Date'] = df['Start Year'].map(str) + '/' + df['Start Month'].map(str) + '/' + df['Start Day'].map(str)
df['End Date'] = df['End Year'].map(str) + '/' + df['End Month'].map(str) + '/' + df['End Day'].map(str)

print('-------------------------------------------------------------------------')
print("Nan values before being replaced:\n" + str(df.isna().sum()))

#The remaining Nans will be shown as "unknown" in the data presentation.
df['VEI']= df['VEI'].fillna('VEI Unknown')
df['Evidence Method (dating)']= df['Evidence Method (dating)'].fillna('Evidence Method (dating) Unknown')

print("Nan values after being replaced:\n" + str(df.isna().sum()))

print('-------------------------------------------------------------------------')
print("Clean data:\n")
info()

#The lifetime data column will be cleaned from Nans after it has been explored to make the process easier.

df.to_csv('clean_volcano_data.csv')