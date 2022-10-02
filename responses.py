import random
from responses_list import greetings, quotes, jokes


def responses_handler(msg):
    msg = msg.lower()

    if msg in greetings:
        return greetings[msg]

    match msg:
        case "roll":
            return random.randint(1, 6)
        case "qoute":
            return random.choice(quotes)
        case "joke":
            return random.choice(jokes)
