from tkinter import *
from tkinter import messagebox
import random
import csv

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)        # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()
        self.n=False                    #是否开始了抽选的逻辑开关，False表示还没开始抽
        self.zjr=[]                     #本次抽选的中奖人名单，放入数组zjr中
        #本期抽奖的候选者名单
        self.mingdan=self.lordmd()

    #读取候选名单的方法
    def lordmd(self):
        headers=[]
        with open(r"mingdan.csv")as csv_file:
            csv_reader=csv.reader(csv_file)
            for row in csv_reader:
                for ge in row:
                    headers.append(ge)
        print(headers)
        return headers



    #开始抽选的方法
    def chouxuan(self):
        self.n=True
        self.xianshi()

    #停止抽选的方法
    def stop(self):
        if self.n:     #检查是否已经按下开始抽选
            try:
                self.n=False                      #停止抽选后停掉逻辑开关将显示停止下来
                self.zjr.append(self.label01["text"])       #将当年显示上的候选人加入中奖名单
                self.mingdan.remove(self.label01["text"])   #已经成为中奖人的从候选名单里面删除掉，当mingdan列表为空时抛出异常
                self.label02["text"] = "中奖人:" + ','.join(self.zjr)   #将中奖名单的数组转换成字符串后输出到中奖标签
            except BaseException as e:
                self.cuowu2()
                print(e)
            return self.label01["text"]
        else:          #如果未开始抽选就停止即提示错误
            print("请先点击开始抽选再点击停止抽选")
            self.cuowu()

    #抽选时的面板显示方法
    def xianshi(self):
        if self.n:                      #检查开始抽选是否被按下
            try:
                a = random.choice(self.mingdan)     #从候选名单列表中随机选一个元素
                self.label01["text"] = a            #将这个随机元素赋予给标签1用于显示
                self.label01.after(50, self.xianshi)  #50毫秒后循环函数xianshi
            except BaseException as e:               #等抽选人名单列表mingdan为空的时候会抛出异常
                self.cuowu2()                        #当出现异常是用信息框提醒
                print(e)

        else:
            return self.label01["text"]

    def cuowu(self):        #为先点击开始的错误提示
        messagebox.showinfo("错误提示","请先点击开始抽选再点击停止抽选")

    def cuowu2(self):        #为先点击开始的错误提示
        messagebox.showinfo("错误提示","所有候选人已经抽完，如需重新抽选请关闭程序重新开始抽选")


    def createWidget(self):
        """创建组件"""
        self.label01=Label(self.master,text="候选人",fg='black',bg='white',font=("微软雅黑",20),width=10,height=3)
        self.button01=Button(self.master,text="开始抽选",command=self.chouxuan,fg='black',bg='white',font=("微软雅黑",10),width=8,height=1)
        self.button02=Button(self.master,text="停止抽选",command=self.stop,fg='black', bg='white',font=("微软雅黑",10), width=8, height=1)
        self.label02=Label(self.master,text="中奖人",fg='black',bg='white',font=("微软雅黑",10),width=30,height=3)
        self.label01.pack(side='top', expand='yes', fill='both')
        self.label02.pack(side='bottom', expand='yes', fill='both')
        self.button01.pack(side='left',expand='yes',anchor='e')
        self.button02.pack(side='right',expand='yes',anchor='w')


if __name__ == '__main__':
    root = Tk()
    # 设置标题
    root.title('幸运抽奖机GUI程序')
    # 设置窗口大小
    width = 400
    height = 300
    # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2 , (screenheight - height)/2)
    root.geometry(alignstr)
    # 设置窗口是否可变长、宽，True：可变，False：不可变
    root.resizable(width=True, height=True)
    app = Application(master=root)
    root.mainloop()