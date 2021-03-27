
def bark():
    return "Woof!"


def meow():
    return "Meow"


def func(pet):
    if pet == ' ' or pet == None:
        return "Please enter correct input"

    try:
        if pet.lower() == 'dog':
            return bark()
        elif pet.lower() == 'cat':
            return meow()
    except:
        return "Please enter correct input"


if __name__ =='__main__':
    pet = input("Enter type of pet (Dog/Cat): ")

    print(func(pet))




