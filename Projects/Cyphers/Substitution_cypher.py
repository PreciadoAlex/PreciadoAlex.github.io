string = ('The quick brown fox jumps over the lazy dog')
def encrypt (plainText):
    for ch in string:
        if ch == 'a':
            print ('!', end='')
        elif ch == 'e':
            print ('#', end='')
        elif ch == 'i':
            print ('%', end='')
        elif ch == 'o':
            print ('&', end='')
        elif ch == 'u':
            print ('(', end='')
        else:
            print (ch, end='')
#encrypt (string)

string2 = ('Th# q(%ck br&wn f&x j(mps &v#r th# l!zy d&g')
def decrypt(plainText):
    for ch in string2:
        if ch == '!':
            print ('a', end='')
        elif ch == '#':
            print ('e', end='')
        elif ch == '%':
            print ('i', end='')
        elif ch == '&':
            print ('o', end='')
        elif ch == '(':
            print ('u', end='')
        else:
            print (ch, end='')
decrypt (string2)


