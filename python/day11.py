import re

alphabet = "abcdefghijklmnopqrstuvwxyz"

old_password = "hepxcrrq"

def increment(password):
    
    reduced_alphabet = "abcdefghjkmnpqrstuvwxyza"

    i = len(password) - 1

    new_password = ""

    while i > -1:

        old_char = password[i]

        next_char = reduced_alphabet.index(old_char) + 1

        new_password = reduced_alphabet[next_char] + new_password

        if old_char == "z":
            i -= 1
        else:
            new_password = password[:i] + new_password
            break

    return new_password

def get_new_password(password):
    secure = False

    while not secure:

        password = increment(password)

        if re.search(r"[iol]", password):
            continue
        
        if len(re.findall(r"(.)\1", password)) < 2:
            continue

        for i in range(24):
            x = alphabet[i : i + 3]
            if re.search(alphabet[i : i + 3], password):
                secure = True
                break
            
    return password

new_password = get_new_password(old_password)

print("Part 1: First password: {0}.\nPart 2: Second password: {1}.".format(new_password, get_new_password(new_password)))

