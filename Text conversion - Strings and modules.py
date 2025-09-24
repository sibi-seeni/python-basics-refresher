#   A program to translate English to pig Latin
#   Program demonstrates string manipulation and using funtions & modules
#
#   by: Sibi Seenivasan

from pig_latin import to_pig_latin

def main():
    # display a welcome message
    print("Pig Latin Translator\n")

    loop = "y"
    # Start the while loop
    while loop.lower() == "y":
        # Get input
        text = input("Enter text (Separated by space) : ").strip()

        # Declaring empty string to store output
        pig_text = '' 

        # Normalizing the string by keeping case and characters uniform
        formatted_text = text.lower()
        for char in "-().":
            formatted_text = formatted_text.replace(char, "")
        
        # Splitting and passing to the module word by word
        ylist = formatted_text.split()
        for i in range(len(ylist)):
            pig_text += to_pig_latin(ylist[i])
            pig_text += ' '

        # Output
        print(f"\nEnglish\t\t{formatted_text}")
        print(f"Pig Latin:\t{pig_text}")
        print()
        loop = input("Continue? (y/n): ")
        print()
    
    print("Bye!")

if __name__ == "__main__":
    main() 