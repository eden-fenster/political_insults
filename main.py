#!/usr/bin/env python3
from person import Person, Insults, Reaction


def main():
    # Input details for player one
    person_one: Person = make_person()
    # Input details for player two
    person_two: Person = make_person()
    # Start fight and continue until one gives up.
    print(fight(who_is_making_statement=person_one, who_might_get_triggered=person_two))


# Creates person by getting details.
def make_person() -> Person:
    print("Input details for person: \n")
    gender: str = input('Gender: \n')
    pronouns: str = input('Pronouns: \n')
    age: int = int(input('Age: \n'))
    skin_color: str = input('Skin Color: \n')
    political_ideology: str = input('Political Ideology: \n')
    our_person: Person = Person(gender=gender, pronouns=pronouns, age=age, skin_color=skin_color,
                                political_ideology=political_ideology)
    return our_person


# Fight
def fight(who_is_making_statement: Person, who_might_get_triggered: Person) -> str:
    # print statement.
    # If statement == 'I give up', return.
    # print reaction.
    # If reaction == 'I give up', return.
    # Switch between people making statements.
    pass


if __name__ == '__main__':
    main()
