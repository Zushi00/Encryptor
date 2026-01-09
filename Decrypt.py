
message = input ("Enter the message you want decrypted. ")

decryption= str.maketrans({'0': 'a', 'q': 'b', 'v': 'c', 'g':'d', 'r':'e', '3':'f', 's': 'g', 't':'h', 
                       'f':'i', 'u': 'j', '5':'k', 'x': 'l', 'a':'m', 'j': 'n', '8': 'o', 'l': 'p',
                        '2': 'q', 'i': 'r', 'h': 's', 'm':'t', '1': 'u', 'b': 'v', 'c': 'w',
                         'd': 'x', 'z': 'y', 'e': 'z'})
    
new_message = message.translate(decryption)
print ("Your message has been decrypted.\n" + new_message)