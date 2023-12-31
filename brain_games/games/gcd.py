from random import randint

import math


MIN_VALUE_GCD = 0
MAX_VALUE_GCD = 100
QUESTION = 'Find the greatest common divisor of given numbers.'


def initialize_correct_answer():
    """
    Correct answet for even gcd
    """
    number1 = randint(MIN_VALUE_GCD, MAX_VALUE_GCD)
    number2 = randint(MIN_VALUE_GCD, MAX_VALUE_GCD)

    question = f'{number1} {number2}'

    return (question, math.gcd(number1, number2))
