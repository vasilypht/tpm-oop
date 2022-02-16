from enum import Enum


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_back(self, item) -> None:
        node = Node(item)

        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1

    def push_front(self, item) -> None:
        node = Node(item)

        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
            return

        self.head.prev = node
        node.next = self.head
        self.head = node
        self.size += 1

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def read_from(self, stream):
        while line := stream.readline():
            item = Film.create_from(stream, line)
            self.push_back(item)

    def write_to(self, stream):
        stream.write(f"Container contents {self.size} elements.\n")

        for item in self:
            item.write_to(stream)

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        self.__cur_item = self.head
        self.__cur_index = 0
        return self

    def __next__(self):
        if self.size == 0:
            raise StopIteration

        if self.__cur_index == 0:
            self.__cur_index += 1
            return self.__cur_item.data

        elif self.__cur_index < self.size:
            self.__cur_index += 1
            self.__cur_item = self.__cur_item.next
            return self.__cur_item.data

        else:
            raise StopIteration


class Film:
    def __init__(self):
        self.title = ""

    def read_from(self, stream):
        pass

    def write_to(self, stream):
        pass

    @staticmethod
    def create_from(stream, line):
        k = int(line)

        match k:
            case 1:
                film = GameFilm()

            case 2:
                film = Cartoon()

            case _:
                stream.close()
                raise Exception("Error type!")

        film.read_from(stream)
        return film


class GameFilm(Film):
    def __init__(self):
        super().__init__()
        self.director = ""

    def read_from(self, stream):
        self.title = stream.readline().rstrip("\n")
        self.director = stream.readline().rstrip("\n")

    def write_to(self, stream):
        stream.write(f"This is a game movie.\n"
                     f"\tTitle: {self.title}\n"
                     f"\tDirector: {self.director}\n")

    def __str__(self):
        return f"This is a game movie.\n"\
               f"\tTitle: {self.title}\n"\
               f"\tDirector: {self.director}\n"


class WayToCreate(Enum):
    drawn = 1
    puppet = 2
    plasticine = 3


class Cartoon(Film):
    def __init__(self):
        super().__init__()
        self.way_to_create = None

    def read_from(self, stream):
        self.title = stream.readline().rstrip("\n")

        k = int(stream.readline())

        match k:
            case WayToCreate.drawn.value:
                self.way_to_create = WayToCreate.drawn
            case WayToCreate.puppet.value:
                self.way_to_create = WayToCreate.puppet
            case WayToCreate.plasticine.value:
                self.way_to_create = WayToCreate.plasticine
            case _:
                stream.close()
                raise Exception("Error type!")

    def write_to(self, stream):
        stream.write(f"This is a cartoon.\n"
                     f"\tTitle: {self.title}\n"
                     f"\tWay to create: {self.way_to_create.name}\n")

    def __str__(self):
        return f"This is a cartoon.\n"\
               f"\tTitle: {self.title}\n"\
               f"\tWay to create: {self.way_to_create.name}\n"
