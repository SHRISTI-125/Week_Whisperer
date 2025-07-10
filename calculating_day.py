from days import day;

#C=int(input("Enter Date :: "))
#B=input("Enter Month :: ")
#A=int(input("Enter Years :: "))
entered_date = input("Enter date like 20-05-1989 between 1700 to 2200 : ")
entered_date=entered_date.replace("-","")
entered_date=entered_date.replace("/","")
entered_date=entered_date.replace(".","")
entered_date=entered_date.replace("th","")
date = int(entered_date[:2])
month = int(entered_date[2:4])
year = int(entered_date[4:8])

#print(date," ",month," ",year)

day(date,month,year)

