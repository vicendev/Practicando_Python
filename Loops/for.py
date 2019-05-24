for number in range(1,21):
    print(number)
print("--------")

for number in range(1,21,2):
    print(number)
print("--------")

for number in [1,2,3,4]:
    print(number)
print("--------")

for letter in "abcd":
    print(letter)
print("--------")

vowels = 0
consonants = 0

for letter in "paralelepipedo":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants +1 

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))
print("--------")

