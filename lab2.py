from xml.dom.minidom import *

def parse() -> dict:
    data = {}
    for i, row in enumerate(open('books.csv', encoding='cp1251')):
        if i == 0:
            headers = tuple(map(lambda x: x.strip(), row.split(';')[1:]))
            continue

        row = row.split(';')
        data[row[0]] = {}
        for p, header in enumerate(headers, start=1):
            data[row[0]][header] = row[p].strip()

    return data


def printlen(data:dict) -> int:
    counter = 0
    for book in data.values():
        if len(book['Название']) > 30: counter += 1
    return counter


def search(data:dict) -> list:
    result = []
    print('Поиск книги от 2016 до 2018 года по автору')
    request = input('Введите имя автора: ')
    for book in data.values():
        if request.lower() in f'{book["Автор"]}{book["Автор (ФИО)"]}'.lower():
            date = int(book['Дата поступления'].split(' ')[0].split('.')[2])
            if date in range(2016, 2019): result.append((book["Автор"], book['Название']))
    return result


def xmlParse() -> list:
    rawFile = open('currency.xml', 'r', encoding='cp1251').read()
    parsedData = parseString(rawFile)
    parsedData.normalize()
    elements = parsedData.getElementsByTagName('Valute')
    result = []
    for node in elements:
        tmp = [0, 0]
        for child in node.childNodes:
            match child.tagName:
                case 'CharCode':
                    tmp[0] = child.firstChild.data
                case 'Nominal':
                    tmp[1] = int(child.firstChild.data)
        if tmp[1] in (10, 100): result.append(tmp[0])
    return result


def allTags(data:list) -> set:
    tags = set()
    for book in data.values():
        bookTags = list(map(lambda x: x.strip(), book['Жанр книги'].split('#')))
        tags.update(bookTags)
    return tags


def topBooks(data:list) -> list:
    books = [(book["Автор"], book["Название"], book["Кол-во выдач"]) for book in data.values()]
    books.sort(key=lambda x: -int(x[2]))
    return books[:20]


def start():
    parsedXML = xmlParse()
    print('Список CharCode, но только для валют с Nominal=10 или Nominal=100:', *parsedXML, end='\n\n')

    data = parse()
    print(f'Количество записей, у которых в поле "Название" строка длиннее 30 символов: {printlen(data)} \n')

    tags = allTags(data)
    print(f'Все теги: ', end='')
    print(*tags, sep=', ', end='\n\n')

    print('Топ 20 популярных книг: ')
    [print(f'{book[0]} - {book[1]}') for book in topBooks(data)]
    print()

    searched_books = search(data)
    if searched_books == []: print('По вашему запросу ничего не нашлось')
    else: [print(f'{book[0]} - {book[1]}') for book in searched_books]

if __name__ == '__main__':
    start()





