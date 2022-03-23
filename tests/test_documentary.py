import io

from module import Documentary


def test_read_from():
    buffer = io.StringIO("Под лёд\n2019\nРоссия\n")
    film = Documentary()
    film.read_from(buffer)
    buffer.seek(0)

    assert film.title == "Под лёд"
    assert film.year_of_issue == 2019
    assert film.country == "Россия"


def test_write_to():
    test_buffer = io.StringIO("This is a documentary.\n"
                              "\tTitle: Под лёд\n"
                              "\tYear of issue: 2019\n"
                              "\tCountry: Россия\n"
                              "\tNum of vowels in title: 2\n")
    buffer = io.StringIO()

    film = Documentary()
    film.title = "Под лёд"
    film.country = "Россия"
    film.year_of_issue = 2019
    film.write_to(buffer)

    buffer.seek(0)

    assert buffer.read() == test_buffer.read()
