import random
import string


def generate(length=6, numbers=False, spec_chars=False, upper_case=False):
    # menggunakan modul random sample untuk membuat password
    
    sequences = string.ascii_lowercase

    if upper_case:
        sequences += string.ascii_uppercase

    if numbers:
        sequences += string.digits

    if spec_chars:
        sequences += "!@#$%&-?_"

    p = random.sample(sequences, k=length)
    pwd = "".join(p)

    return pwd


if __name__ == "__main__":
    print("Program untuk membuat password acak secara otomatis")

    while True:
        pwd_length = int(input("Panjang password: ").strip())
        if 6 <= pwd_length <= 26:
            pwd_upper = input("Huruf kapital [y/n]: ").lower() == "y"
            pwd_numbers = input("Digit angka [y/n]: ").lower() == "y"
            pwd_spec_chars = input("Karakter khusus [y/n]: ").lower() == "y"
            pwd = generate(length=pwd_length, numbers=pwd_numbers, spec_chars=pwd_spec_chars, upper_case=pwd_upper)
            print("Password anda: ", pwd)
        else:
            print("Panjang password minimal 6 dan maksimal 26 karakter!!!")

        if input("Berhenti?[y/n]: ").lower() == "y":
            break
