import sys
import calculate_checksum

def calculate_final_key(key: int, password: str) -> int:
    final_key = 0
    if password:
        temp_key = 0xFFFFFFFF  
        for char in password:
            intermediate_key = temp_key ^ ord(char)
            for _ in range(8):
                temp_key = key ^ (intermediate_key >> 1)
                if (intermediate_key & 1) == 0:
                    temp_key = intermediate_key >> 1
                intermediate_key = temp_key
        final_key = ~temp_key & 0xFFFFFFFF 
    return final_key

def cryption_filter(src: bytes, key: int, password: str) -> bytes:
    final_key = calculate_final_key(key, password)
    dst = bytearray()
    for i, byte in enumerate(src):
        transformed_key = final_key ^ (final_key << 13) & 0xFFFFFFFF
        transformed_key ^= (transformed_key >> 17)
        transformed_key ^= (transformed_key << 5) & 0xFFFFFFFF
        final_key = transformed_key
        decrypted_byte = byte ^ (final_key & 0xFF)
        dst.append(decrypted_byte)
    return bytes(dst)

def decrypt_file(input_file: str, key: int, password: str):
    with open(input_file, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = cryption_filter(encrypted_data, key, password)

    with open(input_file, "wb") as f:
        f.write(decrypted_data)
    print(f"Decryption complete: {input_file}")

def encrypt_file(input_file: str, key: int, password: str):
    with open(input_file, "rb") as f:
        decrypted_data = f.read()

    encrypted_data = cryption_filter(decrypted_data, key, password)

    with open(input_file, "wb") as f:
        f.write(encrypted_data)
    print(f"Encryption complete: {input_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python save_decrypt.py decrypt <file_name>")
        print("  python save_decrypt.py encrypt <file_name>")
        print("  python save_decrypt.py checksum <file_name>")
        sys.exit(1)

    command = sys.argv[1]
    input_file = sys.argv[2]
    key = 0x7A7B58C6  
    password = "vb76Eg43" 

    if command == "decrypt":
        decrypt_file(input_file, key, password)
    elif command == "encrypt":
        encrypt_file(input_file, key, password)
    elif command == "checksum":
        calculate_checksum.checksum(input_file)
    else:
        print("Invalid command. Use decrypt, encrypt, or checksum.")
