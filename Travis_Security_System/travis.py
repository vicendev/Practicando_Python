known_user = ["Alice","Bob", "Claire", "Dan","Emma", "Fred","Georgie", "Harry"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_user:
        print("Hello {}".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()
        if remove == "y":
            known_user.remove(name)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
    else:
        print("Hmmmm I don't think i have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_user.append(name)
        elif add_me == "n":
            print("No worries see you around!")
