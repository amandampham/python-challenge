#import appropriate modules to work across operation systems and open csv
import os 
import csv
#Establish path for csv and file to write to 
csvpath = os.path.join('..', 'Pybank', 'Resources', 'budget_data.csv')
analysispath = os.path.join('..', 'Pybank', 'Analysis', 'analysis.txt')

# Variables
totalrows = 0
totalamount = 0
previous_total = 0
total_change_list = []
month_of_change = []
average_changes = 0
total_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]

#open csv file
with open(csvpath) as csvfile:
# Run functions to clean csv data / clear the headers
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=',')

    # loop through to find total months
    for row in csvreader:
       # process each row
       totalrows += 1
       # find data in column 2 and add to total amount profit/loss

       totalamount += int(row[1])
    
        #if it is not the first iteration then do the following code to calculate change and add to change list
       if previous_total != 0:
            total_change = int(row[1])- previous_total
            # create list to store changes and grab month
            total_change_list.append(total_change)
            month_of_change = [month_of_change] + [row[0]]

            
       print(str(row[0]))
       previous_total = int(row[1])
        #Find greatest increase
       if total_change>greatest_increase[1]:
        greatest_increase[1] = total_change
        greatest_increase[0] = row[0]
        #find greatest decrease
       if total_change<greatest_decrease[1]:
        greatest_decrease[1]= total_change
        greatest_decrease[0] = row[0]
    
        
        # #Average changes over entire period 
    
        average_changes = round(sum(total_change_list)/len(total_change_list), 2)

#Write Analysis to text file
with open(analysispath, 'w') as textFile:
        textFile.write('Financial Analysis')
        textFile.write('\n')
        textFile.write('---------------------------')
        textFile.write('\n')
        textFile.write('Total Months: ')
        textFile.write(str(totalrows))
        textFile.write('\n')
        textFile.write('Total: ')
        textFile.write(str(totalamount))
        textFile.write('\n')
        textFile.write('Average Change: $')
        textFile.write(str(average_changes))
        textFile.write('\n')
        textFile.write('Greatest Increase in Profits: ')
        textFile.write(str(greatest_increase[0]))
        textFile.write('(')
        textFile.write(str(greatest_increase[1]))
        textFile.write(')')
        textFile.write('\n')
        textFile.write('Greatest Decrease in Profits: ')
        textFile.write(str(greatest_decrease[0]))
        textFile.write('(')
        textFile.write(str(greatest_decrease[1]))
        textFile.write(')')



    

