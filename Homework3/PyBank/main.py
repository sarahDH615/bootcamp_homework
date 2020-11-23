import os
import csv

#lists to hold values from col1(row[0]) and col2(row[1])
months = []
money_made = []
max_inc = 0
max_dec = 0
#categories = []
#values1 = []
#values2 = []

#functions to call for finding values from the lists


csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    for row in csvreader:
        if row[0] == "Date":
            continue
        months.append(row[0])
        if row[1] == "Profit/Losses":
            continue
        money_made_int = int(row[1])
        money_made.append(money_made_int)
        if int(row[1]) > max_inc:
            max_inc = int(row[1])
            max_inc_month = row[0]
        if int(row[1]) < max_dec:
            max_dec = int(row[1])
            max_dec_month = row[0]
    
    #print(months)
    #print(money_made)
    #print(max_inc)
    #print(max_inc_month)
    #print(max_dec)
    #print(max_dec_month)


print("                   ")
print("Financial Analysis:")
print("______________________________________")    
print("                   ")

months_total = int(len(months))
print(f"Total Months: {months_total}")
#values1.append(int(len(months)))

#def months_total(a_list):
#    print(f"Total Months: {int(len(a_list))}")
#months_total(months)


net_total = sum(money_made)
print(f"Net Total: ${net_total} ")
#values1.append(net_total)

#def net_total(a_list):
    #print(f"Net Total: ${(sum(a_list))} ")
#net_total(money_made)

avg_change = round((net_total/months_total), 2)
print(f"Average Change: ${avg_change}")
#values1.append(avg_change)

#def avg_change_calc():
    #months_total/net_total

print(f"Greatest Increase in Profits: {max_inc_month} (${max_inc})")
print(f"Greatest Decrease in Profits: {max_dec_month} (${max_dec})")

#values1.append(max_inc_month)
#values1.append(max_dec_month)

#values2.append(max_inc)
#values2.append(max_dec)

#categories = ["Total Months:", "Net Total:", "Average Change:", "Greatest Increase in Profits:", "Greatest Decrease in Profits:"]

#def max_val(a_list):
    #currently displaying wrong max number, needs to incl the date
    #print(f"Maximum Increase in Profits: ${max(a_list)}")
#max_val(money_made)
#def min_val():
#    min(money_made)
print("                   ")
print("______________________________________")    
print("(End of 'Financial Analysis'")
print("                   ")


#2 col: [0] is heading; [1] is data


output_path = os.path.join("Analysis", "pybank_results.csv")

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])

    csvwriter.writerow(["Total Months:", "86"])

    csvwriter.writerow(["Net Total:", "$38382578"])

    csvwriter.writerow(["Average Change:", "$446309.05"])

    csvwriter.writerow(["Greatest Increase in Profits:", "Feb-2012" ,"$1170593"])

    csvwriter.writerow(["Greatest Decrease in Profits:", "Sep-2013" ,"$-1196225"])





    





       
