import sympy
import time

def encrypt_text(message, public_key, alphabet):
    start_time = time.perf_counter()
    e, n = public_key

    char_dict = {char: index + 1 for index, char in enumerate(alphabet)}
    text_num = [char_dict.get(char) for char in message]
    ciphertext_nums = [(num ** e) % n for num in text_num]

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Encryption execution time: {execution_time:.5f} seconds")

    return ciphertext_nums


def decrypt_text(cipher_text, private_key, alphabet):
    start_time = time.perf_counter()
    d, n = private_key

    num_text = {index + 1: char for index, char in enumerate(alphabet)}
    decrypted_nums = [(num ** d) % n for num in cipher_text]
    decrypted_message = ''.join([num_text.get(num, '.') for num in decrypted_nums])

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Decryption execution time: {execution_time:.5f} seconds")

    return decrypted_message


def generate_rsa_keys(p, q):
    if not (sympy.isprime(p) and sympy.isprime(q)):
        print("Both numbers must be prime.")
        exit()

    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = sympy.prevprime(p)
    d = sympy.mod_inverse(e, phi_n)

    return (e, n), (d, n)

# 13 41
p = int(input("Enter p: "))
q = int(input("Enter q: "))
public_key, private_key = generate_rsa_keys(p, q)

alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ 0123456789'
message = "СБОР21"
encrypt = [191, 139, 117, 270, 458, 346, 1, 79]

encrypted_result = encrypt_text(message, public_key, alphabet)
decrypted_result = decrypt_text(encrypt, private_key, alphabet)

print("Public Key:", public_key)
print("Private Key:", private_key)
print("\nMessage to encrypt:", message)
print("Encrypted:", encrypted_result)
print("\nMessage to decrypt:", encrypt)
print("Decrypted:", decrypted_result)
