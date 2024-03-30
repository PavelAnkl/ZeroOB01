class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline, 'description': description, 'status': 'Не выполнено'})

    def complete_tasks(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = 'Выполнено'
                print(f'Задача {description} выполнена')
            else:
                print(f'Задача {description} не найдена')

    def show_tasks(self):
        print('Текущие задачи')
        for task in self.tasks:
            if task['status'] == 'Не выполнено':
                print(f'{task['description']} - {task['deadline']}')


t = Task()
t.add_task('01.06.2023','Прочитать книгу')
t.add_task('02.06.2023','Посмотреть ТВ')
t.add_task('02.06.2023','Понажимать на кнопки')

t.show_tasks()

t.complete_tasks('Прочитать книгу')