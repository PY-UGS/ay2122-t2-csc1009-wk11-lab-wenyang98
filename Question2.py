class ClockTime:
    #constructors
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
    
    #Sets the hours attribute
    def setHours(self, hour):
        self.hour = hour

    #Sets the minutes attribute
    def setMinutes(self, minute):
        self.minute = minute
    
    #Sets the seconds attribute
    def setSeconds(self, second):
        self.second = second
    
    #Sets the time for all attribute
    def setTime(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    # returns the time in hours:minutes:seconds format
    def showTime(self):
        return str("Time: {:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second))

hour = -1 #defining hour
minute = -1 #defining minute
second = -1 # defining second

# ask userinput for hours
# Checks if number of hours is 0 - 59
while hour > 23 or hour < 0:
        hour = int(input("Enter hour: "))
        if hour > 23 or hour < 0:
            print("Invalid input for hour")

# ask userinput for minutes
# Checks if number of minutes is 0 - 59
while minute > 59 or minute < 0:
        minute = int(input("Enter minute: "))
        if minute > 59 or minute < 0:
            print("Invalid input for minute")

# ask userinput for seconds 
# Checks if number of seconds is 0 - 59
while second > 59 or second < 0:
        second = int(input("Enter second: "))
        if second > 59 or second < 0:
            print("Invalid input for number of second")

#creates clock object
Clock = ClockTime()
#sets the time
Clock.setTime(hour, minute, second)
#printing the time
print(Clock.showTime())