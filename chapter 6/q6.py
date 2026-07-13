marks = []
while (1>0):
        a = int (input("enter a marks or enter stop to end the input"))
        if (a == "stop" ):
                break
        marks.append(a)
percent = (sum(marks)/len(marks)*100)*100
if percent < 90 and percent >= 100:
     print("Ex") 
elif percent<80 and percent>= 90:
       print("A")
elif percent < 70 and percent>= 80:
     print("B")
elif percent <60 and percent >= 70:
       print("C")
elif percent < 50 and percent >= 60:
       print("D")
else:
       print("F")
                                  
