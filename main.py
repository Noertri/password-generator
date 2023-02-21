import random
import string


def generate(length=6, numbers=False, spec_chars=False):
    letters = string.ascii_letters
    digits = string.digits
    puncts = "!@#$%&-_?"

    pwd = ""

    while len(pwd) < length:

        if length > 32:
            break

        if numbers and not spec_chars:
            letter = random.choice(letters+digits)
        elif not numbers and spec_chars:
            letter = random.choice(letters+puncts)
        elif numbers and spec_chars:
            letter = random.choice(letters+puncts+digits)     
        else:
            letter = random.choice(letters)

        pwd += letter

    return pwd


if __name__ == "__main__":
    print("Program untuk membuat password acak secara otomatis")
    pwd_length = int(input("Panjang password: ").strip())
    if 6 < pwd_length <= 32:
        pwd_numbers = input("Tambahkan digit angka [y/n]: ").lower() == "y"
        pwd_spec_chars = input("Tambahkan karakter khusus [y/n]: ").lower() == "y"
        pwd = generate(length=pwd_length, spec_chars=pwd_numbers, numbers=pwd_spec_chars)
        print("Password anda = ", pwd)
    else:
        print("Panjang password minimal 6 dan maksimal 32!!!")