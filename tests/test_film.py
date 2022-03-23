import io

import pytest

from module import Film, GameFilm, Cartoon, Documentary, WayToCreate


def test_read_from():
    buffer = io.StringIO("США")
    film = Film()
    film.read_from(buffer)
    buffer.seek(0)

    assert film.country == buffer.read()


def test_write_to():
    buffer = io.StringIO()

    film = Film()
    film.title = "Варкрафт"
    film.country = "США"
    film.write_to(buffer)

    buffer.seek(0)

    test_str = f"\tCountry: {film.country}\n" \
               f"\tNum of vowels in title: {film.num_vowels_in_title()}\n"

    assert buffer.read() == test_str


@pytest.mark.parametrize("buffer,obj", [
    (io.StringIO("1\nВаркрафт\nДункан Джонс\nСША\n"), GameFilm),
    (io.StringIO("2\nУоллес и Громит: Неправильные штаны\n3\nВеликобритания\n"), Cartoon),
    (io.StringIO("3\nПод лёд\n2019\nРоссия\n"), Documentary)
])
def test_create_from(buffer, obj):
    line = buffer.readline()
    film = Film.create_from(buffer, line)
    assert isinstance(film, obj)


@pytest.mark.parametrize("string,count", [
    ("Варкрафт", 2),
    ("Уоллес и Громит: Неправильные штаны", 13),
    ("Под лёд", 2)
])
def test_num_vowels_in_title(string, count):
    film = Film()
    film.title = string
    assert film.num_vowels_in_title() == count
