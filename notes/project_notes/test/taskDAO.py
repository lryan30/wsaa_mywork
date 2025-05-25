import csv

class TaskDAO:
    def __init__(self, filename='tasks.csv'):
        self.filename = filename
        self.tasks = []

        try:
            with open(self.filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None)  # Skip header
                for idx, row in enumerate(reader):
                    if len(row) < 4:
                        continue
                    task = {
                        "id": idx + 1,
                        "title": row[0],
                        "description": row[1],
                        "due_date": row[2],
                        "status": row[3]
                    }
                    self.tasks.append(task)
            self.last_id = self.tasks[-1]["id"] if self.tasks else 0
        except FileNotFoundError:
            self.tasks = []
            self.last_id = 0

    def save_to_file(self):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Description", "DueDate", "Status"])
            for task in self.tasks:
                writer.writerow([task["title"], task["description"], task["due_date"], task["status"]])

    def getAll(self):
        return self.tasks

    def findByID(self, id):
        for task in self.tasks:
            if task["id"] == id:
                return task.copy()
        return None

    def create(self, task):
        self.last_id += 1
        new_task = {
            "id": self.last_id,
            "title": task.get("title"),
            "description": task.get("description"),
            "due_date": task.get("due_date"),
            "status": task.get("status", "Pending")  # Default status
        }
        self.tasks.append(new_task)
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([new_task["title"], new_task["description"], new_task["due_date"], new_task["status"]])
        return new_task

    def update(self, id, task):
        for i, existing in enumerate(self.tasks):
            if existing["id"] == id:
                self.tasks[i]["title"] = task.get("title", existing["title"])
                self.tasks[i]["description"] = task.get("description", existing["description"])
                self.tasks[i]["due_date"] = task.get("due_date", existing["due_date"])
                self.tasks[i]["status"] = task.get("status", existing["status"])
                self.save_to_file()
                return

    def delete(self, id):
        for i, existing in enumerate(self.tasks):
            if existing["id"] == id:
                self.tasks.pop(i)
                self.save_to_file()
                return

# Global DAO instance
taskDAO = TaskDAO()
