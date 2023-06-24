import os
import csv

#budget_data = "C:/Users/aliac/python-challenge/PyBank/Resources/budget_data.csv"
budget_data = os.path.join("Resources", "budget_data.csv")

#open budget data csv file 
with open(budget_data,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 

    next(csvreader, None) #removes/bypasses the header
    #define values 
    m = 0  #months 
    total = 0  #profits/losses
    totalch = 0
    fr = next(csvreader) #fr is the first row
    m = 1
    prev = float(fr[1])
    total = total + prev
    print('Financial Analysis') #sets the title above data
    
    for row in csvreader:
        m = m + 1 #count number of rows in csv file
        current = float(row[1]) #define 'current' as the second column of csv file
        change = current - prev
        total = total + current
        totalch = totalch + change
        prev = current

    print("Total Months:", m)
    print("Total:", total)
    print(totalch)