import random
import string
import os


def generate(length=6, numbers=False, spec_chars=False, upper_case=False):
    letters = string.ascii_letters
    lower_letters = string.ascii_lowercase
    digits = string.digits
    puncts = "!@#$%&-?"

    pwd = ""

    # menggunakan modul random sample untuk membuat password
    
    if numbers and spec_chars and upper_case:
        p = random.sample(letters+puncts+digits, k=length)
    elif numbers and spec_chars:
        p = random.sample(lower_letters+puncts+digits, k=length)
    elif numbers and upper_case:
        p = random.sample(letters+digits, k=length)
    elif spec_chars and upper_case:
        p = random.sample(letters+puncts, k=length)
    elif spec_chars:
        p = random.sample(lower_letters+puncts, k=length)
    elif numbers:
        p = random.sample(lower_letters+digits, k=length)
    elif upper_case:
        p = random.sample(letters, k=length)
    else:
        p = random.sample(lower_letters, k=length)

    pwd += "".join(p)

    return pwd


if __name__ == "__main__":
    print("Program untuk membuat password acak secara otomatis")

    while True:
        pwd_length = int(input("Panjang password: ").strip())
        if 6 <= pwd_length <= 20:
            pwd_upper = input("Huruf kapital [y/n]: ").lower() == "y"
            pwd_numbers = input("Digit angka [y/n]: ").lower() == "y"
            pwd_spec_chars = input("Karakter khusus [y/n]: ").lower() == "y"
            pwd = generate(length=pwd_length, numbers=pwd_numbers, spec_chars=pwd_spec_chars, upper_case=pwd_upper)
            print("Password anda: ", pwd)
        else:
            print("Panjang password minimal 6 dan maksimal 20 karakter!!!")

        if input("Berhenti?[Y/n]: ").lower() == "y":
            break