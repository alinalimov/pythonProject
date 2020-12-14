#birth_year = input("enter birth year:")
#import datetime
#now = datetime.datetime.now()
#age = now.year - int(birth_year)
#print (age)
#zodiac_sign = input("what month were you born?")
month = input("what month were you born?")
day = input("on what day were you born?")
if int(month) == 1 and int(day) < 20:
    print ("capricorn")
elif int(month) == 1 and int(day) > 19:
    print ("aquarius")
elif int(month) == 2 and int(day) < 19:
        print ("aquarius")
elif int(month) == 3 and int(day) > 20:
    print ("pices")
elif int(month) == 3 and int(day) < 20:
    print ("Pices")
elif int(month) == 4:
    print("aries")
elif int(month) == 5:
    print("Taurus")
elif int(month) == 6:
    print ("Gemini")
elif int(month) == 7:
    print ("cancer")
elif int(month) == 8:
    print("leo")
elif int(month) == 9:
    print ("virgo")
elif int(month) == 10:
    print("libra")
elif int(month) == 11:
    print("scorpio")
elif int(month) == 12:
    print ("Sagittarius")
else:
    print("something else")


