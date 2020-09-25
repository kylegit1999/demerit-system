speed = int(input("what was your average speed?"))
allowed_speed= int(input("what was your allowed speed"))
if speed > allowed_speed:
    merit=(speed-allowed_speed)//5
    print (merit, "demerit points")
    if merit>=12:
        print("Time to go to jail")
