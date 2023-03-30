from PIL import Image, ImageDraw
# ------------
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score


def read_results(filename):
    f = open(filename)
    results = f.read()
    f.close()
    # print(results)
    results = results.split("\n")
    # print(results)

    res = []
    res_int = []

    for i in results:
        if " " in i:
            t = i.split(" ")
            res.append(t)
        if "\t" in i:
            t = i.split("\t")
            res.append(t)
    # print(res)
    for i in res:
        s = []
        for n in i:
            if not n == "":
                k = int(n)
                s.append(k)
        if not s == []:
            res_int.append(s)
    res_all = []
    res1 = []
    res2 = []
    # print(res_int)
    for i in range(0, len(res_int)):
        r1 = res_int[i][0:4]
        r1.sort()
        r2 = res_int[i][4:9]
        r2.sort()
        res_all.append(r1 + r2)
        res1.append(r1)
        res2.append(r2)
    return res1, res2


def resN(arr, N):
    resn = []
    for i in range(len(arr) - N):
        k = 0
        res = []
        while k < N:
            res += arr[i + k]
            k += 1
        resn.append(res)
    return resn


def y_train(arr, minR, maxR, N):
    y = []
    for i in range(minR, maxR):
        y.append(arr[i][N - 1])
    return y


#file_folder = "C:/Matlab_projects/4/python/"
res1, res2 = read_results("results.txt")

# ----
# Пустой желтый фон.
im = Image.new('RGB', (224, 224), (255, 255, 255))


def draw_rectangle(n, m,X0, color):
    x0 = X0 + (n - 1) * 30
    y0 = 7 + (m - 1) * 30
    x1 = x0 + 30
    y1 = y0 + 30
    draw.rectangle((x0, y0, x1, y1), fill=color, outline=(0, 0, 0))


draw = ImageDraw.Draw(im)
color = (255, 255, 255)
for column in range(1, 4):
    for row in range(1, 8):
        draw_rectangle(column, row,15, color)
        draw_rectangle(column, row, 120, color)


def obtain_n_m(num):
    m = 1 + (num - 1) // 3
    n = 3 - (3 * m - num)
    return n, m


def draw_rectangleN(N,X0, color):
    n, m = obtain_n_m(N)
    draw_rectangle(n, m, X0, color)


def draw_arr(arr,X0, color):
    for t in arr:
        draw_rectangleN(t,X0, color)


def draw_res(arr,X0):
    arr_of_color = []
    col1 = 50
    col2 = 50
    color_init = [0, col1, col2]
    for o in range(20):
        arr_of_color.append(color_init)
    draw_arr(arr[0],X0, tuple(color_init))
    if len(arr) > 1:
        for u in range(1, len(arr)):
            for sd in range(len(arr_of_color)):
                arr_of_color[sd] = [a + b for a, b in zip(arr_of_color[sd], [0, 50, 50])]

            for t in arr[u]:
                if t not in arr[u - 1]:
                    colorN = tuple(arr_of_color[t - 1])
                    draw_rectangleN(t,X0, colorN)
                if t in arr[u - 1]:
                    arr_of_color[t - 1] = [a + b for a, b in zip(arr_of_color[t - 1], [50, 100, 75])]
                    colorN = tuple(arr_of_color[t - 1])
                    draw_rectangleN(t,X0, colorN)


draw_res(res1[:5],15)
draw_res(res2[:5],120)
im.show()



for Ni in range(1, 5500):
    image_name = "all/" + str(Ni) + ".jpg"
    draw_res(res1[Ni:Ni + 5],15)
    draw_res(res2[Ni:Ni + 5], 120)
    im.save(image_name, quality=95)
"""    
for ni in range(1, 9):
    exec('labels_{} = []'.format(ni))
    for ni in range(1, 5):
        f = F"labels_{ni}.append(str(res1[Ni-1][{ni - 1}]))"
        exec(f)
    for ni in range(1, 5):
        f = F"labels_{ni+4}.append(str(res2[Ni-1][{ni - 1}]))"
        exec(f)
for ni in range(1, 9):
    #f = F"Labels_{ni} = pd.DataFrame(labels_{ni})"
    #exec(f)
    f = F"file_name = 'labels_{ni}.txt'"
    exec(f)
    import csv

    f = F"with open(file_name, 'w') as output: \n" \
        F" output.write(str(labels_{ni}))"
    #f= F"labels_{ni}.to_csv(file_name, sep='\t')"
    exec(f)
im.show()
"""