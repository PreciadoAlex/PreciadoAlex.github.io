
def Encrypt(plainText):
    even = ''
    odd = ''
    acc = 0

    for ch in plainText:
        if acc % 2 is 0:
            even = even + ch
        else:
            odd = odd + ch

        acc = acc + 1

    ciphertext = even + odd

    return ciphertext

msg = Encrypt('I want my message to be encrypted!')

print (msg)

def Decrypt(plainText):
    thing1 = ''
    thing2 = ''
    msg2 = ''
    smol = int(len(plainText)/2)
    big = int(len(plainText))
    acc2 = 0
    for i in plainText:
        if acc2 <= smol:
            thing1 = thing1 + i
        if acc2 >= smol:
            thing2 = thing2 + i
        acc2 = acc2 + 1
    #print (thing1)
    #print (thing2)
    acc2 = 0
    for i in range (smol):
        msg2 = msg2 + thing1[i]
        msg2 = msg2 + thing2[i]
    return msg2
msg2 = Decrypt('Iwn ymsaet eecytd atm esg ob nrpe!')
print (msg2)
