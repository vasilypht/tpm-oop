import sys
from enum import Enum
import re


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

    def sort(self):
        for i in range(self.size):
            curr_node = self.head
            while curr_node.next:
                next_node = curr_node.next
                if curr_node.data.compare(next_node.data):
                    curr_node.data, next_node.data = next_node.data, curr_node.data
                curr_node = next_node

    def write_game_film_to(self, stream):
        stream.write("Only game films.\n")

        for item in self:
            item.write_game_film_to(stream)

    def compare_films(self):
        film_pack_1 = [item for item in self]
        film_pack_2 = film_pack_1.copy()

        for film_1 in film_pack_1:
            for film_2 in film_pack_2:
                Film.check_films(film_1, film_2)

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        self.__cur_item = self.head
        return self

    def __next__(self):
        if self.__cur_item is not None:
            data = self.__cur_item.data
            self.__cur_item = self.__cur_item.next
            return data

        else:
            raise StopIteration


class Film:
    def __init__(self):
        self.title = ""
        self.country = ""

    def read_from(self, stream):
        try:
            self.country = stream.readline().rstrip("\n")
        except Exception:
            print("Country read error!")
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        try:
            stream.write(f"\tCountry: {self.country}\n")
            stream.write(f"\tNum of vowels in title: {self.num_vowels_in_title()}\n")
        except Exception:
            print("Error writing data to file!")
            stream.close()
            sys.exit(1)

    @staticmethod
    def create_from(stream, line):
        try:
            k = int(line)
        except Exception:
            print(f"Number conversion error. ({line})")
            stream.close()
            sys.exit(1)

        match k:
            case 1:
                film = GameFilm()

            case 2:
                film = Cartoon()

            case 3:
                film = Documentary()

            case _:
                stream.close()
                print(f"Error, invalid object id entered: {k}")
                sys.exit(1)

        film.read_from(stream)
        return film

    @staticmethod
    def check_films(film_1, film_2):
        match film_1, film_2:
            case GameFilm(), GameFilm():
                print("Films from the same category")
                print("Type - first film: GameFilm, second film: GameFilm")
                print(f"Name - first film: {film_1.title}, second film: {film_2.title}")
                print()

            case GameFilm(), Cartoon():
                print("Films from different categories")
                print("Type - first film: GameFilm, second film: Cartoon")
                print(f"Name - first film: {film_1.title}, second film: {film_2.title}")
                print()

            case GameFilm(), Documentary():
                print("Films from different categories")
                print("Type - first film: GameFilm, second film: Documentary")
                print(f"Name - first film: {film_1.title}, second film: {film_2.title}")
                print()


            case Cartoon(), GameFilm():
                print("Films from different categories")
                print("Type - first film: Cartoon, second film: GameFilm")
                print(f"Name - first film: {film_1.title}, second film: {film_2.title}")
                print()

            case Cartoon(), Cartoon():
                print("Films from the same category")
                print("Type - first film: Cartoon, second film: Cartoon")
                print(f"Name - first film: {film_1.title}, second film: {film_2.title}")
                print()

            case Cartoon(), Documentary():
                print("Films from different categories")
                print("Type - first film: Cartoon, second film: Documentary")
                print(f"Name - first film: {film_1.title}, second film: {film_2.title}")
                print()


            case Documentary(), GameFilm():
                print("Films from different categories")
                print("Type - first film: Documentary, second film: GameFilm")
                print(f"Name - first film: {film_1.title}, second film: {film_2.title}")
                print()

            case Documentary(), Cartoon():
                print("Films from different categories")
                print("Type - first film: Documentary, second film: Cartoon")
                print(f"Name - first film: {film_1.title}, second film: {film_2.title}")
                print()

            case Documentary(), Documentary():
                print("Films from the same category")
                print("Type - first film: Documentary, second film: Documentary")
                print(f"Name - first film: {film_1.title}, second film: {film_2.title}")
                print()

    def write_game_film_to(self, stream):
        pass

    def num_vowels_in_title(self):
        return len(re.findall(r"[????????????????????aeiouy]", self.title, re.IGNORECASE))

    def compare(self, other):
        return self.num_vowels_in_title() < other.num_vowels_in_title()


class GameFilm(Film):
    def __init__(self):
        super().__init__()
        self.director = ""

    def read_from(self, stream):
        try:
            self.title = stream.readline().rstrip("\n")
            self.director = stream.readline().rstrip("\n")
            super().read_from(stream)
        except Exception:
            print("Game movie data read error.")
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        try:
            stream.write(f"This is a game movie.\n"
                         f"\tTitle: {self.title}\n"
                         f"\tDirector: {self.director}\n")
            super().write_to(stream)
        except Exception:
            stream.close()
            print("Error writing data to file!")
            sys.exit(1)

    def write_game_film_to(self, stream):
        try:
            self.write_to(stream)
        except Exception:
            stream.close()
            print("Error writing data to file!")
            sys.exit(1)

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
        try:
            self.title = stream.readline().rstrip("\n")
        except Exception:
            stream.close()
            print("Name reading error!")
            sys.exit(1)

        try:
            k = int(stream.readline())
        except Exception:
            print(f"Number conversion error.")
            stream.close()
            sys.exit(1)

        match k:
            case WayToCreate.drawn.value:
                self.way_to_create = WayToCreate.drawn
            case WayToCreate.puppet.value:
                self.way_to_create = WayToCreate.puppet
            case WayToCreate.plasticine.value:
                self.way_to_create = WayToCreate.plasticine
            case _:
                stream.close()
                print(f"Error, invalid object id entered: {k}")
                sys.exit(1)
        try:
            super().read_from(stream)
        except Exception:
            stream.close()
            print("Cartoon data read error!")
            sys.exit(1)

    def write_to(self, stream):
        try:
            stream.write(f"This is a cartoon.\n"
                         f"\tTitle: {self.title}\n"
                         f"\tWay to create: {self.way_to_create.name}\n")
            super().write_to(stream)

        except Exception:
            stream.close()
            print("Error writing data to file!")
            sys.exit(1)

    def __str__(self):
        return f"This is a cartoon.\n"\
               f"\tTitle: {self.title}\n"\
               f"\tWay to create: {self.way_to_create.name}\n"


class Documentary(Film):
    def __init__(self):
        super().__init__()
        self.year_of_issue = 0

    def read_from(self, stream):
        try:
            self.title = stream.readline().rstrip("\n")
            self.year_of_issue = int(stream.readline())
            super().read_from(stream)
        except Exception:
            stream.close()
            print("Documentary Read Error!")
            sys.exit(1)

    def write_to(self, stream):
        try:
            stream.write(f"This is a documentary.\n"
                         f"\tTitle: {self.title}\n"
                         f"\tYear of issue: {self.year_of_issue}\n")
            super().write_to(stream)
        except Exception:
            stream.close()
            print("Error writing documentary film data to file.")
            sys.exit(1)

    def __str__(self):
        return f"This is a documentary.\n" \
               f"\tTitle: {self.title}\n" \
               f"\tYear of issue: {self.year_of_issue}\n"
