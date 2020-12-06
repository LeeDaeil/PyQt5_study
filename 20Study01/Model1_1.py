import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class GpWithBotton:
    def __init__(self):
        # 데이터
        self.x = []
        self.y = []
        # 그래프
        self.fig, self.ax = plt.subplots()
        self.lfig, = self.ax.plot(self.x, self.y, label='Test')
        # 그래프 위 버튼
        # Onstep 버튼
        self.bt = Button(ax=plt.axes([0.7, 0.05, 0.1, 0.075]),
                         label='OneStep')
        self.bt.on_clicked(self._call_click)
        # Read DB 버튼
        self.btr = Button(ax=plt.axes([0.81, 0.05, 0.1, 0.075]),
                         label='Read DB')
        self.btr.on_clicked(self._call_read_click)
        plt.show()

    def _call_click(self, event):
        print(f'Call Event | {event}')
        self.lfig.set_ydata(self.y)
        self.lfig.set_xdata(self.x)
        self.ax.relim()
        self.ax.autoscale_view()
        self.ax.figure.canvas.draw()
        self.ax.legend()

    def _call_read_click(self, event):
        print(f'Call Read Event | {event}')
        print(f'Before\nX:{self.x}\nY:{self.y}')
        self.x.append(len(self.x))
        self.y.append(len(self.y) * 2)
        print(f'After\nX:{self.x}\nY:{self.y}')


if __name__ == '__main__':
    gp = GpWithBotton()