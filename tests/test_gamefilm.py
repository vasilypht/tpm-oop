import io

from module import GameFilm


def test_read_from():
    buffer = io.StringIO("Варкрафт\nДункан Джонс\nСША\n")
    film = GameFilm()
    film.read_from(buffer)
    buffer.seek(0)

    assert film.title == "Варкрафт"
    assert film.director == "Дункан Джонс"
    assert film.country == "США"


def test_write_to():
    test_buffer = io.StringIO("This is a game movie.\n"
                              "\tTitle: Варкрафт\n"
                              "\tDirector: Дункан Джонс\n"
                              "\tCountry: США\n"
                              "\tNum of vowels in title: 2\n")
    buffer = io.StringIO()

    film = GameFilm()
    film.title = "Варкрафт"
    film.country = "США"
    film.director = "Дункан Джонс"
    film.write_to(buffer)

    buffer.seek(0)

    assert buffer.read() == test_buffer.read()
