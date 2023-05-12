#writing a program to calculate the area of a triangle

#Title of the Program
print("\nProgram to calculate the area of a triangle \n")

#Ask user to enter the base as integer
base = int(input("Enter the base(cm): "))

#prints the base that the user has entered (notice the type casting)
print("\nYou entered: " + str(base) + "cms\n")

#Ask user to enter the height as string
height = int(input("Enter the base(cm): "))

#prints the height as string (notice the type casting)
print("\nYou entered: " + str(height) + "cms\n")

#function to calculate the area
area = ((base * height) / 2)

#Prints the result as string (notice the type casting)
print("Area = " + str(area) + "cm\u00b2 \n")

