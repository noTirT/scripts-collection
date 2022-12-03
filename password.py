import sys
import string
import random
import subprocess

def main():
    available_items = {
        "letters": {
            "item_list": list(string.ascii_letters),
            "count": 2
        },
        "digits": {
            "item_list": list(string.digits),
            "count": 4
        },
        "symbols": {
            "item_list": list("!@#$%^*()"),
            "count": 4
        }
    }

    password_length = int(sys.argv[1]) if len(sys.argv) > 1 else 12

    password = []
    for item in available_items.values():
        random.shuffle(item["item_list"])
        for i in range(int(password_length/item["count"])):
            password.append(random.choice(item["item_list"]))

    random.shuffle(password)

    while(len(password) < password_length):
        password.append(random.choice(available_items["letters"]["item_list"]))

    print("".join(password))
    copy2clip("".join(password))

def copy2clip(txt):
    cmd = "echo " + txt.strip() + "| clip"
    print("Password has been copied to clipboard")
    return subprocess.check_call(cmd, shell=True)

if __name__ == "__main__":
    main()
