import os
import configparser
import shutil
import datetime

listing = []
dict_year = {}
config = configparser.ConfigParser()
config['MAIN'] = {}


def saveconf():
    with open('config.ini', "w") as config_file:
        config.write(config_file)


asd = True

while asd:
    ask1 = input(r"Введите путь к 1 директории: ")
    if ask1 == '-q':
        saveconf()
        break
    else:
        listing.append(ask1)
        for s in listing:
            s.replace('\\\\', os.path.sep)
            config.set('MAIN', 'path1', str(s))
    ask2 = input(r"Введите путь к 2 директории: ")
    if ask2 == '-q':
        saveconf()
        break
    else:
        listing.append(ask2)
        for s in listing:
            s.replace('\\\\', os.path.sep)
            config.set('MAIN', 'path2', str(s))
    ask3 = input(r"Введите путь к 3 директории: ")
    if ask3 == '-q':
        saveconf()
        break
    else:
        listing.append(ask3)
        for s in listing:
            s.replace('\\\\', os.path.sep)
            config.set('MAIN', 'path3', str(s))
    ask4 = input(r"Введите путь к 4 директории: ")
    if ask4 == '-q':
        saveconf()
        break
    else:
        listing.append(ask4)
        for s in listing:
            s.replace('\\\\', os.path.sep)
            config.set('MAIN', 'path4', str(s))
    ask5 = input(r"Введите путь к 5 директории: ")
    if ask5 == '-q':
        saveconf()
        break
    else:
        listing.append(ask5)
        for s in listing:
            s.replace('\\\\', os.path.sep)
            config.set('MAIN', 'path5', str(s))
    saveconf()
    break


def filenames():
    for k, v in config['MAIN'].items():
        filenames = os.listdir(v)
        time = datetime.datetime.fromtimestamp(os.path.getmtime(v))
        for file in filenames:
            file_time = time
            file_date = file_time.strftime('%d %m %Y')
            dict_year[file] = file_date


filenames()
print(dict_year)


def path():
    for k, v in config['MAIN'].items():
        return v

path()

for key, value in dict_year.items():
    if not os.path.exists(f'{path()}{os.path.sep}{value}'):
        os.mkdir(f'{path()}{os.path.sep}{value}')
    filename = key
    if not os.path.exists(f'{path()}{os.path.sep}{value}{os.path.sep}{filename}'):
        print(f'{path()}{os.path.sep}{value}{os.path.sep}{filename}')
        if os.path.isfile(key):
            shutil.move(key, f'{path()}{os.path.sep}{value}{os.path.sep}{filename}')
        elif os.path.isdir(key):
            if key != value:
                shutil.copytree(key, f'{path()}{os.path.sep}{value}{os.path.sep}{filename}')
                shutil.rmtree(key)
            elif key == value:
                continue

# def t_file():
#     for k, v in config['MAIN'].items():
#         return datetime.datetime.fromtimestamp(os.path.getmtime(v))
#
# for file in filenames:
#     file_time = t_file(file)
#     file_date = file_time.strftime('%d %m %Y')
#     dict_year[file] = file_date
