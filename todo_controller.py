import sys
from todo_view import TodoView
from todo_model import TodoModel

class TodoContoller(object):

    def __init__(self):
        self.todo_view = TodoView()
        self.todo_model = TodoModel()
        self.user_command()

    def get_arguments(self):
        if len(sys.argv) > 1:
            return sys.argv[1]
        return None

    def user_command(self):
        self.arg = self.get_arguments()
        if self.arg == None:
            self.todo_view.print_commands()
        elif self.arg == '-l':
            self.todo_view.print_list(self.todo_model.todo_list)
        elif self.arg == '-a':
            self.add_task(sys.argv[2])
        elif self.arg == '-r':
            self.remove_task(sys.argv[2])
        elif self.arg == '-c':
            self.checked_task(sys.argv[2])
        else:
            print('\n-Unsupported argument-\n')
            self.todo_view.print_commands()

    def add_task(self, task):
        with open('todo_list.txt', 'a') as text_file:
            text_file.write('0' + task + '\n')
            text_file.close

    def remove_task(self, task_number):
        with open('todo_list.txt', 'r') as text_file:
            self.list = list(text_file)

        del self.list[int(task_number) - 1]

        with open('todo_list.txt', 'w') as text_file:
            for i in self.list:
                text_file.write(i)
                text_file.close

    def checked_task(self, finished_task):
        with open('todo_list.txt', 'r') as text_file:
            self.list = list(text_file)

        completed_task = self.list[int(finished_task) - 1]
        self.list[int(finished_task) - 1] = completed_task.replace('0', '1')
        print(self.list, completed_task)
        
        with open('todo_list.txt', 'w') as text_file:
            for i in self.list:
                text_file.write(i)


todo = TodoContoller()