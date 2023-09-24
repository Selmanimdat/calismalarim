def rot13(encoded_str):
    decoded_str = ""
    for char in encoded_str:
        if 'A' <= char <= 'Z':
            # Calculate the new character position, wrapping around if necessary
            decoded_char = chr(((ord(char) - ord('A') - 13) % 26) + ord('A'))
        else:
            # Non-alphabetic characters are passed through unchanged
            decoded_char = char
        decoded_str += decoded_char
    return decoded_str