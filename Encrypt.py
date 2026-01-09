
message = input("Enter the message you want to send. ")

encryption = str.maketrans({'a': '0', 'b': 'q', 'c': 'v', 'd':'g', 'e':'r', 'f':'3', 'g': 's', 'h':'t', 
                       'i':'f', 'j': 'u', 'k':'5', 'l': 'x', 'm':'a', 'n': 'j', 'o': '8', 'p': 'l',
                        'q': '2', 'r': 'i', 's': 'h', 't':'m', 'u': '1', 'v': 'b', 'w': 'c',
                         'x': 'd', 'y': 'z', 'z': 'e'})
decryption= str.maketrans({'0': 'a', 'q': 'b', 'v': 'c', 'g':'d', 'r':'e', '3':'f', 's': 'g', 't':'h', 
                       'f':'i', 'u': 'j', '5':'k', 'x': 'l', 'a':'m', 'j': 'n', '8': 'o', 'l': 'p',
                        '2': 'q', 'i': 'r', 'h': 's', 'm':'t', '1': 'u', 'b': 'v', 'c': 'w',
                         'd': 'x', 'z': 'y', 'e': 'z'})

new_message = message.translate(encryption)
print ("Your message has been encrypted.\n" + new_message)

transBack = input ("Would you like to translate it back? (y/n) ")

if transBack == "y":
    old_message = new_message.translate(decryption)
    print ("Your message has been decrypted. " + old_message)

print ("Happy encrypting!")