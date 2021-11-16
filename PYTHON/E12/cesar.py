import argparse
import detectEnglish, descifradoTransposicion

def main():
    # You might want to copy & paste this text from the source code at
    # https://invpy.com/transpositionHacker.py
    #propuesta: Iuirisr dnmoeisyfanctt ot uy
    #propuesta 2: Hoeaeedo sn rlsttusaoueni yd idy idva
    myMessage = message

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print(hackedMessage)


def hackTransposition(message):
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # Brute-force by looping through every possible key.
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))

        decryptedText = descifradoTransposicion.decryptMessage(key, message)#TODAS las sol.

        if detectEnglish.isEnglish(decryptedText):
            # Ask user if this is the correct decryption.
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("-n1", dest="e", help="escribe el modo que desees (encriptar , desencriptar  y crackear) ")


    parser.add_argument("-n2", dest="mensaje",help="escribe la frase o el mesanje ")

    parser.add_argument("-n3", dest="clave", help="clave para cifrar o descifrar, en caso de seleccionar crackear este elemento no es necesario")
                    

    params = parser.parse_args()

    modo = params.e                    
    message =  params.mensaje
    clave = params.clave

    print('---------------------------------------------------------------------------')
    print ("el modo seleccionado es: ", modo, "para el/la - frase/mensaje: ", message, "la clave es: ", clave,)
    print('---------------------------------------------------------------------------')

    if modo == "encriptar":
        espacios = 1
        while espacios > 0:
          
            espacios = clave.count(' ')
            if clave.isalpha() == False:
                espacios += 1
        key = len(clave)

        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

        translated = ''

        for symbol in message:
            # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex + key

            
                
                if translatedIndex >= len(SYMBOLS):
                    translatedIndex = translatedIndex - len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol

        print("EL MENSAJE CIFRADO ES: ",translated)


    elif modo == "desencriptar":
        espacios = 1
        while espacios > 0:
          
            espacios = clave.count(' ')
            if clave.isalpha() == False:
                espacios += 1
        key = len(clave)

        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

        translated = ''

        for symbol in message:
            # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

            
                
                if translatedIndex >= len(SYMBOLS):
                    translatedIndex = translatedIndex - len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol

        print("EL MENSAJE CIFRADO ES: ",translated)

    elif modo == "crackear":
            main()

    else:
         print('Intente Nuevamente')
    
        
    

