from random import randint

def password_generate(password_length = 10, password_quantity = 1):
    for i in range(1, password_quantity + 1, 1):
        password = ""
        for j in range(0, password_length, 1):
            #Basic Latin (Unicode block) 32-126
            ranges = [(48, 57), (65, 90), (97, 122)]
            for k, l in enumerate(ranges):
                # 0: 1/1, 1: 1/2, 2: 1/3
                if randint(0, k) == 0:
                    num = randint(*l)
            random_hex = hex(num).replace("0x", "")
            unicode_character = bytes.fromhex(random_hex).decode("utf-8")
            password += unicode_character
        #print(f"{i}: {password}")
    return password

if __name__ == "__main__":
    print(f"Password: {password_generate()}")