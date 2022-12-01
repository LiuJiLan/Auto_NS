import serial
from PIL import Image  # cv2本地崩了, 而且cv2要自己调阈值
import numpy as np
import matplotlib.pyplot as plt
from controller import Controller


def save_picture_as_text(path="./img/test_08.png"):
    im = Image.open(path)
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


def load_pic_from_text(path="./pic_text.csv"):
    im_array = np.genfromtxt(path, delimiter=',').astype(np.uint8)
    Image.fromarray(im_array * 255).show()
    return im_array


from printer import Printer


class NSPrinter(Printer):
    def __init__(self, im, ctr):
        super(NSPrinter, self).__init__(im)
        self.ctr = ctr

    def move_u(self):
        self.ctr.u()

    def move_d(self):
        self.ctr.d()

    def move_l(self):
        self.ctr.l()

    def move_r(self):
        self.ctr.r()

    def print(self):
        self.ctr.A()


def prepare(ctr_ins):
    ctr_ins.LS()  # 清屏
    ctr_ins.L()  # 调整画笔大小

    # 画笔归位到左上角
    ctr_ins.ls_l(5)
    ctr_ins.ls_u(5)


if __name__ == '__main__':
    # ctr = Controller()
    # ctr.LR()
    # ctr.A()
    # ctr.h()

    # ctr.L()
    # ctr.m()
    # ctr.l(1)
    # ctr.u(1)

    # ctr.B()
    # save_picture_as_text("./img/test_08.png")
    # im = load_pic_from_text("./auto_save.csv")
    im = load_pic_from_text()

    #
    # prepare(ctr)
    # test_im = im_array = np.asarray([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], dtype='int8')

    # prt = NSPrinter(im, ctr)
    # prt.main()
    # ctr.m()

    pass
