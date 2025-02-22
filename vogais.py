vowels = ["a", "e", "i", "o", "u"]
def vogal(letter):
    return letter.lower() in vowels

if __name__ == "__main__":
    print(vogal("a"))
    print(vogal("b"))
    print(vogal("E"))