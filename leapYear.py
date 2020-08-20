#This program determines if a year is a leap or a comman year
year = int(input("Enter a year: "))

#The requirement for a leap year is that it must be divisable by 4
commanYear = year % 4
#if the year is under 1582 it is not within of the Greforian calendar period
if year < 1582:
    print("Not within the Gregorian calendar period")
#if the year does not this requerement is is not a leap year thus it's a comman year
elif commanYear != 0:
        print ("comman year")
#will be the default output for everyother year
else:
    print("leap year")
