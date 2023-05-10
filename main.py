#!/usr/bin/env python3
from person import Person, Insults, Reaction


def main():
    # Input details for player one
    print("Player 1: \n")
    person_one: Person = make_person()
    # Input details for player two
    print("Player 2: \n")
    person_two: Person = make_person()
    # Start fight and continue until one gives up.
    print(fight(one_who_is_making_statement=person_one, one_who_might_get_triggered=person_two))


# Creates person by getting details.
def make_person() -> Person:
    print("Input details for person: \n")
    # Gets details.
    gender: str = input('Gender: \n')
    pronouns: str = input('Pronouns: \n')
    age: int = int(input('Age: \n'))
    skin_color: str = input('Skin Color: \n')
    political_ideology: str = input('Political Ideology: \n')
    # Puts them into an object.
    our_person: Person = Person(gender=gender, pronouns=pronouns, age=age, skin_color=skin_color,
                                political_ideology=political_ideology)
    # Returns the person object.
    return our_person


# Fight
def fight(one_who_is_making_statement: Person, one_who_might_get_triggered: Person) -> str:
    # print statement.
    statement: str = one_who_is_making_statement.make_statement()
    print(statement)
    print("Waiting for reaction...")
    print("")
    # If statement == 'I give up', return.
    if statement == 'I give up':
        return 'Game Over'
    # print reaction.
    is_triggered: bool = one_who_might_get_triggered.triggered()
    success: bool = one_who_is_making_statement.triggers_other_side(other_reaction=is_triggered)
    if success:
        print("Oponent is Triggered")
    else:
        print("Oponent is not Triggered")
    print("Waiting for statement...")
    print("")
    # Switch between people making statements.
    return fight(one_who_is_making_statement=one_who_might_get_triggered,
                 one_who_might_get_triggered=one_who_is_making_statement)


if __name__ == '__main__':
    main()
