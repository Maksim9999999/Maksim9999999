key = {
    'A': '@', 'B': '#', 'C': '$', 'D': '%', 'E': '&', 'F': '*', 'G': '(',
    'H': ')', 'I': '!', 'J': '^', 'K': '_', 'L': '+', 'M': '~', 'N': '`',
    'O': '-', 'P': '=', 'Q': '{', 'R': '}', 'S': '[', 'T': ']', 'U': ';',
    'V': ':', 'W': '"', 'X': "'", 'Y': '<', 'Z': '>', ' ': ' '
}

# Повідомлення для розшифрування
encrypted_message = "[)@++ ! $-~=@}& <-; ]- @ [;~~&} %@<? <-; @}& ~-}& +-:&+< @`% ~-}& ]&~=&}@]&..."

# Створюємо зворотний словник: символ -> літера
reverse_key = {v: k for k, v in key.items()}

# Розшифровуємо повідомлення
decrypted_message = ''
for char in encrypted_message:
    if char in reverse_key:
        decrypted_message += reverse_key[char]
    else:
        decrypted_message += char  # Залишаємо як є, якщо немає в ключі

print(decrypted_message)
