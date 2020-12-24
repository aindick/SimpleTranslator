def translate(word):
    translation = ""
    # Loop through each letter in "word" and change the vowels to b's#
    for letter in word:
        if letter in "AEIOUaeiou":
            translation = translation + "b"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))