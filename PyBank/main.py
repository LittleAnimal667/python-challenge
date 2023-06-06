import os
import csv

#budget_data = "C:/Users/aliac/python-challenge/PyBank/Resources/budget_data.csv"
budget_data = os.path.join("Resources", "budget_data.csv")

#open budget data csv file 
with open(budget_data,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 

    next(csvreader, None) #removes/bypasses the header
    #define values 
    average = 0
    m = 0
    i = 0
    print('Financial Analysis')
    for col in csvreader:
        
        m = m+1 #count number of rows in csv file
        i = i + float(col[1]) #define i as the second column of csv file
        
    
    print("Total Months:", m)
    print("Total:", i)