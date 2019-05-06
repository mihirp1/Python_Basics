import calendar
#import datetime

def day():
 days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
 MM, DD, YYYY = list(map(int,input().split(" ")))
 index = int(calendar.weekday(YYYY,MM,DD))  # what I look for
 print(days[index])   
if __name__ == "__main__":
    day()
