import io

from module import Cartoon, WayToCreate


def test_read_from():
    buffer = io.StringIO("Уоллес и Громит: Неправильные штаны\n3\nВеликобритания\n")
    film = Cartoon()
    film.read_from(buffer)
    buffer.seek(0)

    assert film.title == "Уоллес и Громит: Неправильные штаны"
    assert film.way_to_create == WayToCreate(3)
    assert film.country == "Великобритания"


def test_write_to():
    test_buffer = io.StringIO("This is a cartoon.\n"
                              "\tTitle: Уоллес и Громит: Неправильные штаны\n"
                              "\tWay to create: plasticine\n"
                              "\tCountry: Великобритания\n"
                              "\tNum of vowels in title: 13\n")
    buffer = io.StringIO()

    film = Cartoon()
    film.title = "Уоллес и Громит: Неправильные штаны"
    film.country = "Великобритания"
    film.way_to_create = WayToCreate(3)
    film.write_to(buffer)

    buffer.seek(0)

    assert buffer.read() == test_buffer.read()
