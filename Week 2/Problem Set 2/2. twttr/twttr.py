def main():
    # Initialize a string with user input
    phrase = input("Input: ")

    # Split the input string into a list of words
    words = phrase.split()

    # Iterate through each word and remove all vowels
    for i in range(len(words)):
        words[i] = remove_vowels(words[i])

    # Join the modified words back into a single string
    print(f"Output: {' '.join(words)}")


# Function to remove vowels from a word
def remove_vowels(s):
    for vowel in "aeiouAEIOU":
        s = s.replace(vowel, "")
    return s

main()
