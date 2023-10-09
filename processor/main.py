#!/usr/bin/env python3
"""Methods for fight"""
import logging
from person import Person

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# pylint: disable=consider-using-f-string
# pylint: disable=logging-fstring-interpolation


# Fight - Need to find way to print entire conversation.
def fight(one_who_is_making_statement: Person,
          one_who_might_get_triggered: Person, return_string: str) -> str:
    """The fight itself"""
    logging.debug(f"Our contestants are:\n {one_who_is_making_statement}"
                  f" \n {one_who_might_get_triggered}")
    # print statement.
    statement: str = one_who_is_making_statement.make_statement()
    logging.debug(f"statement is -> {statement}")
    return_string += statement + "<br>"
    return_string += "Waiting for reaction... <br>"
    # If statement == 'I give up', return.
    if statement == 'I give up':
        return return_string + 'Game Over'
    # print reaction.
    is_triggered: bool = one_who_might_get_triggered.triggered()
    logging.debug(f"Is other side triggered ? \n {is_triggered}")
    success: bool = one_who_is_making_statement.triggers_other_side(other_reaction=is_triggered)
    logging.debug(f"Was triggering a success ? \n {success}")
    if success:
        return_string += "Opponent is Triggered <br>"
    else:
        return_string += "Opponent is not Triggered <br>"
    return_string += "Waiting for statement... <br>"
    # Switch between people making statements.
    return fight(one_who_is_making_statement=one_who_might_get_triggered,
                 one_who_might_get_triggered=one_who_is_making_statement,
                 return_string=return_string)
