def calculator():
    while True: #Starting loop
        try:
            width = float(input("Width: "))
            if width <= 0: # Asking for width
                print("Width must be bigger than 0")
                continue 
            height = float(input("Height: ")) # Asking for height
            if height <= 0: 
                print("Height must be bigger than 0")
                continue

            area = height*width # Calculating area
            perimeter = 2*(height+width) # Calculating perimeter
            print(f"The area is {area} square units") # Printing area
            print(f"The perimeter is {perimeter} units") # Printing perimeter

            more = input("Would you like to calculate another? ").lower()
            if more != 'yes':
                break
        except ValueError:
            print("Invalid input, try again.")

calculator()



            
    
    