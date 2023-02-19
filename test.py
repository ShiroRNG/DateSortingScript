import os
import configparser

listing = []
config = configparser.ConfigParser()
config['MAIN'] = {}

asd = True

while asd:
    ask = input("??? ")
    if ask == '\\':
        ask.replace("\\", os.path.sep)
    if ask == "F":
        asd = False
    else:
        listing.append(ask)
    for s in listing:
        s.replace('\\\\', os.path.sep)
        
        config.set('MAIN', 'paths', str(s))
    with open('conf.ini', "w") as config_file:
        config.write(config_file)

for key, v in config['MAIN'].items():
    k = v.replace('\\\\', os.path.sep)
    filenames = os.listdir(k)
    print(filenames)



# print(listing)
#
# cocojambo = []
# cocojambo.append(listing)
# print(cocojambo)


















# def checkFiles(path):
#     folderslist = []
#     # print(config['DEFAULT']['paths'])
#     for key, v in config['DEFAULT'].items():
#         # v.replace('\\', os.path.sep)
#         folderslist.append(v)
#         # d = v.replace('\\\\', '\\')
#         # b = v.replace('\\\\', os.path.sep)
#         # print(d)
#         # for pizdec in folderslist:
#         #     pizdec.replace('\\\\', '\\')
#             # print(pizdec)
#         filenames = os.listdir(v)
#         print(filenames)








