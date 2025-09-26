def caesar_encryption(msg):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    private_key = 19
    encry_message = ""
    for c in msg:
        position = alphabet.find(c)
        new_position = (position + private_key) % len(alphabet)
        new_character = alphabet[new_position]
        encry_message += new_character
    return encry_message

def caesar_decryption(msg, public_key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    private_key = 23
    decry_message = ""
    key = int(public_key / private_key)
    for c in msg:
        position = alphabet.find(c)
        new_position = (position - key) % len(alphabet)
        new_character = alphabet[new_position]
        decry_message += new_character
    return decry_message

if __name__ == "__main__":
    public_key = 19 * 23
    message = input("Please enter message: ")
    encrypted = caesar_encryption(message)
    print("Encrypted message:", encrypted)
    decrypted = caesar_decryption(encrypted, public_key)
    print("Decrypted message:", decrypted)
