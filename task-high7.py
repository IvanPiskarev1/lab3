class Table: 
    def __init__(self, name):
        self.name = name
        self.rows = []

    def insert(self, data):
        self.rows.append(data)

    def select(self):
        return self.rows

    def delete(self, data):
        if data in self.rows:
            self.rows.remove(data)

    def count(self):
        return len(self.rows)


students = Table("students")

students.insert({"name": "Михаил", "age": 20})
students.insert({"name": "Александр", "age": 18})

print(students.select())

students.delete({"name": "Александр", "age": 18})
print(f"После удаления: {students.select()}")
print(f"Количество записей: {students.count()}")