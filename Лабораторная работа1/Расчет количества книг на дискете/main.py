# TODO Найдите количество книг, которое можно разместить на дискете
Count_page = 100
Count_str = 50
Count_Sym = 25
size_disket = 1024**2 * 1.44

All_Sym = Count_page * Count_str * Count_Sym
size_book = All_Sym * 4 #байты
count_book = int(size_disket // size_book)
print("Количество книг, помещающихся на дискету:", count_book)
