import sys

principal = 1000
rate = 5
time = 1

if len(sys.argv) == 4:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
    print("User provided input values:")
else:
    print("No parameters given using default values:")

# Simple interest
simple_interest = (principal * rate * time) / 100

#output
print("Principal:", principal)
print("Rate:", rate)
print("Time:", time)
print("Simple Interest:", simple_interest)
