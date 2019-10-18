#coding=utf-8
#摆放家具需求
class Room():
    #属性：户型、总面积、剩余面积、家具名称列表
    def __init__(self,apartment,total_area,*furnitures):
        self.apartment = apartment
        self.total_area = float(total_area)
        #根据家具占用面积计算剩余面积
        self.furnitures = furnitures

    #房子的剩余面积计算
    def count_area(self):
        #循环将家具所占面积求和
        self.residual_area = self.total_area
        if self.furnitures == None:
            self.residual_area = self.total_area
        else:
            for furniture in self.furnitures:
                if furniture == "床":
                    self.residual_area -= 4
                elif furniture == "衣柜":
                    self.residual_area -= 2
                elif furniture == "餐桌" :
                    self.residual_area -= 1.5

        return self.residual_area

    #打印房子
    def print_roominfo(self):
        #self.residual_area = self.count_area()
        if self.furnitures == "":
            print('户型：' + self.apartment + '\n总面积：' + str(self.total_area) + '平方米' + '\n剩余面积：' + str(self.count_area()))
        else:
            print('户型：' + self.apartment+'\n总面积：'+ str(self.total_area) + '平方米' +'\n剩余面积：' + str(self.count_area()) + '\n家具名称:' + str(self.furnitures))#+ self.furnitures

furniture = ['床','衣柜','餐桌']
myroom = Room('三室一厅','100',*furniture)
myroom.print_roominfo()

