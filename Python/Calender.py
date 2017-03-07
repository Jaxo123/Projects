from time import *

username = "Jax Oliver"
calender = {}

def welcome():
  print "Welcome, %s, the calender will open shortly." % (username)
  print "Today's date: " + strftime("%A %m %d, %Y")
  sleep(1)
  print strftime("%H, %M, %S")
  sleep(1)
  print "What would you like to do?"

def start_calender():
  welcome()
  start = True
  while start is True:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit:")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calender.keys()) < 1:
        "Your calender is empty."
      else:
        print calender
    elif user_choice == 'U':
      date = raw_input("What date")
      update = raw_input("Enter the update:")
      calender[date] = update
      print "Your update was a success."
    elif user_choice == 'A':
      event = raw_input("Enter event:")
      date = raw_input("Enter date (MM/DD/YYYY)")
      if len(date) > 10 or int(date[6:11] < strftime("%Y")):
        print "Specified date is invalid."
        try_again = raw_input("Try Again? ")
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calender[date] = event
        print "Event was added succesfully."
    elif user_choice == "D":
      if len(calender.keys()) < 1:
        print "There are no dates to delete."
      else:
        event = raw_input("What event?")
        for date in calender.keys():
          if event == calender[date]:
            del calender[date]
            print "Event succesfully deleted."
            print calender
          else:
            print "Specified event is invalid"
    elif user_choice == "X":
      start = False
    else:
      print "Specified command is invalid"
      start = False
start_calender()
