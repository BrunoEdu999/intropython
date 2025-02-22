def maior_primo(numero):
    for i in range(numero, 1, -1):
        primo = True
        for n in range(2, i):
            if i % n == 0:
                primo = False
        if primo:
            return i
if __name__ == "__main__":
    print(maior_primo(100))
    print(maior_primo(7))