import os
import csv


#Load CSV file
budget = os.path.join("budget_data.csv")

#Declare Dictionary and Lists
DataDict = {}
datelist = []
indexlist = []
GainLossList = []
rowcounter = 0

#Read CSV file into lists
with open(budget) as f:
    csvreader = csv.reader(f, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        indexlist.append(rowcounter)
        datelist.append(row[0])
        GainLossList.append(int(row[1]))
        rowcounter += 1

#Combine two lists into a dictonary
DataDict = {a: b for a, b in zip(datelist, GainLossList)}

totalPL = sum(DataDict.values())
CountMonths = len(DataDict.values())
BestMonth = max(DataDict.values())
WorstMonth = min(DataDict.values())
BestMonth_Date = list(DataDict.keys())[list(DataDict.values()).index(BestMonth)]
WorstMonth_Date = list(DataDict.keys())[list(DataDict.values()).index(WorstMonth)]



PythonBudgetHW = open("PythonBudgetHW.txt","w+")



PythonBudgetHW.write('   \n')
PythonBudgetHW.write('   \n')
PythonBudgetHW.write('Financial Analysis\n')
PythonBudgetHW.write('Prepared by Greg Poppe\n')
PythonBudgetHW.write('----------------------------------------------------------\n')
PythonBudgetHW.write('   \n')
PythonBudgetHW.write(f'Total Months: {CountMonths}\n')
PythonBudgetHW.write(f'Total Change: $ {totalPL}\n')
PythonBudgetHW.write(f'Average Change: ${round(totalPL/CountMonths,2)}\n')
PythonBudgetHW.write(f'Greatest increase in Profits was on: {BestMonth_Date} for: ${BestMonth}\n')
PythonBudgetHW.write(f'Greatest decrease in Profits was on: {WorstMonth_Date} for: ${WorstMonth}\n')
PythonBudgetHW.write('   \n')
PythonBudgetHW.write('------------------------End--------------------------------\n')


PythonBudgetHW.close()