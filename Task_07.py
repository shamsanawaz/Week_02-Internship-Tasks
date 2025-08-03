while True:
   try:
       number = int(input("Please enter an integer:"))
       print("You enterd:",number)
       break
   except ValueError:
       print("Invaid input! Please enter a valid integer .")
           