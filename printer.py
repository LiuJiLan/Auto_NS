import math
import numpy as np

MAX_DISTENCE = 9999  # 对角线最远, 320 + 120 = 440


class Printer:
    def __init__(self, array):
        self.plan = []
        self.array = array

    def main(self):
        self.plan_path()

        try:
            self.draw()
        except Exception as e:
            np.savetxt("./fail.csv", self.array, delimiter=",", fmt='%d')
        finally:
            exit()

    def draw(self):
        prev_dot = Dot(0, 0)
        for dot in self.plan:
            self.move(prev_dot, dot)
            self.mark(dot)
            self.print()
            prev_dot = dot

    def plan_path(self):
        array = np.array(self.array, dtype="int8")
        cur_dot = Dot(0, 0)

        while True:
            if 0 not in array:
                return

            next_dot = self.find_nearest(cur_dot, array)
            self.plan.append(next_dot)
            array[next_dot.y, next_dot.x] = 1
            cur_dot = next_dot

    def find_nearest(self, dot, array):
        if self.array[dot.y, dot.x] == 0:
            return dot

        dist = np.zeros(shape=array.shape, dtype='float')
        for y in range(array.shape[0]):
            for x in range(array.shape[1]):
                if array[y, x] == 0:
                    dist[y, x] = dot.dist(x, y)
                else:
                    dist[y, x] = MAX_DISTENCE

        nearest_y, nearest_x = np.where(dist == np.min(dist))
        return Dot(nearest_x, nearest_y)

    def move(self, prev, tar):
        delta_x = tar.x - prev.x
        delta_y = tar.y - prev.y

        if delta_x == 0 and delta_y == 0:
            return

        if delta_x > 0:
            for _ in range(delta_x):
                self.move_r()
        else:
            delta_x = abs(delta_x)
            for _ in range(delta_x):
                self.move_l()

        if delta_y > 0:
            for _ in range(delta_y):
                self.move_u()
        else:
            delta_y = abs(delta_y)
            for _ in range(delta_y):
                self.move_d()

    def mark(self, dot):
        self.array[dot.y, dot.x] = 1

    def move_u(self):
        pass

    def move_d(self):
        pass

    def move_l(self):
        pass

    def move_r(self):
        pass

    def print(self):
        pass


class Dot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, x, y):
        if x == self.x and y == self.y:
            return 0

        # 得出由self指向(x, y)的向量
        vec_x = x - self.x
        vec_y = self.y - y
        # y要反转, 因为是向下生长的

        # 顺时针旋转90度, 但是y反转所以逆时针90
        v_x_ = -vec_y  # v_x_ => Vec x'
        v_y_ = vec_x
        perfer = (math.atan2(v_y_, v_x_) + math.pi) / math.pi / 2

        return abs(vec_x) + abs(vec_y) + perfer
