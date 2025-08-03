import random
import datetime
def main():
    # Generate a random number betwwen 1 and 100
    num = random.randint(1,100)
    print("Random number:",num)
    
    # Get current date and time
    now = datetime.datetime.now()
    print("Current date and time:",now)
main()    