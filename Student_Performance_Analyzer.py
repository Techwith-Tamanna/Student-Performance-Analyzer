import numpy as np
marks = np.array([26, 52, 48, 63, 72, 64, 45, 84, 82, 93, 55, 70, 84, 65,78,45,92,67,31,88,54])
print("- - - - STUDENT PERFORMANCE ANALYZER - - - -")

avg = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)

print(avg, "was the Average marks scored by students.")
print(highest, "was the Highest marks scored by students.")
print(lowest, "was the Lowest marks scored by students.")

print("\n- - - -Detailed Report- - - -")
excellent = 0
good = 0
average = 0
poor = 0

for i in marks:
    if i>=80:
        print(i, ": Excellent")
        excellent=+1
    elif  i>=65:
        print(i, ": Good")
        good+=1
    elif i>=33:
        print(i, ": Average")
        average+=1
    else:
        print(i, ": Poor")
        poor+=1
print("\n- - - -Summary- - - -")

print("Excellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Essential Repeat:", poor)


print("\n- - - -End of the Analysis- - - -")

