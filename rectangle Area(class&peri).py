class rectangle:
    def getdata(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):    
        print("Area of rectangle:", self.length * self.breadth)

    def perimeter(self):
        print("Perimeter of rectangle:", 2 * (self.length + self.breadth))


# Main program
l = float(input("Enter a length: "))
b = float(input("Enter a breadth: "))

obj = rectangle()
obj.getdata(l, b)

ch = 0
while ch != 3:
    print("\n*------ Menu ------*")
    print("1. Area")
    print("2. Perimeter")
    print("3. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        obj.area()
    elif ch == 2:
        obj.perimeter()
    elif ch == 3:
        print("Exiting Program...")
    else:
        print("Invalid choice!!")
