Players = ["Dave", "Paul", "Jesse", "Vadim", "Mason", "Luke"]
Stats = [[22,4,8],[34,6,9],[54,3,8],[43,6,11],[4,10,13],[3,5,9]]
Events = ["Bench Press", "Shoulder Press", "Pullups"]
noEvents = 3

#Create an 1d arrays that will store the averages of each event
eventAverages = []
eventTotals = []
eventRecords = [0,0,0]


#Create an array to store 'cut' or 'signed' status
status = []

#Create a variable of Integer type to store the number of players
noPlayers = len(Players)
#Create variables to store the best performers in each exercise
recordHolders = ["","",""]
#Temporary variable to store total of event scores
tempTotal = 0
#Variable used to count the number of events above average
plusCount = 0

#Calculate the total of each Event
for x in range (0, noEvents):
  for y in range (0,noPlayers):
    tempTotal += Stats[y][x]
  eventTotals.append(tempTotal)
  tempTotal = 0

#Calculate the average of each event - Rounded
for x in range (0,3):
  eventAverages.append(round(eventTotals[x]/noPlayers))

#Determine which players are cut or signed
for x in range(0,noPlayers):
  for y in range(0,noEvents):
    if Stats[x][y] > eventAverages[y]:
      plusCount = plusCount + 1
  if plusCount >=2:
    status.append("Signed")
  else:
    status.append("Cut")
  plusCount = 0


#Output the players names and signing status
for x in range(0,noPlayers):
  print(f"Name - {Players[x]}, Status - {status[x]}")

#Calculate event record holders
for x in range (0, noPlayers):
  for y in range (0,3):
    if Stats[x][y] > eventRecords[y]:
      eventRecords[y] = Stats[x][y]
      recordHolders[y] = Players[x]

#Output record holders
print("\nRecord Holders: ")
for x in range (0,noEvents):
  print(f"{Events[x]} - {recordHolders[x]}")
