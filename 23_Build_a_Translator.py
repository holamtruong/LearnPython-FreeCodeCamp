# Dog language

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "naidom":
            if letter.isupper():
                translation = translation + "Gau"
            else:
                translation = translation + "gau"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
