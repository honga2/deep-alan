from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Cat got ya tongue?'
    else:
        # return 'Deep Alan is in progress... Please check in later.'
        return '0_0'

