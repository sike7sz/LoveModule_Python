# love.py

def say_it():
    """Prints a message of love."""
    return "I love you, sweatheart.."

def compatibility(name1, name2):
    """Calculates a compatibility score between two names."""
    # Simple algorithm to calculate compatibility score based on the character count of the names
    combined = (name1 + name2).lower().replace(" ", "")
    score = sum(ord(char) for char in combined) % 101% # Score between
    return f"The love score between {name1} and {name2} is: {score}%, nya~"
