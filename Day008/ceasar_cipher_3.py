alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

again = True


import os

def clear_console():
    # os.name gibt den Namen des Betriebssystems zurück.
    # 'nt' steht für Windows, andere Werte sind für Unix-basierte Systeme.
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')




def ceasar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1


    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]



    print(f"Here is the encoded result: {output_text}")
    
 

    


        

while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    again = input("Do you want encode/decode again? yes or no? y/n: ").lower()
    if again == "n" or again == "no":
        break

    clear_console()
