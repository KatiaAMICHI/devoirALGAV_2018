import os
import sys

import numpy as np
from bokeh.plotting import figure, show

from src.main.hach import MD5

if sys.version_info.major == 2:
    pass
else:
    pass
if sys.version_info.major == 2:
    pass
else:
    pass
if sys.version_info.major == 2:
    pass
else:
    pass

PATH_cles_alea = r'../../res/cles_alea/'
PATH_Shakespeare = r'../../res/Shakespeare/'
pathShakespeare_file = '../../res/Shakespeare/titus.txt'


def inf(l1, l2, deb, fin):
    if (isinstance(l1, np.int64) or isinstance(l1, np.int)) and (isinstance(l2, np.int64) or isinstance(l2, np.int)):
        return l1 < l2
    if l1 == l2:
        return False  # 'equel'
    if int(l1[deb:fin], base=16) > int(l2[deb:fin], base=16):
        return False
    elif int(l1[deb:fin], base=16) < int(l2[deb:fin], base=16):
        return True
    else:
        inf(l1, l2, deb + 8, fin + 8)


def sup(l1, l2, deb, fin):
    if (isinstance(l1, np.int64) or isinstance(l1, np.int)) and (isinstance(l2, np.int64) or isinstance(l2, np.int)):
        return l1 > l2
    if l1 == l2:
        return False  # 'equel'
    if int(l1[deb:fin], base=16) > int(l2[deb:fin], base=16):
        return True
    elif int(l1[deb:fin], base=16) < int(l2[deb:fin], base=16):
        return False
    else:
        inf(l1, l2, deb + 8, fin + 8)


# y_range = (list(sortDic.values())[0], list(sortDic.values())[len(list(sortDic.values())) - 1]),
# 1/2

def plot3(sortDic1, sortDic2, sortDic3, n1='n1', n2='n2', n3='n3', name='plot'):
    max_x = max(2,
                int(list(sortDic2.keys())[len(list(sortDic1.keys())) - 1]),
                int(list(sortDic3.keys())[len(list(sortDic1.keys())) - 1]))
    max_y = list(sortDic1.values())[len(list(sortDic1.values())) - 1]
    p = figure(title=name, y_axis_type="log",
               x_range=(0, max_x),
               y_range=(list(sortDic1.values())[0], max_y + 1),
               background_fill_color="#fafafa")

    p.line(list(sortDic1.keys()), list(sortDic1.values()), legend=n1)
    p.circle(list(sortDic1.keys()), list(sortDic1.values()), legend=n1)

    p.line(list(sortDic2.keys()), list(sortDic2.values()), legend=n2,
           line_color="gold", line_width=2)

    p.line(list(sortDic3.keys()), list(sortDic3.values()), legend=n3,
           line_color="coral", line_dash="dotdash", line_width=2)

    p.legend.location = "top_left"

    show(p)


def plot4(sortDic0, sortDic1, sortDic2, sortDic3, n0='n0', n1='n1', n2='n2', n3='n3', name='plot'):
    max_x = max(2,
                int(list(sortDic0.keys())[len(list(sortDic0.keys())) - 1]),
                int(list(sortDic1.keys())[len(list(sortDic1.keys())) - 1]),
                int(list(sortDic2.keys())[len(list(sortDic2.keys())) - 1]),
                int(list(sortDic3.keys())[len(list(sortDic3.keys())) - 1]))
    max_y = list(sortDic1.values())[len(list(sortDic1.values())) - 1]
    p = figure(title=name,
               x_range=(0, max_x),
               y_range=(list(sortDic1.values())[0], max_y),
               background_fill_color="#fafafa")
    # y_axis_type = "log",
    p.line(list(sortDic0.keys()), list(sortDic0.values()), legend=n0,
           line_color="gold", line_width=2)

    p.line(list(sortDic1.keys()), list(sortDic1.values()), legend=n1)
    p.circle(list(sortDic1.keys()), list(sortDic1.values()), legend=n1)

    p.line(list(sortDic2.keys()), list(sortDic2.values()), legend=n2,
           line_color="navy", line_width=2)

    p.line(list(sortDic3.keys()), list(sortDic3.values()), legend=n3,
           line_color="coral", line_dash="dotdash", line_width=2)

    p.legend.location = "top_left"

    show(p)


def plot(sortDic, name="plot"):
    p = figure(title=name,
               x_range=(0, int(list(sortDic.keys())[len(list(sortDic.keys())) - 1])),
               y_range=(list(sortDic.values())[0], list(sortDic.values())[len(list(sortDic.values())) - 1] + len(
                   list(sortDic.keys()))),
               background_fill_color="#fafafa")

    p.line(list(sortDic.keys()), list(sortDic.values()), legend="",
           line_color="tomato", line_dash="dashed")

    p.legend.location = "top_left"

    show(p)


def lectureFicher(file=None):
    if file is None:
        file = pathShakespeare_file
    f = open(file, 'r', newline="\n")
    data = f.read().rstrip().split()
    return data

def fichiers_ShakespeareMD5_file(file=None):
    if file is None:
        file = pathShakespeare_file
    data_dic = {}
    data = []
    dataMD5 = []
    md5 = MD5()
    f = open(file, 'r', newline="\n")
    data = f.read().rstrip().split()
    for word in data:
        dataMD5.append(md5.md5_to_hex(md5.md5(word.encode())))
    print(dataMD5)
    return dataMD5


def fichiers_ShakespeareMD5():
    data_dic = {}
    data = []

    md5 = MD5()
    for file in os.listdir(PATH_Shakespeare):
        f = open(PATH_Shakespeare + file, 'r', newline="\n")
        data = f.read().rstrip().split()
        for word in data:
            try:
                data_dic[str(len(data))].append(md5.md5_to_hex(md5.md5(word.encode())))
            except:
                data_dic[str(len(data))] = [md5.md5_to_hex(md5.md5(word.encode()))]

    return data_dic


def Shakespeare(path=None):
    if path is None:
        path = PATH_Shakespeare
    words = []
    for file in os.listdir(path):
        f = open(path + file, 'r', newline="\n")
        words.extend(f.read().rstrip().split())
    return words


def FileReader(path=None):
    if path is None:
        path = PATH_cles_alea
    l1_dic = {}

    l1_dic['100'] = []
    l1_dic['200'] = []
    l1_dic['500'] = []
    l1_dic['1000'] = []
    l1_dic['5000'] = []
    l1_dic['10000'] = []
    l1_dic['20000'] = []
    l1_dic['50000'] = []
    # print('le path : ', os.getcwd())
    for element in os.listdir(path):
        if element.endswith('100.txt'):
            f1 = open(path + str(element), 'r')
            lignes1 = f1.readlines()
            f1.close()
            for i in lignes1:
                l1_dic['100'].append(i[2:].rstrip())
            f1.close()
        elif element.endswith('200.txt'):
            f1 = open(path + str(element), 'r')
            lignes1 = f1.readlines()
            f1.close()
            for i in lignes1:
                l1_dic['200'].append(i[2:].rstrip())
            f1.close()

        elif element.endswith('_500.txt'):
            f1 = open(path + str(element), 'r')
            lignes1 = f1.readlines()
            f1.close()
            for i in lignes1:
                l1_dic['500'].append(i[2:].rstrip())
            f1.close()

        elif element.endswith('1000.txt'):
            f1 = open(path + str(element), 'rb')
            lignes1 = f1.readlines()
            f1.close()
            for i in lignes1:
                l1_dic['1000'].append(i[2:].rstrip())
            f1.close()

        elif element.endswith('2000.txt'):
            f1 = open(path + str(element), 'r')
            lignes1 = f1.readlines()
            f1.close()
            for i in lignes1:
                l1_dic['2000'].append(i[2:].rstrip())
            f1.close()

        elif element.endswith('5000.txt'):
            f1 = open(path + str(element), 'r')
            lignes1 = f1.readlines()
            f1.close()
            for i in lignes1:
                l1_dic['5000'].append(i[2:].rstrip())
            f1.close()

        elif element.endswith('10000.txt'):
            f1 = open(path + str(element), 'r')
            lignes1 = f1.readlines()
            f1.close()
            for i in lignes1:
                l1_dic['10000'].append(i[2:].rstrip())
            f1.close()

        elif element.endswith('20000.txt'):
            f1 = open(path + str(element), 'r')
            lignes1 = f1.readlines()
            f1.close()
            for i in lignes1:
                l1_dic['20000'].append(i[2:].rstrip())
            f1.close()

        elif element.endswith('50000.txt'):
            f1 = open(path + str(element), 'r')
            lignes1 = f1.readlines()
            f1.close()
            for i in lignes1:
                l1_dic['50000'].append(i[2:].rstrip())
            f1.close()

    return l1_dic
