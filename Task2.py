N = int(input("Put number of students:"))
K = int(input("Put number of apples:"))

z = K // N #This will give number of apples for each student
y = K % N #This will give number of apples in basket
print("Apples for each student", z)
print("Apples in a basket", y)