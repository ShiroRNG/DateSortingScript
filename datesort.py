import platform
import os
from shutil import move
import configparser
import datetime

listing = []
config = configparser.ConfigParser()
config['MAIN'] = {}

opsys = platform.system()
if opsys == "Windows" or "Linux":
    operating_system = 'win/linux'
else:
    operating_system = 'nix'


def saveconf():
    # Сохраняет конфиг в случае внесения изменений в него
    with open('datesortconfig.ini', "w") as config_file:
        config.write(config_file)


def start_menu():
    '''Стартовая функция. Проверяет наличие конфига. В случае его отсутствия, предлагает создать новый,
    либо закрыть скрипт. При выборе создания нового конфига, вызывается функция для его создания,
    заполняется желаемое кол-во дерикторий, после чего, функция вызывает саму себя, чтобы снова
    проверить наличие конфига. При условии наличия конфига, запускается основная функция.'''

    if not os.path.exists('datesortconfig.ini'):
        ask1 = input('Необходимо создать конфиг. Начать? y/n ')
        if ask1.lower() == 'n':
            exit()
        elif ask1.lower() == 'y':
            newConfig()
            start_menu()
        else:
            start_menu()
    else:
        ask = input('Начать сортировку? y/n ')
        if ask.lower() == 'y':
            getting()
        elif ask.lower() == 'n':
            exit()
        else:
            start_menu()


def newConfig():
    '''Функция создания конфига. На нее перебрасывает после стартовой функции. Стоит счетчик, который позволяет ввести
    любое кол-во путей и сохранить их в конфиг. Пути сохраняются в список, после чего каждый из них перебрасывается
    в конфиг под названием path1, path2 и т.д. Прервать работу функции и сохранить записанные пути можно двумя
    способами - с помощью пустой строки и написания -q'''

    counter = 0
    while True:
        counter += 1
        ask1 = input(f"Закончить -q. Введите путь к {counter} директории: ")
        if ask1 == '':
            saveconf()
            break
        elif ask1.lower() == '-q':
            saveconf()
            break
        else:
            listing.append(ask1)
            for s in listing:
                s.replace('\\\\', os.path.sep)
                config.set('MAIN', 'path' + str(counter), str(s))
    saveconf()


config.read('datesortconfig.ini')

def lw_file(file):
    # Получает дату модификации файла/дериктории
    return datetime.datetime.fromtimestamp(os.path.getmtime(file))

def mac_file(file):
    # Получает дату создания файла/дериктории
    return datetime.datetime.fromtimestamp(os.stat(file).st_birthtime)


def sort_time(path):
    filenames = os.listdir(path)
    for files in filenames:
        full_path = os.path.join(path, files)
        if operating_system == 'win/linux':
            file_time = lw_file(full_path)
            year_date = file_time.strftime('%Y')
            month_date = file_time.strftime('%m')
            full_sorting(path, files, year_date, month_date, full_path)
        else:
            file_time = mac_file(full_path)
            year_date = file_time.strftime('%Y')
            month_date = file_time.strftime('%m')
            full_sorting(path, files, year_date, month_date, full_path)

def full_sorting(path, file, year_date, month_date, full_path):
    if not os.path.exists(f'{path}{os.path.sep}{year_date}'):
        os.mkdir(f'{path}{os.path.sep}{year_date}')
    if not os.path.exists(f'{path}{os.path.sep}{year_date}{os.path.sep}{month_date}'):
        os.mkdir(f'{path}{os.path.sep}{year_date}{os.path.sep}{month_date}')
    if not os.path.exists(f'{path}{os.path.sep}{year_date}{os.path.sep}{month_date}{os.path.sep}{file}'):
        if os.path.isfile(full_path):
            move(full_path, f'{path}{os.path.sep}{year_date}{os.path.sep}{month_date}{os.path.sep}{file}')
        elif os.path.isdir(full_path):
            None

def getting():
    '''Основная функция. Проходится по файлу конфигурации с помощью цикла и счетчика.
    Все находящиеся пути в конфиге попадают в список. Цикл прекращается, когда обойдет весь конфиг.
    После чего, с помощью цикла for, в списке перебирается каждый из указанных путей, постепенно вызывая
    необходимые функции. После заверешения сортировки одной из директорий, очищает словарь,
    начинается следующая итерация'''

    count = 0
    lists = []
    while True:
        try:
            count += 1
            getterg = config.get('MAIN', 'path' + str(count))
            lists.append(getterg)
        except configparser.NoOptionError:
            break
    try:
        for path in lists:
            os.chdir(path)
            sort_time(path)
    except FileNotFoundError:
        print(f'Путь до {path} не найден')

if __name__ == "__main__":
    start_menu()


