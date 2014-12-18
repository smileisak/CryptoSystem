#!/usr/bin/python2.7 
# Affine Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)
       

import  Cryp_affine, inverse_modulaire, detectEnglish

SILENT_MODE = False

#def main():
#    # You might want to copy & paste this text from the source code at
    # http://invpy.com/affineHacker.py
    #myMessage = """U&'<3dJ^Gjx'-3^MS'Sj0jxuj'G3'%j'<mMMjS'g{GjMMg9j{G'g"'gG'<3^MS'Sj<jguj'm'P^dm{'g{G3'%jMgjug{9'GPmG'gG'-m0'P^dm{LU'5&Mm{'_^xg{9"""
#    myMessage = """g)>R1>R13q13IRRTsI1g]1i=|gI^]=~I"""
#    hackedMessage = hackAffine(myMessage)

#    if hackedMessage != None:
 #       # The plaintext is displayed on the screen. For the convenience of
        # the user, we copy the text of the code to the clipboard.
#        print('Copying hacked message to clipboard:')
#        print(hackedMessage)
 #   else:
 #       print('Failed to hack encryption.')


def hackAffine(message):
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # brute-force by looping through every possible key
    for key in range(len(Cryp_affine.SYMBOLS) ** 2):
        keyA = Cryp_affine.getKeyParts(key)[0]
        if inverse_modulaire.pgcd(keyA, len(Cryp_affine.SYMBOLS),1) != 1:
            continue

        decryptedText = Cryp_affine.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            # Check with the user if the decrypted key has been found.    
            print()
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            return decryptedText
    return None


# If affineHacker.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()