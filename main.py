def letterPos(w, letter):

    for i in range(0, len(w)):
        if letter == w[i]:
            return i + 1

    return 0


print(letterPos("sunshine", "e"))

