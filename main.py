
def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
        print(b)
    return a

def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
    return gcd, y, x - (a // b) * y

def prime_factorization(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors



def encrypt(text, key):

    key = abs(int(key))
    table = [[] for _ in range(key)]
    row = 0
    for char in text:
        table[row].append(char)
        row = (row + 1) % key
    encrypted_text = ''.join([''.join(row) for row in table])

    return encrypted_text

def decrypt(ciphertext, key):

    key = abs(int(key))
    num_columns = len(ciphertext) // key + (len(ciphertext) % key > 0)
    table = [[' ' for _ in range(num_columns)] for _ in range(key)]
    index = 0
    for col in range(num_columns):
        for row in range(key):
            if index < len(ciphertext):
                table[row][col] = ciphertext[index]
                index += 1

    decrypted_text = ''.join([''.join(row) for row in table])

    return decrypted_text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Пример использования алгоритма Эвклида
    num1 = 101398751
    num2 = 326147777
    gcd_result = euclidean_algorithm(num1, num2)
    print(f"GCD of {num1} and {num2} is {gcd_result}")

    # Пример использования расширенного алгоритма Эвклида
    num1 = 101398751
    num2 = 326147777
    gcd_result, x, y = extended_euclidean_algorithm(num1, num2)
    print(f"GCD of {num1} and {num2} is {gcd_result}")
    print(f"Coefficients (x, y): ({x}, {y})")

    number = 326147777
    result = prime_factorization(number)

    print(f"Prime factorization of {number}: {result}")

    plaintext = "Hello,World!"
    encryption_key = 3
    cipher_text = encrypt(plaintext, encryption_key)

    print("Original Text:", plaintext)
    print("Encrypted Text:", cipher_text)

    encrypted_text = cipher_text
    decryption_key = 1
    decrypted_text = decrypt(encrypted_text, decryption_key)
    while plaintext != decrypted_text:
        decryption_key += 1
        decrypted_text = decrypt(encrypted_text, decryption_key)

    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
