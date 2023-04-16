should_continue = True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # todo-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    def caesar(text, shift):
        alphabet_index = []
        cypher_text = ""

        for letter in text:  
            if letter in alphabet:
                alphabet_index.append(alphabet.index(letter))
            else:
                alphabet_index.append(letter)
            
        for _ in range(shift):
            if direction == "encode":
                letter = alphabet.pop(0)
                alphabet.append(letter)
            elif direction == "decode":
                letter = alphabet.pop(-1)
                alphabet.insert(0, letter)
            else:
                print("""Invalid command. type "encode" or "decode" to proceed with this program """)
                return ""

        for index in alphabet_index:
            if type(index) == str:
                cypher_text += index
            else:
                cypher_text += alphabet[index]
        
    
        print(f"The {direction}d text is {cypher_text}")

    caesar(text, shift)

    again = input("Do you want to continue using this program? [y] or [n]: ").lower()
    
    if again == 'y' or again == 'yes':
        continue
    elif again == 'n' or again == 'no':
        should_continue = False





    
