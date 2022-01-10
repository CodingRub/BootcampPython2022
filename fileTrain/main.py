
def read(filename):
    with open(f"C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/fileTrain/{filename}") as file:
        print(file.read())
        file.close()

def write(filename, msg):
    with open(f"C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/fileTrain/{filename}", "w") as file:
        file.write(msg)
        file.close()

def create(filename):
    open(f"C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/fileTrain/{filename}", "x")

