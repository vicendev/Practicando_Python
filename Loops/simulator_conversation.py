from random import choice

questions = ["Why the water not have color?: ", "Why we need food?: ", "Why i can't understand the dogs?: "]

questions = choice(questions)
answer = input(questions).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("Oh... Okay")