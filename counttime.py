# https://www.jianshu.com/p/0b5dfd0f6fd7
from tkinter import *
from datetime import datetime


class TestTime(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('800x300')
        self.root.resizable(width=True, height=True)
        self.updatetime()

    def updatetime(self):
        self.labelA = Label(self.root, font='楷体 -60 bold', foreground='red')
        self.labelA.pack()
        self.labelF = Label(self.root, text="")
        self.labelF.pack()

        self.updateA()

    def updateA(self):
        # self.now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        future = datetime(2022, 8, 8, 18, 0, 0)
        now = datetime.now()
        diff = future - now
        day = diff.days
        hour = diff.seconds // 3600
        minute = (diff.seconds % 3600) // 60
        second = (diff.seconds % 3600) % 60
        text = "HY结束倒计时：\r\r{}天{}小时{}分{}秒".format(day, hour, minute, second).strip()
        self.labelA.configure(text=text, bg='#BFEFFF',) #bg='#BFEFFF',
        self.root.after(1000, self.updateA)


if __name__ == '__main__':
    root = Tk()
    root.title('HY倒计时')
    root.configure(bg='#BFEFFF',)
    # 窗口置顶.
    root.wm_attributes('-topmost', 1)
    TestTime(root)
    root.mainloop()

