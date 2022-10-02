import random
from responses_list import quotes, jokes, rockpaperscissor


def responses_handler(msg):
    msg = msg.lower()

    if msg == "!help":
        return '`You can type some greetings: like hello, hi, and hey. \
Also, "qoute", "joke", and also "roll" to roll a dice`'

    match msg:
        case "roll" | "dice":
            return random.randint(1, 6)
        case "quote" | "quotes":
            return random.choice(quotes)
        case "joke" | "jokes":
            return random.choice(jokes)
        case "rock" | "paper" | "scissor":
            com = random.choice(rockpaperscissor)
            if msg == "rock":
                match com:
                    case "Rock":
                        return "Draw!"
                    case "Paper":
                        return "You loss!"
                    case "Scissor":
                        return "You won!"
            elif msg == "paper":
                match com:
                    case "Rock":
                        return "You won!"
                    case "Paper":
                        return "Draw!"
                    case "Scissor":
                        return "You loss!"
            else:
                match com:
                    case "Rock":
                        return "You loss!"
                    case "Paper":
                        return "You won!"
                    case "Scissor":
                        return "Draw!"
