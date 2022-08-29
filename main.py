import serial
from PIL import Image  # cv2本地崩了, 而且cv2要自己调阈值
import numpy as np
import matplotlib.pyplot as plt
from controller import Controller


def save_picture_as_text():
    im = Image.open("./default.png")
    im = im.convert("1")
    # im.show()
    im_array = np.array(im)
    # im_array = limit_shape(im_array)
    # im_array.shape # y轴, x轴
    np.savetxt("./pic_text.csv", im_array, delimiter=",", fmt='%d')
    # print(im_array[0].shape) # [0..., :]是纵向， 包含每个[?, :]
    # print(im_array[0, 0]) # True对应的是白色


def limit_shape(im):
    y = min(im.shape[0], 120)
    x = min(im.shape[1], 320)
    return im[:y, :x]


def load_pic_from_text():
    im_array = np.genfromtxt("./pic_text.csv", delimiter=',').astype(np.uint8)
    Image.fromarray(im_array * 255).show()
    return im_array


def draw(im, ctr):
    shape_y, shape_x = im.shape
    for y in range(int(shape_y / 2)):
        x = 0

        while x < shape_x:
            if im[2 * y, x] == 0:
                ctr.A()
            x += 1
            if x < shape_x:
                ctr.r()

        ctr.d()

        print(2 * y)

        while x > 0:
            x -= 1
            if im[2 * y + 1, x] == 0:
                ctr.A()
            if x != 0:
                ctr.l()

        ctr.d()

        print(2 * y + 1)

    ctr.p()

def draw2(im, ctr):
    shape_y, shape_x = im.shape
    for y in range(41, int(shape_y / 2)):
        x = 0

        while x < shape_x:
            if im[2 * y, x] == 0:
                ctr.A()
            x += 1
            if x < shape_x:
                ctr.r()

        ctr.d()

        while x > 0:
            x -= 1
            if im[2 * y + 1, x] == 0:
                ctr.A()
            if x != 0:
                ctr.l()

        ctr.d()

    ctr.B()
    #ctr.p()


def prepare(ctr_ins):
    ctr_ins.LS()  # 清屏
    ctr_ins.L()  # 调整画笔大小

    # 画笔归位到左上角
    ctr_ins.ls_l(5)
    ctr_ins.ls_u(5)


if __name__ == '__main__':
    # ctr = Controller()
    #ctr.LR(5)
    #ctr.A()
    #ctr.h()

    #ctr.B()
    #save_picture_as_text()
    # im = load_pic_from_text()

    #
    # prepare(ctr)
    #test_im = im_array = np.asarray([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], dtype='int8')
    #draw(test_im, ctr)

    # draw(im, ctr)
    #draw2(im, ctr)
    pass

    from printer import Dot

    dot = Dot(2, 2)

    for y in range(5):
        for x in range(5):
            print(x, ", ", y, " : ", end="")
            print(dot.dist(x, y))
