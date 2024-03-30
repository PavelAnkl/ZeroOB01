class Task:
    def __init__(self, description, deadline, status=False):
        """Инициализация новой задачи с описанием, сроком выполнения и статусом."""
        self.description = description
        self.deadline = deadline
        self.status = status

    def __str__(self):
        """Возвращает строковое представление задачи."""
        return f"{self.description}, Дата выполнения: {self.deadline}, Статус: {'Выполнена' if self.status else 'Не выполнена'}"

class TaskManager:
    def __init__(self):
        """Инициализация менеджера задач с пустым списком задач."""
        self.tasks = []

    def add_task(self, description, deadline):
        """Добавляет новую задачу в список задач."""
        new_task = Task(description, deadline)
        self.tasks.append(new_task)
        print("Задача добалена.")

    def mark_task_done(self, description):
        """Отмечает задачу как выполненную по описанию."""
        for task in self.tasks:
            if task.description == description:
                task.status = True
                print(f"Задача '{description}' выполнена.")
                return
        print(f"Задача '{description}' не найдена.")

    def show_current_tasks(self):
        """Выводит список текущих (не выполненных) задач."""
        print("Список невыполненных задач:")
        for task in self.tasks:
            if not task.status:
                print(task)

# Пример использования классов Task и TaskManager
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Тестовая задача 1", "2024-03-28")
    manager.add_task("Тестовая задача 2", "2024-03-28")

    manager.show_current_tasks()

    manager.mark_task_done("Тестовая задача 1")

    manager.show_current_tasks()
