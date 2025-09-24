def to_pig_latin(word):
    ch = word[0]
    if (ch == 'a' or
        ch == 'e' or
        ch == 'i' or
        ch == 'o' or
        ch == 'u'):
        word += "way"
    else:
        if ch == 'y':
            word = word[1:]
            word += ch
            ch = word[0]
        while (ch != 'a' and
               ch != 'e' and
               ch != 'i' and
               ch != 'o' and
               ch != 'u' and
               ch != 'y'):
            word = word[1:]
            word += ch
            ch = word[0]
        word += "ay"
    return word

