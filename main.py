from datetime import datetime, timedelta
import sqlite3, sys

d = datetime.today() - timedelta(hours=4, minutes=0)

d.strftime('%H:%M %p')
now = datetime.now()
#print(now)
current_time = now.strftime("%H:%M:%S")
#print("Current Time =", d.strftime('%H:%M %p'))

months = {
  1: 744,
  2: 672,
  3: 744,
  4: 720,
  5: 744,
  6: 720,
  7: 744,
  8: 744,
  9: 720,
  10: 744,
  11: 720,
  12: 744,
}

class Point :
  def __init__(self, name):
    self.name = name
    self.start = 0
    self.isOpen = True
    self.timeTaken = 0
    self.timeMonth = 0
    self.timeYear = 0
    self.efficiencyMonth = 0
    self.efficiencyYear = 0
    
    
  def getName(self):
    print("Name: {}".format(self.name))
    return self.name
    
  def setName(self, name):
    self.name = name
    print("Name is now: {}".format(self.name) +"\n")

  def getIsOpen(self):
    return self.isOpen

  def setIsOpen(self, open):
    self.isOpen = open

  def setSpotName(self):
    elevation = input("What is the elevation number? ")
    elevation = str(elevation)
    group = input("What is the group number? ")
    group = str(group)
    row = input("What is the row number? ")
    row = str(row)
    spot = input("What is the spot number? ")
    spot = str(spot)
    fullName = elevation + "-" + group + "-" + row + "-" + spot
    self.name = fullName
    print("Name is now: {}".format(self.name) +"\n")

  def getElevation(self):
    x = self.name.split("-")
    elevation = x[0]
    return elevation

  def getGroup(self):
    x = self.name.split("-")
    group = x[1]
    return group

  def getRow(self):
    x = self.name.split("-")
    row = x[2]
    return row

  def getSpot(self):
    x = self.name.split("-")
    spot = x[3]
    return spot

  def excludeEl(self):
    x = self.getGroup()
    y = self.getRow()
    z = self.getSpot()
    name = x + "-" + y + "-" + z
    return name
  def getAllInfo(self):
    print("Spot Name: {}".format(self.name) + "\n")
    if self.isOpen == 1:
      temp = "Yes";
    else:
      temp = "No";
      print("Time spot was recorded as taken: {}".format(self.start) + "\n")
    print("Is the spot open: {}".format(temp) + "\n")
    print("Spot Time Taken total: {}".format(self.timeTaken) + "\n")
    print("Spot Time Taken for the month: {}".format(self.timeMonth) + "\n")
    print("Spot Time Taken for the year: {}".format(self.timeYear) + "\n")
    print("Spot Efficiency for the month: {}".format(self.efficiencyMonth) + "\n")
    print("Spot Efficiency for the year: {}".format(self.efficiencyYear) + "\n")
    
  def getTimeTaken(self):
    return self.timeTaken

  def getStartTime(self):
    return self.start

  def setStartTime(self, time):
    self.start = time

  def getTimeMonth(self):
    print("Time for the month: {}".format(self.timeMonth) +"\n")
    return self.timeMonth
  
  def setTimeMonth(self, time):
    self.timeMonth = time

  def getTimeYear(self):
    print("Time for the year: {}".format(self.timeYear) +"\n")
    return self.timeYear

  def setTimeYear(self, time):
    self.timeYear = time

  def isTaken(self):
    startingNow = datetime.today() - timedelta(hours=4, minutes=0)
    self.start = startingNow.hour
    self.isOpen = False

  def isNowOpen(self):
    self.isOpen = True
    closingTime =  d.strftime('%H')
    startingTime = self.start
    elapsedTime = int(closingTime) - int(startingTime)
    self.timeTaken += elapsedTime
    self.timeMonth += elapsedTime
    self.timeYear += elapsedTime
    self.start = 0
    
  def setTimeTaken(self, time):
    self.timeTaken = self.timeTaken + time

  def updateTimeMonth(self):
    self.timeMonth = 0
    print("timeMonth now set to 0 " +"\n")

  def updateTimeYear(self):
    self.timeYear = 0
    self.timeTaken = 0
    print("timeYear and timeTaken now set to 0 " +"\n")  

  def getYearEfficiency(self):
    yearSeconds = 0
    if(now.month > 1):
      yearSeconds = 0
      for x in range(now.month):
        x += 1
        yearSeconds += months[x]
    else:
      yearSeconds = months[now.month]
    self.efficiencyYear = self.timeYear / yearSeconds
    if(self.efficiencyYear<.01):
      self.efficiencyYear = 0
    else:
      self.efficiencyYear = self.efficiencyYear
    self.efficiencyYear = self.efficiencyYear * 100
    self.efficiencyYear = "{:.2f}".format(self.efficiencyYear)
    return self.efficiencyYear

  def setYearEfficiency(self, eff):
    self.efficiencyYear = eff
  
  def getMonthEfficiency(self):
    monthSeconds = months[now.month]
    self.efficiencyMonth = self.timeMonth / monthSeconds
    if(self.efficiencyMonth<.01):
      self.efficiencyMonth = 0
    else:
      self.efficiencyMonth = self.efficiencyMonth
    self.efficiencyMonth = self.efficiencyMonth * 100
    self.efficiencyMonth = "{:.2f}".format(self.efficiencyMonth)
    return self.efficiencyMonth
    
  def setMonthEfficiency(self, eff):
    self.efficiencyMonth = eff

class Lot :
  name = "UnNamed"
  list = []
  def __init__(self, name):
    self.name = name
    
  def setName(self, name):
    self.name = name
    print("Name is now: {}".format(self.name) +"\n")

  def getLotName(self):
    return self.name
  
  def addParkingSpot(self, p):
    self.list.append(p)

  def CreateRow(self):
    elevation = input("What is the elevation number? ")
    elevation = str(elevation)
    group = input("What is the group number? ")
    group = str(group)
    row = input("What is the row number? ")
    row = str(row)
    startNumber = input("What is the starting spot number? ")
    startNumber = str(startNumber)
    endNumber = input("What is the ending spot number? The ending number will be a spot created ")
    endNumber = str(endNumber)
    intStart = int(startNumber)
    intEnd = int(endNumber)
    for x in range(intStart, intEnd+1):
      strX = str(x)
      fullName = elevation + "-" + group + "-" + row + "-" + strX
      s1 = Point(fullName)
      self.list.append(s1)
      print("name: {}".format(s1.name))
      print("time taken: {}".format(s1.timeTaken))
      print("time month: {}".format(s1.timeMonth))
      print("time month: {}".format(s1.timeYear) +"\n")
    
  def showParkingSpot(self):
    for x in range(len(self.list)):
      print("name: {}".format(self.list[x].name))
      print("time taken: {}".format(self.list[x].timeTaken))
      print("time month: {}".format(self.list[x].timeMonth))
      print("time month: {}".format(self.list[x].timeYear) +"\n")

  def clearTimeMonth(self):
    for x in range(len(self.list)):
      self.list[x].updateTimeMonth()

  def clearTimeYear(self):
    for x in range(len(self.list)):
      self.list[x].updateTimeYear()
      
  def findName(self, findName):
    for x in range(len(self.list)):
      if(findName == self.list[x].name):
        print("time month: {}".format(self.list[x].timeMonth))
        return self.list[x]

  def getName(self, findName):
    for x in range(len(self.list)):
      if(findName == self.list[x].name):
        return self.list[x]
        
  def findtimeMonth(self, findtimeMonth):
    for x in range(len(self.list)):
      if(findtimeMonth == self.list[x].timeMonth):
        return self.list[x]

  def findtimeYear(self, findtimeYear):
    for x in range(len(self.list)):
      if(findtimeYear == self.list[x].timeYear):
        return self.list[x]

  def elCounter(self):
    elDict = {}
    sortedElDict = {}
    for x in range(len(self.list)):
      elevation = self.list[x].getElevation()
      if elevation not in elDict:
        elDict[elevation] = 1
      else:
        num = elDict.get(elevation)
        num += 1
        elDict[elevation] = num
    sortedElDict = sorted(elDict.items(), key = lambda kv: kv[1], reverse=True)
    return sortedElDict

  def getElCount(self, number):
    elDict = {}
    counter = 0
    number = str(number)
    for x in range(len(self.list)):
      elevation = self.list[x].getElevation()
      if elevation not in elDict:
        elDict[elevation] = 1
      else:
        num = elDict.get(elevation)
        num += 1
        elDict[elevation] = num
    counter = elDict.get(number)
    return counter

  def getElTime(self, number):
    time = 0
    count = 0
    for x in range(len(self.list)):
      elevation = self.list[x].getElevation()
      if int(elevation) == int(number):
        time += self.list[x].getTimeTaken()
        count += 1
      else:
        continue
    return time
  
  def getNumberOfEl(self):
    elDict = {}
    counter = 0
    for x in range(len(self.list)):
      elevation = self.list[x].getElevation()
      if elevation not in elDict:
        elDict[elevation] = 1
        counter +=1
      else:
        continue
    return counter

  def topElTime(self, number):
    elDict = {}
    sortedElDict = {}
    time = 0
    NumEl = self.getNumberOfEl()
    for x in range(NumEl):
      index = x + 1
      time = self.getElTime(index)
      elDict[index] = time
    sortedElDict = sorted(elDict.items(), key = lambda kv: kv[1], reverse=True)
    if number > len(sortedElDict):
        number = len(sortedElDict)
        print("Number of entries is now {}\n".format(number))
    for x in range(number):
      index = x + 1
      print("Elevation: {}".format(index))
      time = self.getElTime(index)
      print("Elevation time: {}\n".format(time))
    return sortedElDict
    
  def groupCounter(self):
    groupDict = {}
    sortedGroupDict = {}
    for x in range(len(self.list)):
      group = self.list[x].getGroup()
      if group not in groupDict:
        groupDict[group] = 1
      else:
        num = groupDict.get(group)
        num += 1
        groupDict[group] = num
    sortedGroupDict = sorted(groupDict.items(), key = lambda kv: kv[1], reverse=True)
    return sortedGroupDict
  
  def getGroupCount(self, number):
    groupDict = {}
    counter = 0
    number = str(number)
    for x in range(len(self.list)):
      group = self.list[x].getGroup()
      if group not in groupDict:
        groupDict[group] = 1
      else:
        num = groupDict.get(group)
        num += 1
        groupDict[group] = num
    counter = groupDict.get(number)
    return counter

  def getGroupTime(self, elNumber, gNumber):
    time = 0
    count = 0
    for x in range(len(self.list)):
      elevation = self.list[x].getElevation()
      if int(elevation) == int(elNumber):
        group = self.list[x].getGroup()
        if int(group) == int(gNumber):
          time += self.list[x].getTimeTaken()
          count += 1
        else:
          continue
      else:
          continue
    return time

  def getNumberOfGroup(self):
    groupDict = {}
    counter = 0
    for x in range(len(self.list)):
      group = self.list[x].getGroup()
      if group not in groupDict:
        groupDict[group] = 1
        counter +=1
      else:
        continue
    return counter

  def topGroupTime(self, el, number):
    groupDict = {}
    sortedGroupDict = {}
    time = 0
    NumGroup = self.getNumberOfGroup()
    for x in range(NumGroup):
      groupIndex = self.list[x].getGroup()
      index = x + 1
      time = self.getGroupTime(el, index)
      groupDict[groupIndex] = time
    sortedGroupDict = sorted(groupDict.items(), key = lambda kv: kv[1], reverse=True)
    if number > len(sortedGroupDict):
        number = len(sortedGroupDict)
        print("Number of entries is now {}\n".format(number))
    for x in range(number):
      index = x + 1
      groupIndex = self.list[index].getGroup()
      print("In elevation: {}". format(el))
      print("Group: {}".format(groupIndex))
      time = self.getElTime(index)
      print("Group time: {}\n".format(time))
    return sortedGroupDict
  
  def rowCounter(self):
    rowDict = {}
    sortedRowDict = {}
    for x in range(len(self.list)):
      row = self.list[x].getRow()
      if row not in rowDict:
        rowDict[row] = 1
      else:
        num = rowDict.get(row)
        num += 1
        rowDict[row] = num
    sortedRowDict = sorted(rowDict.items(), key = lambda kv: kv[1], reverse=True)
    return sortedRowDict
  
  def getRowCount(self, elNumber, gNumber, rNumber):
    rowDict = {}
    counter = 0
    number = str(rNumber)
    for x in range(len(self.list)):
      elevation = self.list[x].getElevation()
      if int(elevation) == int(elNumber):
        group = self.list[x].getGroup()
        if int(group) == int(gNumber):
          row = self.list[x].getRow()
          if row not in rowDict:
            rowDict[row] = 1
          else:
            num = rowDict.get(row)
            num += 1
            rowDict[row] = num
        else:
          continue
      else:
        continue
    counter = rowDict.get(number)
    return counter
    
  def getRowTime(self, elNumber, gNumber, rNumber):
    time = 0
    count = 0
    for x in range(len(self.list)):
      elevation = self.list[x].getElevation()
      if int(elevation) == int(elNumber):
        group = self.list[x].getGroup()
        if int(group) == int(gNumber):
          row = self.list[x].getRow()
          if int(row) == int(rNumber):
            time += self.list[x].getTimeTaken()
            count += 1
          else:
            continue
        else:
          continue
      else:
          continue
    print("Number of spots at those locations: {}".format(count))
    print("Row time: {}".format(time))
    return time
  
  def spotCounter(self):
    spotDict = {}
    sortedSpotDict = {}
    for x in range(len(self.list)):
      spot = self.list[x].getSpot()
      if spot not in spotDict:
        spotDict[spot] = 1
      else:
        num = spotDict.get(spot)
        num += 1
        spotDict[spot] = num
    sortedSpotDict = sorted(spotDict.items(), key = lambda kv: kv[1], reverse=True)
    return sortedSpotDict
  
  def getSpotCount(self, number):
    spotDict = {}
    counter = 0
    number = str(number)
    for x in range(len(self.list)):
      spot = self.list[x].getSpot()
      if spot not in spotDict:
        spotDict[spot] = 1
      else:
        num = spotDict.get(spot)
        num += 1
        spotDict[spot] = num
    counter = spotDict.get(number)
    return counter
        
  def allgreatestTimeMonth(self):
    tempList = self.list
    tempList.sort(key = lambda x:x.timeMonth, reverse=True)
    for x in range(len(tempList)):
      print("name: {}".format(tempList[x].name))
      print("time taken: {}".format(tempList[x].timeTaken))
      print("time month: {}".format(tempList[x].timeMonth) +"\n")

        
  def greatestTimeMonth(self, number):
    tempList = self.list
    tempList.sort(key = lambda x:x.timeMonth, reverse=True)
    for x in range(number):
      print("name: {}".format(tempList[x].name))
      print("time taken: {}".format(tempList[x].timeTaken))
      print("time month: {}".format(tempList[x].timeMonth) +"\n")

  def allgreatestTimeYear(self):
    tempList = self.list
    tempList.sort(key = lambda x:x.timeYear, reverse=True)
    for x in range(len(tempList)):
      print("name: {}".format(tempList[x].name))
      print("time taken: {}".format(tempList[x].timeTaken))
      print("time month: {}".format(tempList[x].timeYear) +"\n")
      
  def greatestTimeYear(self, number):
    tempList = self.list
    tempList.sort(key = lambda x:x.timeYear, reverse=True)
    for x in range(number):
      print("name: {}".format(tempList[x].name))
      print("time taken: {}".format(tempList[x].timeTaken))
      print("time month: {}".format(tempList[x].timeYear) +"\n")

  def elevationMenu(self):
    print("Welcome to the elevation menu ")
    print("1. Get number of spots per elevation ")
    print("2. Get number of spots in a certain elevation ")
    print("3. Get the time of all spots at a certain elevation ")
    print("4. Get number of elevations ")
    print("5. Get the top list of elevations ")
    print("7. Go back to the previous menu ")
    print("8. Go back to the main menu ")
    response = input("What would you like to do? ")
    if response == "1":
      print(self.elCounter())
      print("")
      self.elevationMenu()
    elif response == "2":
      elevation = input("At what elevation? ")
      intEl = int(elevation)
      print(self.getElCount(intEl))
      print("")
      self.elevationMenu()
    elif response == "3":
      elevation = input("At what elevation? ")
      intEl = int(elevation)
      print(self.getElTime(intEl))
      print("")
      self.elevationMenu()
    elif response == "4":
      print(self.getNumberOfEl())
      print("")
      self.elevationMenu()
    elif response == "5":
      entries = input("Give the number of entries you want on the list: ")
      intEntries = int(entries)
      print("")
      print(self.topElTime(intEntries))
      self.elevationMenu()
    elif response == "7":
      print("")
      self.infoMenu()
    elif response == "8":
      print("")
      self.menu()
    else:
      print("That is not a recognized entry please try again: \n")
      print("")
      self.elevationMenu()

  def groupMenu(self):
    print("Welcome to the group menu ")
    print("1. Get number of groups in a certain elevation ")
    print("2. Get number of spots per group in a certain elevation ")
    print("3. Get the time of all spots at a certain group in a certian elevation ")
    print("4. Get number of groups ")
    print("5. Get the top list of groups in an elevation ")
    print("7. Go back to the previous menu ")
    print("8. Go back to the main menu ")
    response = input("What would you like to do? ")
    if response == "1":
      print(self.groupCounter())
      print("")
      self.groupMenu()
    elif response == "2":
      elevation = input("At what elevation? ")
      intEl = int(elevation)
      print(self.getGroupCount(intEl))
      print("")
      self.groupMenu()
    elif response == "3":
      elevation = input("At what elevation? ")
      intEl = int(elevation)
      group = input("At what group? ")
      intGroup = int(group)
      print(self.getGroupTime(intEl, intGroup))
      print("")
      self.groupMenu()
    elif response == "4":
      print(self.getNumberOfGroup())
      print("")
      self.groupMenu()
    elif response == "5":
      entries = input("Give the number of entries you want on the list: ")
      intEntries = int(entries)
      elevation = input("At what elevation? ")
      intEl = int(elevation)
      print(self.topGroupTime(intEl, intEntries))
      print("")
      self.groupMenu()
    elif response == "7":
      print("")
      self.infoMenu()
    elif response == "8":
      print("")
      self.menu()
    else:
      print("That is not a recognized entry please try again: ")
      print("")
      self.groupMenu()
  
  def rowMenu(self):
    print("Welcome to the row menu ")
    print("1. Get number of rows in an elevation ")
    print("2. Get number of spots per row in a certain elevation ")
    print("3. Get the time of all spots at a certain row in a group and elevation ")
    print("4. Get the number of groups ")
    print("7. Go back to the previous menu ")
    print("8. Go back to the main menu ")
    response = input("What would you like to do? ")
    if response == "1":
      print(self.rowCounter())
      print("")
      self.rowMenu()
    elif response == "2":
      elevation = input("At what elevation? ")
      intEl = int(elevation)
      group = input("At what group? ")
      intGroup = int(group)
      row = input("At what row? ")
      intRow  = int(row)
      print(self.getRowCount(intEl, intGroup, intRow))
      print("")
      self.rowMenu()
    elif response == "3":
      elevation = input("At what elevation? ")
      intEl = int(elevation)
      group = input("At what group? ")
      intGroup = int(group)
      row = input("At what row? ")
      intRow  = int(row)
      print(self.getRowTime(intEl, intGroup, intRow))
      print("")
      self.rowMenu()
    elif response == "4":
      print(self.getNumberOfGroup())
      print("")
      self.rowMenu()
    elif response == "7":
      print("")
      self.infoMenu()
    elif response == "8":
      print("")
      self.menu()
    else:
      print("That is not a recognized entry please try again: ")
      print("")
      self.rowMenu()
  
  def spotMenu(self):
    print("Welcome to the spot menu ")
    print("1. Get number of spots ")
    print("2. Get number of a certain spot name ")
    print("3. Get all information of a certain spot name ")
    print("7. Go back to the previous menu ")
    print("8. Go back to the main menu ")
    response = input("What would you like to do? ")
    if response == "1":
      print(self.spotCounter())
      print("")
      self.spotMenu()
    elif response == "2":
      spot = input("What Spot name are you looking for? ")
      intSpot  = int(spot)
      print(self.getSpotCount(intSpot))
      print("")
      self.spotMenu()
    elif response == "3":
      spot = input("What Spot name are you looking for? ")
      print("")
      intSpot  = self.getName(spot)
      intSpot.getAllInfo()
      print("")
      self.spotMenu()
    elif response == "7":
      print("")
      self.infoMenu()
    elif response == "8":
      print("")
      self.menu()
    else:
      print("That is not a recognized entry please try again: ")
      print("")
      self.spotMenu()

  def greatestMenu(self):
    print("Welcome to the row menu ")
    print("1. Get all greatest timeMonth list ")
    print("2. Get number of greatest timeMonth list ")
    print("3. Get all greatest timeYear list ")
    print("4. Get number of greatest timeYear list ")
    print("7. Go back to the previous menu ")
    print("8. Go back to the main menu ")
    response = input("What would you like to do? ")
    if response == "1":
      print("")
      self.allgreatestTimeMonth()
      print("")
      self.greatestMenu()
    elif response == "2":
      num = input("How many entries to return? ")
      intNum  = int(num)
      self.greatestTimeMonth(intNum)
      print("")
      self.greatestMenu()
    elif response == "3":
      self.allgreatestTimeYear()
      print("")
      self.greatestMenu()
    elif response == "4":
      num = input("How many entries to return? ")
      intNum  = int(num)
      self.greatestTimeYear(intNum)
      print("")
      self.greatestMenu()
    elif response == "7":
      print("")
      self.infoMenu()
    elif response == "8":
      print("")
      self.menu()
    else:
      print("That is not a recognized entry please try again: ")
      print("")
      self.greatestMenu()

  def saveLoadMenu(self):
    print("Welcome to the Save/Load menu ")
    print("1. Save current parkinglot ")
    print("2. load saved parking lot ")
    print("8. Go back to the main menu ")
    response = input("What would you like to do? ")
    if response == "1":
      print("")
      try:
        self.clearDatabase()
      except:
        print("")
      self.saveSpots()
      print("")
      self.saveLoadMenu()
    elif response == "2":
      print("")
      try:
        self.getSpotInfo()
      except:
        print("")
      self.saveLoadMenu()
    elif response == "8":
      print("")
      self.menu()
    else:
      print("That is not a recognized entry please try again: ")
      print("")
      self.saveLoadMenu()
  
  def clearMenu(self):
    print("Welcome to the clear menu ")
    print("1. Update time month to 0 ")
    print("2. Update time year to 0 ")
    print("3. Clear the saved lot database ")
    print("8. Go back to the main menu ")
    response = input("What would you like to do? ")
    if response == "1":
      self.clearTimeMonth()
      print("")
      self.clearMenu()
    elif response == "2":
      self.clearTimeYear()
      print("")
      self.clearMenu()
    elif response == "3":
      try:
        self.clearDatabase()
        print("")
        print("Database has been cleared ")
        print("")
      except:
        print("Database does not exist")
      self.saveLoadMenu()
      self.clearMenu()
    elif response == "8":
      self.menu()
    else:
      print("That is not a recognized entry please try again: ")
      print("")
      self.clearMenu()
  
  def infoMenu(self):
    print("Welcome to the info retrieval menu ")
    print("1. Get elevation information ")
    print("2. Get group information ")
    print("3. Get row information ")
    print("4. Get spot information ")
    print("5. Show all spots in the parking lot ")
    print("6. Greatest spots menu ")
    print("8. Go back to the main menu ")
    response = input("What would you like to do? ")
    if response == "1":
      print("")
      self.elevationMenu()
    elif response == "2":
      print("")
      self.groupMenu()
    elif response == "3":
      print("")
      self.rowMenu()
    elif response == "4":
      print("")
      self.spotMenu()
    elif response == "5":
      print("")
      self.showParkingSpot()
      print("")
      self.infoMenu()
    elif response == "6":
      print("")
      self.greatestMenu()
    elif response == "8":
      print("")
      self.menu()
    else:
      print("That is not a recognized entry please try again: ")
      print("")
      self.infoMenu()

  def takeOpenMenu(self):
    print("Welcome to the take/open menu ")
    print("1. Take a parking spot ")
    print("2. Open a parking spot ")
    print("3. Take a spot with a name ")
    print("4. Open a spot with a name ")
    print("8. Go back to the main menu ")
    response = input("What would you like to do? ")
    if response == "1":
      elevation = input("What is the elevation number? ")
      elevation = str(elevation)
      group = input("What is the group number? ")
      group = str(group)
      row = input("What is the row number? ")
      row = str(row)
      spot = input("What is the spot number? ")
      spot = str(spot)
      fullName = elevation + "-" + group + "-" + row + "-" + spot
      try:
        spot = self.findName(fullName)
        spot.isTaken()
        print("")
        print("spot:" + fullName + " is now taken")
        print("")
      except:
        print("")
        print("That spot does not exist")
        print("")
        self.takeOpenMenu()
      self.takeOpenMenu()
    elif response == "2":
      elevation = input("What is the elevation number? ")
      elevation = str(elevation)
      group = input("What is the group number? ")
      group = str(group)
      row = input("What is the row number? ")
      row = str(row)
      spot = input("What is the spot number? ")
      spot = str(spot)
      fullName = elevation + "-" + group + "-" + row + "-" + spot
      print("")
      try:
        spot = self.findName(fullName)
        spot.isNowOpen()
        print("")
        print("spot:" + fullName + " is now open")
        print("")
      except:
        print("")
        print("That spot does not exist")
        print("")
        self.takeOpenMenu()
      self.takeOpenMenu()
    elif response == "3":
      name = input("What is the full name? ")
      fullName = str(name)
      try:
        spot = self.findName(fullName)
        spot.isTaken()
        print("")
        print("spot:" + fullName + " is now taken")
        print("")
      except:
        print("")
        print("That spot does not exist")
        print("")
        self.takeOpenMenu()
      self.takeOpenMenu()
    elif response == "4":
      name = input("What is the full name? ")
      fullName = str(name)
      try:
        spot = self.findName(fullName)
        spot.isNowOpen()
        print("")
        print("spot:" + fullName + " is now open")
        print("")
      except:
        print("")
        print("That spot does not exist")
        print("")
        self.takeOpenMenu()
      self.takeOpenMenu()
    elif response == "8":
      print("")
      self.menu()
    else:
      print("That is not a recognized entry please try again: ")
      print("")
      self.takeOpenMenu()

  def effMenu(self):
    print("Welcome to the take/open menu ")
    print("1. Get a parking spots efficiency for the month ")
    print("2. Get a parking spots efficiency for the year ")
    print("3. Get a parking spots efficiency for the month, by name ")
    print("4. Get a parking spots efficiency for the year, by name ")
    print("8. Go back to the main menu ")
    response = input("What would you like to do? ")
    if response == "1":
      elevation = input("What is the elevation number? ")
      elevation = str(elevation)
      group = input("What is the group number? ")
      group = str(group)
      row = input("What is the row number? ")
      row = str(row)
      spot = input("What is the spot number? ")
      spot = str(spot)
      fullName = elevation + "-" + group + "-" + row + "-" + spot
      try:
        spot = self.findName(fullName)
        print("")
        print("Spot month effciecny: " + spot.getMonthEfficiency())
        print("")
      except:
        print("")
        print("That spot does not exist")
        print("")
        self.effMenu()
      self.effMenu()
    elif response == "2":
      elevation = input("What is the elevation number? ")
      elevation = str(elevation)
      group = input("What is the group number? ")
      group = str(group)
      row = input("What is the row number? ")
      row = str(row)
      spot = input("What is the spot number? ")
      spot = str(spot)
      fullName = elevation + "-" + group + "-" + row + "-" + spot
      try:
        spot = self.findName(fullName)
        print("")
        print("Spot year effciecny: " + spot.getYearEfficiency())
        print("")
      except:
        print("")
        print("That spot does not exist")
        print("")
        self.effMenu()
      self.effMenu()
    elif response == "3":
      name = input("What is the full name? ")
      fullName = str(name)
      try:
        spot = self.findName(fullName)
        print("")
        print("Spot month effciecny: " + spot.getMonthEfficiency())
        print("")
      except:
        print("")
        print("That spot does not exist")
        print("")
        self.effMenu()
      self.effMenu()
    elif response == "4":
      name = input("What is the full name? ")
      fullName = str(name)
      try:
        spot = self.findName(fullName)
        print("")
        print("Spot year effciecny: " + spot.getYearEfficiency())
        print("")
      except:
        print("")
        print("That spot does not exist")
        print("")
        self.effMenu()
      self.effMenu()
    elif response == "8":
      print("")
      self.menu()
    else:
      print("That is not a recognized entry please try again: ")
      print("")
      self.effMenu()
    
  def menu(self):
    print("Welcome to the main menu ")
    print("1. Create a spot ")
    print("2. Create a row ")
    print("3. Get information about the lot ")
    print("4. Clear information menu ")
    print("5. Save/Load menu ")
    print("6. Take/Open spot menu ")
    print("7. Get efficiency menu ")
    print("To quit type 'QUIT' ")
    response = input("What would you like to do? ")
    if response == "1":
      print("")
      p1 = Point("newName")
      p1.setSpotName()
      self.list.append(p1)
      print("")
      self.menu()
    elif response == "2":
      print("")
      self.CreateRow()
      print("")
      self.menu()
    elif response == "3":
      print("")
      self.infoMenu()
    elif response == "4":
      print("")
      self.clearMenu()
    elif response == "5":
      print("")
      self.saveLoadMenu()
    elif response == "6":
      print("")
      self.takeOpenMenu()
    elif response == "7":
      print("")
      self.effMenu()
    elif response == "QUIT":
      print("")
      sys.exit(0)
    else:
      print("That is not a recognized entry please try again: ")
      print("")
      self.menu()

  def saveSpots(self):
    connection = sqlite3.connect("parkingLot")
    connection.execute("CREATE TABLE IF NOT EXISTS parkingLot (id INTEGER PRIMARY KEY, name STRING, timeTaken INTEGER, timeMonth INTEGER, timeYear INTEGER, efficiencyMonth INTEGER, efficiencyYear INTEGER, isOpen BOOLEAN, startTime INTEGER);")
      
    insert_query = ("INSERT INTO parkingLot (id,name,timeTaken,timeMonth,timeYear,efficiencyMonth,efficiencyYear,isOpen, startTime)" 
                      "VALUES (:id,:name,:timeTaken,:timeMonth,:timeYear,:efficiencyMonth,:efficiencyYear,:isOpen,:startTime);")
    for x in range(len(self.list)):
      lot_parameters = {
          'id' : x,
          'name': self.list[x].getName(),
          'timeTaken': self.list[x].getTimeTaken(),
          'timeMonth': self.list[x].getTimeMonth(),
          'timeYear' : self.list[x].getTimeYear(),
          'efficiencyMonth' : self.list[x].getMonthEfficiency(),
          'efficiencyYear' : self.list[x].getYearEfficiency(),
          'isOpen' : self.list[x].getIsOpen(),
          'startTime' : self.list[x].getStartTime()
        }
      connection.execute(insert_query, lot_parameters)
    connection.commit()

  def getSpotInfo(self):
    connection = sqlite3.connect("parkingLot")
    cursor_object = connection.execute("SELECT * FROM parkingLot")
    records = cursor_object.fetchall()
    for row in records:
        print("id =", row[0], )
        print("Name =", row[1])
        print("timeTaken =", row[2])
        print("timeMonth =", row[3])
        print("timeYear =", row[4])
        print("efficiencyMonth =", row[5])
        print("efficiencyYear =", row[6])
        print("isOpen =", row[7])
        print("startTime =", row[8])
        print("")
        p1 = Point(row[1])
        p1.setTimeTaken(row[2])
        p1.setTimeMonth(row[3])
        p1.setTimeYear(row[4])
        p1.setMonthEfficiency(row[5])
        p1.setYearEfficiency(row[6])
        p1.setIsOpen(row[7])
        p1.setStartTime(row[7])
        self.addParkingSpot(p1)
      
    connection.close()

  def clearDatabase(self):
    connection = sqlite3.connect("parkingLot")
    dropQuery = "DROP TABLE parkingLot"
    connection.execute(dropQuery)
    connection.close()

""" 
p1 = Point("1-3-1-21")
p2 = Point("1-2-1-22")
p3 = Point("1-5-2-22")
p4 = Point("1-5-2-25")
p5 = Point("1-5-1-26")
p6 = Point("1-6-2-23")

p1.setStartTime(-500)
p1.isNowOpen()




l1.addParkingSpot(p1)
l1.addParkingSpot(p6)
l1.addParkingSpot(p5)
l1.addParkingSpot(p2)
l1.addParkingSpot(p3)
l1.addParkingSpot(p4)
"""

l1 = Lot("teddy")
print(" ")
l1.menu()
