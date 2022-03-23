import io

from module import DList


def test_clear():
    container = DList()
    for i in range(100):
        container.push_back(i)

    container.clear()

    assert len(container) == 0


def test_push_back():
    container = DList()
    container.push_back((1, 2, 3))
    container.push_back("Hello")
    container.push_back("World")

    array = [item for item in container]

    assert [(1, 2, 3), "Hello", "World"] == array


def test_len():
    container = DList()
    for i in range(100):
        container.push_back(i)

    assert len(container) == 100


def test_read_from():
    container = DList()

    with open("tests/input.txt", "r") as file:
        container.read_from(file)

    assert len(container) > 0


def test_write_to():
    container = DList()

    with open("tests/input.txt", "r") as file:
        container.read_from(file)

    with open("tests/output_test_write.txt", "w") as file:
        container.write_to(file)

    file_one = open("tests/output.txt", "r")
    file_two = open("tests/output_test_write.txt", "r")

    assert file_one.read() == file_two.read()

    file_one.close()
    file_two.close()


def test_sort():
    container = DList()

    with open("tests/input.txt", "r") as file:
        container.read_from(file)

    container.sort()
    with open("tests/output_test_sort.txt", "w") as file:
        container.write_to(file)

    file_one = open("tests/output_sort.txt", "r")
    file_two = open("tests/output_test_sort.txt", "r")

    assert file_one.read() == file_two.read()

    file_one.close()
    file_two.close()


def test_write_game_film():
    container = DList()

    with open("tests/input.txt", "r") as file:
        container.read_from(file)

    with open("tests/output_test_write_game_film.txt", "w") as file:
        container.write_game_film_to(file)

    file_one = open("tests/output_game_film.txt", "r")
    file_two = open("tests/output_test_write_game_film.txt", "r")

    assert file_one.read() == file_two.read()

    file_one.close()
    file_two.close()
