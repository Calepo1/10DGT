while True: #Starting loop
    type = input("----- Instructions ----- \nType - \nInteger/Int\nText/Txt/T\nImage/Img/P\nXXX/Exit - \nType: ").lower() #Asking for type
    if type == "xxx" or type == "exit": #If exit
        print("You have chosen to exit.\nThank you for using the bit calculator.")
        break #Exit
    if type == "integer" or type == "int": #If integer
        print("You have chosen an integer. ");integer = int(input("Type integer: ")) #Ask integer
        if integer <= 0: #If not positve
            print("Integer must be bigger than 0") #Loop
        binary = bin(integer) #Calculate binary
        print(f"The binary for this integer is {binary} and it needs {len(bin(integer))} bits") #Bit calculate and print
    elif type == "text" or type == "txt" or type == "t": #If text
        text = input("Enter text: ") #Ask text
        print(f"'{text}' needs {len(text)*8} bits") #Bit calculate and print
    elif type == "image" or type == "img" or type == "p": #If image
        width = float(input("Width in pixels: ")) #Ask for width
        if width <= 0: #If not positive
            print("Width must be bigger than 0") #loop
        length = float(input("Length in pixels: ")) #Asking for length
        if length <= 0: #If not pasitive
            print("Length must be bigger than 0") #loop
        pixels = length*width ; print(f"The ammount of bits needed for your {pixels} pixel images is {pixels*24}")
    elif type not in  ["integer" , "int" , "text" , "t" , "txt" , "image" , "img" , "p"]:
        print("Please enter integer, text or image.") 