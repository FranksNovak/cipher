alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encode(message, shift_number):
#     shifted_text = ""
#     for one_letter in message:
#         if one_letter != " ":
#             index = alphabet.index(one_letter)
#             new_index = index + shift_number
#             shifted_text += alphabet[new_index]
#         else:
#             shifted_text += one_letter
#     print(f"Your encrypted text is {shifted_text}")

# def decode(encrypted_message, shift_number):
#     normal_text = ""
#     for one_letter in encrypted_message:
#         if one_letter != " ":
#             index = alphabet.index(one_letter)
#             new_index = index - shift_number
#             normal_text += alphabet[new_index]
#         else:
#             normal_text += one_letter
#     print(f"your decrypted text is {normal_text}")

def cipher(start_text, shift_number, direction):
    end_text = ""
    for one_letter in start_text:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            if direction == "encode":
                new_index = index + shift_number
                end_text += alphabet[new_index]
            elif direction == "decode":
                  new_index = index - shift_number
                  end_text += alphabet[new_index]
        else:
            end_text += one_letter
    print(f"Vaše operace byla {direction} a výsledek je {end_text}.")

lets_continue = "yes"
while lets_continue == "yes":
    direction = input("Napište 'encode' pokud chcete zakodovat zprávu. Napište 'decode' pokud chcete dekodovat zprávu.\n")
    text = input("Napište svou zprávu\n").lower()
    shift = int(input("Napište hodnotu posunu:\n"))
    cipher(text, shift, direction)
    lets_continue = input("Napište 'yes' pokud chcete pokračovat. Napište 'no' pokud chcete šifrovací program ukončit.")
    
