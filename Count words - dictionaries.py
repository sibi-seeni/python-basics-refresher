#   A program to find word frequency from phrases
#
#   by: Sibi Seenivasan

def build_dictionary(words):
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict

def main():
    print("\nWelcome to the word frequency program!")
    print("\n=====================================\n")

    while True:
        user_input = input("Enter words separated by space: ")
        words_list = user_input.split()
        
        word_freq = build_dictionary(words_list)
        
        sorted_keys = sorted(word_freq.keys())
        print(f"Sorted keys: {sorted_keys}\n")
        
        print("Let's print the frequency of each word!")
        for word in sorted_keys:
            print(f"{word}: {word_freq[word]}")
        
        repeat = input("\nRepeat the program> (y or n)? ").strip().lower()
        print("\n=====================================\n")
        if repeat != 'y':
            print("\nThank you! Goodbye!")
            break

if __name__ == "__main__":
    main()