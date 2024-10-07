class Stek:
    def __init__(self, stek):
        self.stek = stek

    def add_element(self, element):
        self.stek.append(element)

    def del_last_element(self):
        self.stek.pop(-1)

    def get_element(self):
        return self.stek[-1]

    def get_stek(self):
        return self.stek


class TaskManager:
    def __init__(self):
        self.tasks = Stek([])

    def new_task(self, name, prior):
        self.tasks.add_element([prior, name])

    def __str__(self):
        return str(sorted(self.tasks.get_stek()))


if __name__ == '__main__':
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать ДЗ", 2)
    print(manager)

