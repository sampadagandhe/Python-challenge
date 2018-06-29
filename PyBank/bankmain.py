import csv
import os

#input = os.path.join ("", "budget_data.csv")
input= 'budget_data.csv'


months = []
revenue = []

with open(input, "r") as csvfile:

    csvread = csv.reader(csvfile, delimiter = ",")
    
    #next(csvread, None)
    header = next(csvfile)
    
    for row in csvread:

        #print(row)
    
        #split_m_r=row[1].split(",")

        #months = months + [split_m_r[1]]

        #revenue = revenue + [split_m_r[1]]

        months.append(row[0])

        revenue.append(int(row[1]))


total_months = len(months)



greatest_inc = revenue[0]

greatest_dec = revenue[0]

total_revenue = 0


for r in range(len(revenue)):

    if revenue[r] >= greatest_inc:

        greatest_inc = revenue[r]

        great_inc_month = months[r]

    elif revenue[r] <= greatest_dec:

        greatest_dec = revenue[r]

        great_dec_month = months[r]

    total_revenue += revenue[r]



average_change = round(total_revenue/total_months, 2)



#print ('Total Months: ' + str(total_months))

#print ('Total Profit/Losses: $' + str(total_revenue))

#print ('Average Change: $' + str(average_change))

#print ('Greatest Increase in Profits: ' + great_inc_month + ' ($' + str(greatest_inc) + ')')

#print ('Greatest Decrease in Losses: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')



#set path for output file

output_path = ('output.csv')



# open the output destination in write mode and prints the summary

with open(output_path, 'w') as writefile:

    writefile.writelines('Financial Analysis\n')

    writefile.writelines('----------------------------' + '\n')

    writefile.writelines('Total Months: ' + str(total_months) + '\n')

    writefile.writelines('Total Profit/Losses: $' + str(total_revenue) + '\n')

    writefile.writelines('Average Change: $' + str(average_change) + '\n')

    writefile.writelines('Greatest Increase in Profits: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')

    writefile.writelines('Greatest Decrease in Losses: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')



#opens the output file in r mode and prints to terminal

with open(output_path, 'r') as readfile:

    print(readfile.read())



       
