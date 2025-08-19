"""
Program: payroll.py
Chapter 4 example
8/1/2025


"""

import os.path
import time

# Input phase
fileName = input("Please type the name of the payroll file that you wis to process >>")

# WHILE loop which will test if the fileName is provided is a real file. If not, it will prompt the user again until a valid filename is provided
while os.path.isfile(fileName) == False:
	fileName = input(f"Sorry! {fileName} does NOT exist. Please enter a VALID payroll filename >> ")

print("Processing the file data...")
time.sleep(2)

# process and output phases
data = open(fileName, "r")

print()
print("%-18s%9s%9s%11s" % ("Last Name", "Wage", "Hours", "Earnings"))
print("-" * 50)


# Loop through the file line by line. Split up the date in each line. Place each component into tabular format and calculate the earnings. 
for line in data:
	# Break the line into individual string parts
	dataArray = line.split()
	# Extract the last name from that array and store it 
	name = dataArray[0]
	# Extract the wage from the array and store it
	wage = float(dataArray[1])
	# Extractthe hours from the array, convert it to a float and store it
	hours = float(dataArray[2])
	# Next, calculate the earnings and store it 
	earnings = wage * hours
	# Output that info into tabular format 
	print("%-18s%9.2f%9.2f%11.2f" % (name, wage, hours, earnings))

# Final sign-off essage
input("End of file. Press ENTER to quit.")