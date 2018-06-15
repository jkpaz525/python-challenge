# Dependencies
import os
import csv
from pathlib import Path

bank_csv = os.path.join("raw_data", "budget_data_1.csv")

filename = Path("raw_data/budget_data_1.csv")

totalrev = 0 
numMonths = 0

# Track the total
with open(filename) as csvfile:
    reader = csv.reader(csvfile)

    next(reader)
    revenue = []
    date = []
    revenue_change = []

        #sum of column 1 
    for row in reader:
        revenue.append(int(row[1]))
        date.append(row[0])


print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months: ", len(date))
print ("Total Revenue: $", sum(revenue))

#total of difference between all rows
for i in range(1, len(revenue)):
    revenue_change.append (revenue[i] - revenue[i-1])
    avg_rev_change = sum(revenue_change)/len(revenue_change)

    max_rev_change = max(revenue_change)

    min_rev_change = min(revenue_change)

    max_rev_change_date = str(date[revenue_change.index(max(revenue_change))])
    min_rev_change_date = str(date[revenue_change.index(min(revenue_change))])

print("Average Revenue Change: $", round(avg_rev_change))
print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")


#f= open("bank.txt","w+")
#f.write("Financial Analysis\n")
#f.write("-------------------------------\n")
#f.write("Total Months: "+ str(len(date))+ "\n")
#f.write("Total Revenue: $"+ str(sum(revenue)) +"\n")
#f.write("Average Revenue Change: $"+ str(round(avg_rev_change)+ "\n")
#f.write("Greatest Increase in Revenue:"+ str(max_rev_change_date)+"($"+ str(max_rev_change)+")" +"\n")
#f.write("Greatest Decrease in Revenue:"+ str(min_rev_change_date)+"($"+ str(min_rev_change)+")"+"\n")
#f.close()

text_path = os.path.join('.', 'budget_analysis_2.txt')
with open(text_path, "w") as text_file:
   text_file.write("Financial Analysis\n")
   text_file.write("-----------------------------------\n")
   text_file.write("Total Months:" + str(len(date)) + "\n")
   text_file.write("Total Revenue: $" + str(sum(revenue)) + "\n")
   text_file.write("Average Revenue Change : $" + str(round(avg_rev_change)) + "\n")
   text_file.write("Greatest Increase in Revenue :" + str(max_rev_change_date) + "($" + str(max_rev_change) + ")" + "\n")
   text_file.write("Greatest Decrease in Revenue :" + str(min_rev_change_date) + "($" + str(min_rev_change) + ")" + "\n")