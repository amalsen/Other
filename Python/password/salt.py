from random import randint

def salt_generate(salt_length = 10):
    salt = ""

    for i in range(1, salt_length + 1, 1):
        #Basic Latin (Unicode block) 32-126 (32 = Space)
        random_hex = hex(randint(33, 126)).replace("0x", "")
        unicode_character = bytes.fromhex(random_hex).decode("ascii")
        salt += unicode_character
        #print(f"{i}: {unicode_character}")
    return salt

if __name__ == "__main__":
    print(f"Salt: {salt_generate()}")