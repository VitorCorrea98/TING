from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        queue_list = self.data
        return queue_list.pop(0)

    def search(self, index):
        try:
            if index not in range(len(self.data)):
                raise IndexError
            return self.data[index]
        except IndexError:
            raise IndexError("Índice Inválido ou Inexistente")
