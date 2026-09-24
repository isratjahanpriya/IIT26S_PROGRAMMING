print("Program starting.")
print("Estimate how many minutes you spent on programming...")
T1 = int( input("A1_T1:"))
T2 = int( input("A1_T2:"))
T3 = int(input("A1_T3:"))
T4 = int(input("A1_T4:"))
T5 = int(input("A1_T5:"))
T6 = int(input("A1_T6:"))
T7 = int(input("A1_T7:"))
sum = T1+T2+T3+T4+T5+T6+T7
print(f"In total you spent {sum} minutes on programming.")
average = sum/7
print(f"Average per task was {round (average,2)}min and same rounded to the nearest integer {round(average)} min.")
print("Program ending.")
