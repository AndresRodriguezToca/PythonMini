# Andres Rodriguez Toca
# COP1047C-2197-15601
# 10/3/2019

#Declare variables
numberOrganisms= 0
dailyPopulation = 0.0
averageIncrease = 0.0
numberDays = 0
counter = 2

#Get the number of organism
print("Starting number of organisms:", end=' ')
numberOrganisms = int(input())

# If necessary loop through the input until the user provive a valid entry
while numberOrganisms < 2:
  print("The starting number of organisms must be at least 2.")
  print("Starting number of organisms:", end=' ')
  numberOrganisms = int(input())

#Get the average daily population increase
print("Average daily increase:", end=' ')
averageIncrease = float(input())

# If necessary loop through the input until the user provive a valid entry
while averageIncrease <= 0:
  print("Average daily increase:", end=' ')
  averageIncrease = float(input())

#Get the number of days to multiply
print("Number of days to multiply:", end=' ')
numberDays = int(input())

# If necessary loop through the input until the user provive a valid entry
while numberDays < 1:
  print("Number of days must be at least 1:", end=' ')
  numberDays = float(input())

#Header
print("Day Approximate", "\t", "Population")
print("-----------------------------------")

#Print first day
print(1, "\t", "\t", numberOrganisms)

#Calculate daily increase and print result
while counter <= numberDays:
  #Do this if average it's greater than one
  if averageIncrease > 1:
    dailyPopulation = (numberOrganisms * averageIncrease)/100 + numberOrganisms
    numberOrganisms = dailyPopulation
  #Else this if average it's less than one
  else:
    dailyPopulation = (numberOrganisms * averageIncrease) + numberOrganisms
    numberOrganisms = dailyPopulation
  print(counter, "\t", "\t", dailyPopulation)
  counter = counter + 1