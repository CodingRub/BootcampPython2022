def read(path):
    f = open(path, "r")
    return f.read()

def write(filename, msg):
    with open(f"C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/mailMerge/output/ReadyToSend/{filename}", "w") as file:
        file.write(msg)
        file.close()

names = read("C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/mailMerge/input/names/invited_names.txt").splitlines()
letter = read("C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/mailMerge/input/letters/starting_letter.txt")

for name in names:
    letter_perso = letter.replace("[name]", name)
    write(f"letter_for_{name}.txt", letter_perso)


