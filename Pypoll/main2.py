#import os module to go across operational systems 
import os

#import csv module to be able to access csv files 
import csv


#csv file path
csvpath = os.path.join('..', 'Pypoll', 'Resources', 'election_data.csv')
#analysis file path
analysispath = os.path.join('..', 'Pypoll', 'Analysis', 'analysis.txt')

#define variables
totalrows = 0
candidate_list = []
total_votes_count = 0


#open csv file 
with open(csvpath) as csvfile:
  
  # Run functions to clean csv data / clear the headers
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=',')

    # establish counters for each candidate
    Stockham_Count =0 
    Degette_Count = 0
    Li_Count = 0
    Doane_Count = 0
   
  
    # loop through to find total months
    for row in csvreader:
       
    # process each row
        totalrows += 1
    #counter 
        total_votes_count += 1

    #conditionals and counter to tally votes for each candidate 
        if row[2] == "Charles Casper Stockham":
            Stockham_Count += 1
        elif row[2] == "Diana DeGette":
            Degette_Count += 1
        elif row[2] == "Raymon Anthony Doane":
            Doane_Count += 1

 #loop through dictionary ( key= cadidate name and value= votes)
Results = {"Stockham":Stockham_Count, "Degette":Degette_Count, "Doane":Doane_Count}

# Calculate percentages and round to 3 decimal places
Stockham_Percent = round((Stockham_Count / total_votes_count) * 100, 3)
Degette_Percent = round((Degette_Count / total_votes_count) * 100, 3)
Doane_Percent = round((Doane_Count / total_votes_count) * 100, 3)

 # Find the max value from the values in the dictionary and return its key, then store as 'Winner'
Winner = max(Results, key=Results.get)



#Write Analysis to text file
with open(analysispath, 'w') as textFile:
    toprint = f"""Election Results
-------------------------
Total Votes: {totalrows}
-------------------------
Charles Casper Stockham: {Stockham_Percent}% ({Stockham_Count})
Diana DeGette: {Degette_Percent}% ({Degette_Count})
Raymon Anthony Doane: {Doane_Percent}% ({Doane_Count})
-------------------------
Winner: {Winner}
-------------------------
    """
    print(toprint)
    textFile.write(toprint)
    ## older stuff - redundant
    ###
    ##   textFile.write(toprint)
    ## textFile.write('Election Analysis')
    ## textFile.write('\n')
    ## textFile.write('---------------------------')
    ## textFile.write('\n')
    ## textFile.write('Total Votes: ')
    ## textFile.write(str(totalrows))
    ## textFile.write('\n')
    ## textFile.write('---------------------------')
    ## textFile.write('\n')
    ## textFile.write('Charles Casper Stockham: ')
    ## textFile.write(str(Stockham_Percent))
    ## textFile.write('(')
    ## textFile.write(')')
    ## textFile.write(str(Stockham_Count))
    ## textFile.write('\n')
    ## textFile.write('Diana DeGette: ')
    ## textFile.write(str(Degette_Percent))
    ## textFile.write('(')
    ## textFile.write(')')
    ## textFile.write(str(Degette_Count))
    ## textFile.write('\n')
    ## textFile.write('Raymon Anthony Doane: ')
    ## textFile.write(str(Doane_Percent))
    ## textFile.write('(')
    ## textFile.write(')')
    ## textFile.write(str(Doane_Count))
    ## textFile.write('\n')
    ## textFile.write('\n')
    ## textFile.write('---------------------------')
    ## textFile.write('\n')
    ## textFile.write('Winner: ')
    ## textFile.write(str(Winner))
    ## textFile.write('\n')
    ## textFile.write('---------------------------')
    ## textFile.write('\n')
    


 

