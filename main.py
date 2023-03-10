import random
import string
import os


def generate(length=6, numbers=False, spec_chars=False):
    letters = string.ascii_letters
    digits = string.digits
    puncts = "!@#$%&_?"

    pwd = ""

    # menggunakan modul random choices untuk membuat password
    if numbers and spec_chars:
        letter = random.choices(letters+puncts+digits, k=length)
    elif spec_chars:
        letter = random.choices(letters+puncts, k=length)
    elif numbers:
        letter = random.choices(letters+digits, k=length)     
    else:
        letter = random.choices(letters, k=length)

    pwd = "".join(letter)

    return pwd


if __name__ == "__main__":
    print("Program untuk membuat password acak secara otomatis")
    pwd_length = int(input("Panjang password: ").strip())
    if 6 <= pwd_length <= 32:
        pwd_numbers = input("Tambahkan digit angka [y/n]: ").lower() == "y"
        pwd_spec_chars = input("Tambahkan karakter khusus [y/n]: ").lower() == "y"
        pwd = generate(length=pwd_length, numbers=pwd_numbers, spec_chars=pwd_spec_chars)
        print("Password anda: ", pwd)
    else:
        print("Panjang password minimal 6 dan maksimal 32!!!")

   #os.system("pause")
