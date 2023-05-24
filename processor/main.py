#!/usr/bin/env python3
"""Methods for fight"""
from person import Person


# Fight - Need to find way to print entire conversation.
def fight(one_who_is_making_statement: Person,
          one_who_might_get_triggered: Person, return_string: str) -> str:
    """The fight itself"""
    # print statement.
    statement: str = one_who_is_making_statement.make_statement()
    return_string += statement + "<br>"
    return_string += "Waiting for reaction... <br>"
    return_string += "<br>"
    # If statement == 'I give up', return.
    if statement == 'I give up':
        return return_string + 'Game Over'
    # print reaction.
    is_triggered: bool = one_who_might_get_triggered.triggered()
    success: bool = one_who_is_making_statement.triggers_other_side(other_reaction=is_triggered)
    if success:
        return_string += "Opponent is Triggered <br>"
    else:
        return_string += "Opponent is not Triggered <br>"
    return_string += "Waiting for statement... <br>"
    return_string += "<br>"
    # Switch between people making statements.
    return fight(one_who_is_making_statement=one_who_might_get_triggered,
                 one_who_might_get_triggered=one_who_is_making_statement,
                 return_string=return_string)
