import random


def responses_handler(msg):
    msg = msg.lower()
    greetings = ["hi", "hello", "hey"]

    if msg in greetings:
        return "Hello!"

    if msg == "roll":
        return random.randint(1, 6)
