# TODO Найдите количество книг, которое можно разместить на дискете

size_disk = 1.44 * 1024 ** 2  # размер дискеты
pages_ = 100  # количество страниц
str_on_pages = 50  # число строк на странице
symbols_on_pages = 25  # количество символов в строке

symbols_in_the_book = pages_ * str_on_pages * symbols_on_pages  # количество всех символов в книге
size_symbols_in_the_book = symbols_in_the_book * 4  # сколько байт занимают символы


print("Количество книг, помещающихся на дискету:", int(size_disk // size_symbols_in_the_book))
