def day(C,B,A):
  e=0
  a=A%100 #finding last two digit
  y=a//4 #number which is divisible by 4
  y=y+a #adding divisible number with original divisor
  y1=y%7 #remainder after calculation above, code1 for year
  if A>=1700 and A<1800:#predefined code; code2 for year
    c=4
  if A>=1800 and A<1900:
    c=2
  if A>=1900 and A<2000:
    c=0
  if A>=2000 and A<2100:
    c=6
  if A>=2100 and A<2200:
    c=4
  year=y1+c #adding both code1+code2 in year
  # Now calculating month
  if B=="1" or B=="January":
    e=1
    if a%4==0:#if leap year
      e=e-1
  if B=="2" or B=="February":
    e=4
    if a%4==0:
      e=e-1
  if B=="3" or B=="March" or B=="November" or B=="11":
    e=4
  if B=="4" or B=="April" or B=="7" or B=="July":
    e=0
  if B=="5" or B=="May":
    e=2
  if B=="6" or B=="June":
    e=5
  if B=="8" or B=="August":
    e=3
  if B=="9" or B=="September" or B=="December" or B=="12":
    e=6
  if B=="10" or B=="October":
    e=1
  Calc=year+e+C #adding all year+month+day
  #Now it's time for days
  G=Calc%7 #remainder for days
  print("\n")
  if G==1:
    print('\033[95m{}\033[95m'.format("Sunday\nIt's Sunday having Funday\n "))
  elif G==2:
    print('\033[36m{}\033[36m'.format("Monday"))
  elif G==3:
    print('\033[91m{}\033[91m'.format("Tuesday"))
  elif G==4:
    print('\033[33m{}\033[33m'.format("Wednesday"))
  elif G==5:
    print('\033[93m{}\033[93m'.format("Thrusday"))
  elif G==6:
    print('\033[94m{}\033[95m'.format("Friday"))
  elif G==7 or G==0:
    print('\033[96m{}\033[96m'.format("Saturday"))
  #print("\n\n")
  print('\033[32m{}\033[32m'.format("So it's all about Day\nThis program ends here"))
  print("\n")
  print('\033[95m{}\033[95m'.format("Thank you"))
  print('\033[0m')
