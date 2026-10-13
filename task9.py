from pathlib import Path


class FileManager:
    def __init__(self, filename):
        self.filename = Path(filename)

    def exists(self):
        return self.filename.exists()

    def read(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return file.read()

    def write(self, text):
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write(text)

    def append(self, text):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(text)

    def delete(self):
        if self.filename.exists():
            self.filename.unlink()
            print("Файл удален")
        else: 
            print("Файл не найден")


file = FileManager("test.txt")
file.write("Пример текста для записи")
file.append("\nв файл")

print(file.read())
print(file.exists())