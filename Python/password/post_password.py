from password_generate import password_generate
from salt import salt_generate

password_length = 12
salt_length = 5

print(f"Password: {password_generate(password_length=password_length)} + Salt: {salt_generate(salt_length=salt_length)}")