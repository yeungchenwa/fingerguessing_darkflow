from caiquan import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from PyQt5.QtCore import QTimer,QCoreApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QFile
import cv2
import qimage2ndarray
import time
from darkflow.net.build import TFNet



class CamShow(QMainWindow,Ui_MainWindow):
    def __del__(self):
        try:
            self.camera.release()  # 释放资源
        except:
            return

    def __init__(self,parent=None):
        super(CamShow,self).__init__(parent)
        self.setupUi(self)
        self.PrepWidgets()
        self.PrepParameters()
        self.CallBackFunctions()
        #self.Timer=QTimer()
        #self.Timer.timeout.connect(self.TimerOutFun)


    def PrepWidgets(self):
        #self.PrepCamera()
        self.fanhui.setEnabled(False)

    #def PrepCamera(self):
        #try:
            #self.camera=cv2.VideoCapture(1)
            #self.jieguo.clear()
            #self.jieguo.append('正在连接摄像头...')
            #self.jieguo.append('正在连接摄像头...')
        #except Exception as e:
            #self.jieguo.clear()
            #self.jieguo.append(str(e))

    def PrepParameters(self):
        self.jieguo.clear()
        self.RecordFlag = 0
        self.Image_num = 0

    def CallBackFunctions(self):
        self.shuangren.clicked.connect(self.StartCamera2)
        self.sanren.clicked.connect(self.StartCamera3)
        self.siren.clicked.connect(self.StartCamera4)
        self.fanhui.clicked.connect(self.Gotoinit)
        #self.jilu.clicked.connect(self.Zhanji)
        self.jieshu.clicked.connect(self.ExitApp)


    def StartCamera2(self):
        self.shuangren.setEnabled(False)
        self.sanren.setEnabled(True)
        self.siren.setEnabled(True)
        self.jilu.setEnabled(True)
        self.fanhui.setEnabled(True)
        self.jieshu.setEnabled(True)
        #self.Timer.start(1)
        #self.timelb=time.clock()

        self.Shuangren()



    def StartCamera3(self):
        self.shuangren.setEnabled(True)
        self.sanren.setEnabled(False)
        self.siren.setEnabled(True)
        self.jilu.setEnabled(True)
        self.fanhui.setEnabled(True)
        self.jieshu.setEnabled(True)
        #self.Timer.start(1)
        #self.timelb=time.clock()
        self.Sanren()

    def StartCamera4(self):
        self.shuangren.setEnabled(True)
        self.sanren.setEnabled(True)
        self.siren.setEnabled(False)
        self.jilu.setEnabled(True)
        self.fanhui.setEnabled(True)
        self.jieshu.setEnabled(True)
        self.Timer.start(1)
        self.timelb=time.clock()
        self.Siren()



    def Gotoinit(self):
        self.shuangren.setEnabled(True)
        self.sanren.setEnabled(True)
        self.siren.setEnabled(True)
        self.jilu.setEnabled(True)
        self.fanhui.setEnabled(False)
        self.jieshu.setEnabled(True)
        self.jieguo.clear()







    def TimerOutFun(self):
        success,img=self.camera.read()
        if success:
            #self.Image = self.ColorAdjust(img)
            self.Image=img
            self.DispImg()

            #self.Image_num+=1
            #if self.RecordFlag:
               # self.video_writer.write(img)
            #if self.Image_num%10==9:
             #   self.timelb=time.clock()
              #  size=img.shape
                #self.jieguo.clear()
                #self.jieguo.append('获取摄像头成功')
        else:
            self.jieguo.clear()
            self.jieguo.append('获取摄像头失败')

    def DispImg(self):
        img = cv2.cvtColor(self.Image, cv2.COLOR_BGR2RGB)
        qimg = qimage2ndarray.array2qimage(img)

        self.xianshi.setPixmap(QPixmap(qimg))
        self.xianshi.show()

    def Shuangren(self):
        self.jieguo.clear()
        self.jieguo.append('双人猜拳开始！')
        self.NetworkBegin2()
        sys.stdout = Logger("双人模式.txt")
        print('杨振华是我儿子')


    def Sanren(self):
        self.jieguo.clear()
        self.jieguo.append('三人猜拳开始！')
        self.NetworkBegin3()

    def Siren(self):
        self.jieguo.clear()
        self.jieguo.append('四人猜拳开始！')
        self.NetworkBegin4()





    def ExitApp(self):
        #self.Timer.Stop()
        #self.camera.release()
        #self.jieguo.append('正在退出游戏...')
        QCoreApplication.quit()

    def NetworkBegin2(self):
        cap = cv2.VideoCapture(1)
        options = { "model": "cfg/yolov2-tiny.cfg", "load": "bin/yolov2-tiny.weights", "threshold": 0.9, "demo": "camera", "gpuName": "/gpu:0", "gpu": 0.8}
        tfnet = TFNet(options)
        Num = 0
        n1 = []
        n2 = []
        n3 = []
        while(1):

            #get a frame
            ret, frame = cap.read()
            if (cv2.waitKey(10) & 0xFF == ord('q')) :
                break
            # show a frame
            cv2.imshow("capture", frame)
            result = tfnet.return_predict(frame)
            output = []
            if len(result) > 0:

                for i in range(len(result)):
                    pt1_x = result[i]['topleft']['x']
                    pt1_y = result[i]['topleft']['y']
                    pt2_x = result[i]['bottomright']['x']
                    pt2_y = result[i]['bottomright']['y']
                    label = result[i]['label']
                    output.append(label)
                    cv2.rectangle(frame, (pt1_x, pt1_y), (pt2_x, pt2_y), 255, 1, 8, 0, )
                    cv2.imshow("capture", frame)
            print(output)
            Num = Num + 1
            if Num == 4:
                Num = 1
            if Num == 1:
                n1 = output
            if Num == 2:
                n2 = output
            if Num == 3:
                n3 = output
            if (n1 == n2) and (n2 == n3)  and (n1 == ['shitou','shitou'] or
                n1 == ['shitou','jiandao'] or n1 == ['shitou','bu'] or n1 == ['jiandao','shitou'] or
                n1 == ['jiandao','jiandao'] or n2 == ['jiandao','bu'] or n1 == ['bu','shitou'] or
                n1 == ['bu','jiandao'] or n1 == ['bu','bu']):
                player1 = n1[0]
                player2 = n1[1]
                if (player1 == 'jiandao' and player2 == 'bu') or (player1 == 'shitou' and player2 == 'jiandao') or (
                        player1 == 'bu' and player2 == 'shitou'):
                    sys.stdout = Logger("record.txt")
                    print('双人模式:\n玩家1出了' + player1 + '玩家2出了' + player2 + '\n玩家1胜利\n\n')
                    self.jieguo.append('双人模式:\n玩家1出了' + player1 + '玩家2出了' + player2 + '\n玩家1胜利\n\n')
                    break
                elif (player1 == 'jiandao' and player2 == 'jiandao') or (
                    player1 == 'shitou' and player2 == 'shitou') or (
                    player1 == 'bu' and player2 == 'bu'):
                    sys.stdout = Logger("record.txt")
                    print('双人模式:\n玩家1出了' + player1 + '玩家2出了' + player2 + '\n打成平局\n\n')
                    self.jieguo.append('双人模式:\n玩家1出了' + player1 + '玩家2出了' + player2 + '\n打成平局\n\n')
                    break
                else:
                    sys.stdout = Logger("record.txt")
                    print('双人模式:\n玩家1出了' + player1 + '玩家2出了' + player2 + '\n玩家2胜利\n\n')
                    self.jieguo.append('双人模式:\n玩家1出了' + player1 + '玩家2出了' + player2 + '\n玩家2胜利\n\n')
                    break





    def NetworkBegin3(self):
        cap = cv2.VideoCapture(1)
        options = {"model": "cfg/yolov2-voc.cfg", "load": "bin/yolov2-voc_final.weights", "threshold": 0.9,
                   "demo": "camera", "gpuName": "/gpu:0", "gpu": 0.8}
        tfnet = TFNet(options)
        Num = 0
        n1 = []
        n2 = []
        n3 = []
        while (1):

            # get a frame
            ret, frame = cap.read()
            if (cv2.waitKey(10) & 0xFF == ord('q')) :
                break
            # show a frame
            cv2.imshow("capture", frame)
            result = tfnet.return_predict(frame)
            output = []
            if len(result) > 0:

                for i in range(len(result)):
                    pt1_x = result[i]['topleft']['x']
                    pt1_y = result[i]['topleft']['y']
                    pt2_x = result[i]['bottomright']['x']
                    pt2_y = result[i]['bottomright']['y']
                    label = result[i]['label']
                    output.append(label)
                    cv2.rectangle(frame, (pt1_x, pt1_y), (pt2_x, pt2_y), 255, 1, 8, 0, )
                    cv2.imshow("capture", frame)
            print(output)
            Num = Num + 1
            if Num == 4:
                Num = 1
            if Num == 1:
                n1 = output
            if Num == 2:
                n2 = output
            if Num == 3:
                n3 = output
            if (n1 == n2) and (n2 == n3) and (n1 == ['shitou', 'shitou', 'shitou'] or n1 == ['shitou', 'shitou', 'jiandao'] or n1 == ['shitou', 'shitou', 'bu'] or n1 == ['shitou', 'jiandao', 'shitou'] or n1 == ['shitou','jiandao','jiandao'] or n1 == ['shitou', 'jiandao', 'bu'] or n1 == ['shitou', 'bu', 'shitou'] or n1 == ['shitou', 'bu','jiandao'] or n1 == ['shitou', 'bu', 'bu'] or n1 == ['jiandao', 'shitou', 'shitou'] or n1 == ['jiandao', 'shitou','jiandao'] or n1 == ['jiandao', 'shitou', 'bu'] or n1 == ['jiandao', 'jiandao', 'shitou'] or n1 == ['jiandao','jiandao','jiandao']):
                player1 = n1[0]
                player2 = n1[1]
                player3 = n1[2]
                if (player1 == 'jiandao' and player2 == 'bu' and player3 == 'bu') or (player1 == 'shitou' and player2 == 'jiandao' and player3 == 'jiandao') or (player1 == 'bu' and player2 == 'shitou' and player3 == 'shitou'):
                    sys.stdout = Logger("战绩查询.txt")
                    print('三人模式:\n玩家1出了' + player1 + '\n玩家2出了' + player2 + '\n玩家3出了' + player3 + '\n玩家1胜利')
                    self.jieguo.append('三人模式:\n玩家1出了' + player1 + '\n玩家2出了' + player2 + '\n玩家3出了' + player3 + '\n玩家1胜利')
                    break
                elif (player1 == 'bu' and player2 == 'jiandao' and player3 == 'bu') or (player1 == 'jiandao' and player2 == 'shitou' and player3 == 'jiandao') or (player1 == 'shitou' and player2 == 'bu' and player3 == 'shitou'):
                    sys.stdout = Logger("战绩查询.txt")
                    print('三人模式:\n玩家1出了' + player1 + '\n玩家2出了' + player2 + '\n玩家3出了' + player3 + '\n玩家2胜利')
                    self.jieguo.append('三人模式:\n玩家1出了' + player1 + '\n玩家2出了' + player2 + '\n玩家3出了' + player3 + '\n玩家2胜利')
                    break
                elif (player1 == 'bu' and player2 == 'bu' and player3 == 'jiandao') or (player1 == 'jiandao' and player2 == 'jiandao' and player3 == 'shitou') or (player1 == 'shitou' and player2 == 'shitou' and player3 == 'bu'):
                    sys.stdout = Logger("战绩查询.txt")
                    print('三人模式:\n玩家1出了' + player1 + '\n玩家2出了' + player2 + '\n玩家3出了' + player3 + '\n玩家3胜利')
                    self.jieguo.append('三人模式:\n玩家1出了' + player1 + '\n玩家2出了' + player2 + '\n玩家3出了' + player3 + '\n玩家1胜利')
                    break
                elif (player1 == 'bu' and player2 == 'bu' and player3 == 'bu') or (player1 == 'jiandao' and player2 == 'jiandao' and player3 == 'jiandao') or (player1 == 'shitou' and player2 == 'shitou' and player3 == 'shitou'):
                    sys.stdout = Logger("战绩查询.txt")
                    print('三人模式:\n玩家1出了' + player1 + '\n玩家2出了' + player2 + '\n玩家3出了' + player3 + '\n打成平局')
                    self.jieguo.append('三人模式:\n玩家1出了' + player1 + '\n玩家2出了' + player2 + '\n玩家3出了' + player3 + '\n打成平局')
                    break
                else:
                    sys.stdout = Logger("战绩查询.txt")
                    print("无法分出胜负，再猜一次吧~")
                    self.jieguo.append('双方打成平局')
                    break








class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui=CamShow()
    ui.show()
    sys.exit(app.exec_())