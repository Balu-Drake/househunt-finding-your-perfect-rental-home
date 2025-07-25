# Caesar Cipher Encoding and Decoding

def caesar_cipher(text, shift, mode='encode'):
    """
    Encodes or decodes a message using the Caesar cipher.

    Args:
        text (str): The message to be encoded or decoded.
        shift (int): The number of positions to shift each letter.
        mode (str): 'encode' for encryption, 'decode' for decryption.
                    Defaults to 'encode'.

    Returns:
        str: The encoded or decoded message.
    """
    result = ""
    # Determine the effective shift based on mode
    if mode == 'decode':
        shift = -shift

    for char in text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            start = ord('a')
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(shifted_char_code)
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters
            start = ord('A')
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(shifted_char_code)
        else:
            # Keep non-alphabetic characters as they are
            result += char
    return result

# Example Usage for Caesar Cipher (hardcoded for demonstration)
print("--- Caesar Cipher ---")
# Using hardcoded values to avoid EOFError in non-interactive environments
message = input("Enter the Message :- ")
shift_amount = 3

encoded_message = caesar_cipher(message, shift_amount, mode='encode')
print(f"Original Message: {message}")
print(f"Encoded Message (shift {shift_amount}): {encoded_message}")

decoded_message = caesar_cipher(encoded_message, shift_amount, mode='decode')
print(f"Decoded Message (shift {shift_amount}): {decoded_message}")
print("\n")


# Indian Currency Formatting

def format_indian_currency(number):
    """
    Converts a floating-point number into an Indian currency string format
    with commas (Lakhs, Crores).

    Args:
        number (float or int): The number to format.

    Returns:
        str: The formatted currency string.
    """
    # Convert to string and separate integer and decimal parts
    s = str(float(number))
    if '.' in s:
        parts = s.split('.')
        integer_part = parts[0]
        decimal_part = parts[1]
    else:
        integer_part = s
        decimal_part = ''

    # Handle negative numbers
    sign = ''
    if integer_part.startswith('-'):
        sign = '-'
        integer_part = integer_part[1:]

    # Format the integer part
    formatted_integer = []
    # Get the last three digits first
    if len(integer_part) > 3:
        formatted_integer.append(integer_part[-3:])
        integer_part = integer_part[:-3]
    else:
        formatted_integer.append(integer_part)
        integer_part = ''

    # Format the remaining digits in groups of two
    while integer_part:
        if len(integer_part) > 2:
            formatted_integer.append(integer_part[-2:])
            integer_part = integer_part[:-2]
        else:
            formatted_integer.append(integer_part)
            integer_part = ''

    # Reverse and join with commas
    formatted_integer_str = ','.join(reversed(formatted_integer))

    # Combine with decimal part if present
    if decimal_part:
        return f"{sign}{formatted_integer_str}.{decimal_part}"
    else:
        return f"{sign}{formatted_integer_str}"

# Example Usage for Indian Currency Formatting (hardcoded for demonstration)
print("--- Indian Currency Formatting ---")
# Using hardcoded values to avoid EOFError in non-interactive environments
amount1 = float(input("Enter the Value :- "))
amount2 = 12345.00
amount3 = 9876543210.123
amount4 = 500
amount5 = -1234567.89

print(f"Original Amount: {amount1} -> Formatted: {format_indian_currency(amount1)}")
