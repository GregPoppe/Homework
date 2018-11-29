import os
import csv


#Load CSV file
pypoll = os.path.join("election_data.csv")


#Initialize variables
totalvotes = 0
candidates = {}
khanvotes = 0
livotes = 0
correyvotes = 0
otooleyvotes = 0

with open(pypoll) as f:
    csvreader = csv.reader(f, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        totalvotes += 1
        if row[2] == "Khan":
            khanvotes += 1
        if row[2] == "Li":
            livotes += 1
        if row[2] == "Correy":
            correyvotes += 1
        if row[2] == "O'Tooley":
            otooleyvotes += 1


results = {'Khan': khanvotes}
results.update({'Li': livotes})
results.update({'Correy': correyvotes})
results.update({"O'Tooeley": otooleyvotes})
winningvotes = max(results.values())
winner = list(results.keys())[list(results.values()).index(winningvotes)]


PythonPollHW = open("PythonPollHW.txt","w+")
PythonPollHW.write(f"")





PythonPollHW.write('Election Results \n')
PythonPollHW.write('---------------------------------------\n')
PythonPollHW.write(f'Total Votes: {totalvotes}\n')
PythonPollHW.write('---------------------------------------\n')
PythonPollHW.write(f'Khan: {round(100*(khanvotes/totalvotes),2)}% ({khanvotes})\n')
PythonPollHW.write(f'Li: {round(100*(livotes/totalvotes),2)}% ({livotes})\n')
PythonPollHW.write(f'Correy: {round(100*(correyvotes/totalvotes),2)}% ({correyvotes})\n')
PythonPollHW.write(f"O'Tooley: {round(100*(otooleyvotes/totalvotes),2)}% ({otooleyvotes})\n")
PythonPollHW.write('---------------------------------------\n')
PythonPollHW.write(f'The winner is: {winner} with {winningvotes} votes\n')
PythonPollHW.write('---------------------------------------')


PythonPollHW.close()