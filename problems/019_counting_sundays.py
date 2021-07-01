class Date():
    def __init__(self):
        self.day = 1
        self.month = 0
        self.year = 1900
        self.dayofweek = 1

    def nextSunday(self):
        self.day += (7 - self.dayofweek)
        self.calcMonth()
        self.calcYear()
        self.dayofweek = 0

    def calcMonth(self):
        daysInMonth = [31, 29 if self.isLeapYear() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.day > daysInMonth[self.month]:
            self.day -= daysInMonth[self.month]
            self.month += 1

    def calcYear(self):
        if self.month >= 12:
            self.month = 0
            self.year += 1

    def isLeapYear(self):
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def __str__(self):
        return "%s/%s/%s" % (self.day, self.month+1,self.year)

def main():
    date = Date()

    sundays_counted = 0
    while date.year <= 2000:
        date.nextSunday()
        if date.year < 1901:
            continue
        if date.day == 1:
            sundays_counted += 1

    print(sundays_counted)

if __name__ == "__main__":
    main()