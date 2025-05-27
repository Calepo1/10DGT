def calculator():
    while True: # Starting loop
        try:
            width = float(input("Width: ")) # Asking for width
            if width <= 0: 
                print("Width must be bigger than 0")
                continue 
            length = float(input("Length: ")) # Asking for length
            if length <= 0: 
                print("Length must be bigger than 0")
                continue
            cost_per_m = float(input("Cost per meter: ")) # Asking for the Cost per meter
            if cost_per_m <= 0:
                print("Cost per meter must be bigger than 0")
                continue

            perimeter = 2*(width+length) # Calculating the perimeter
            cost = perimeter*cost_per_m # Calculating the cost
            print(f"The cost to fence your {perimeter}m perimeter rectangular area is ${cost}") # Printing the cost

            another = (input("Would you like to calculate another? (Enter = yes, any charactor to quit): ")) # Asking for more
            if another != '':
                print("Thank you for using the calculator.")
                break

        except ValueError:
            print("Invalid input, try again.")
                
calculator()