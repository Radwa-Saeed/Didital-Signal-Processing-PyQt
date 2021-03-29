      #Zooming
        # self.g1 =0
        # self.j1 =0
        # self.k1 =0
        # self.h1 =0
        # self.b1=False
        #----- Buttons actions -----#
        # self.buttonname.clicked.connect(lambda:self.functionname())
 

    def pause(self):
        if self.timer.isActive():
            self.timer.stop()
            self.play2.setIcon(icon5)
            
        else:
            self.timer.start()
            self.play2.setIcon(icon1)
    #---- Hide & Show -----#
    def show1(self):
        if (self.hide1.isChecked()):
            self.Viewsig_1.hide()
            self.viewspect_1.hide()
            self.play1.hide()
            self.pause1.hide()
            self.clear1.hide()
            self.zoomin1.hide()
            self.zoomout1.hide()
            
        else :
            self.Viewsig_1.show()
            self.viewspect_1.show()
            self.play1.show()
            self.pause1.show()
            self.clear1.show()
            self.zoomin1.show()
            self.zoomout1.show()
                

        #----reading function ---#
   
    #------- Clear ------#
    def delete1(self):
        self.Viewsig_1.clear()
        self.viewspect_1.clear()
        self.timer= None
        self.data_line1.setData(self.data1[0 : 100])
    #----- save as pdf ---#


    def savepdf(self):
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export PDF", None, "PDF files (.pdf);;All Files()")
        if fn:
            if QtCore.QFileInfo(fn).suffix() == "": fn += ".pdf"
            print_widget(MainWindow, fn)

    def readsignal1(self):
        self.fname1=QtGui.QFileDialog.getOpenFileName(self,'open only txt file',os.getenv('home'),"text(*.txt)")
        path=self.fname1[0]
        self.data1=np.genfromtxt(path)

    # def readsignal1(self):
    #     self.fname1=QtGui.QFileDialog.getOpenFileName(self,'open only txt file',os.getenv('home'),"text(*.txt)")
    #     path=self.fname1[0]
    #     self.data1=np.genfromtxt(path,delimiter=',')
    #     self.x1= self.data1[: , 0]
    #     self.y1 =self.data1[: , 1] 
    #     self.x1= list(self.x1[:])
    #     self.y1= list(self.y1[:])
def opensignal1(self):
        self.readsignal1()
        self.h =len(self.data1)
        self.n = 0
        self.data_line1 = self.Viewsig_1.plot(self.data1, name="mode2")
        self.ptr1 = 0
        self.pen = pg.mkPen(color=(255, 0, 0))
        # Set timer
        self.timer = pg.QtCore.QTimer()
        # Timer signal binding update_data function
        self.timer.timeout.connect(self.update_data)
        # The timer interval is 50ms, which can be understood as refreshing data once in 50ms
        self.timer.start(50)
        # self.Viewsig_1.plotItem.setXRange(min(self.timer, default=0)+self.x)
    # Data shift left
    def update_data(self):
        if self.n < self.h :
            self.n += 10    
            self.data_line1.setData(self.data1[0 : 100+self.n])
            self.Viewsig_1.plotItem.setXRange(0+self.n, 300+self.n , padding=0)
        else :
            self.data_line1.setData(self.data1[0 : 100+self.n])
            self.Viewsig_1.plotItem.setXRange(0 , self.h , padding=0)
############# FUNCTION KAREEM ##############
    # def opensignal1(self):
    #     self.readsignal1()
    #     self.h =len(self.data1)
    #     self.n = 0
    #     self.data_line1 = self.Viewsig_1.plot(self.data1, name="mode2")
    #     self.ptr1 = 0
    #     self.pen = pg.mkPen(color=(255, 0, 0))
    #     # Set timer
    #     self.timer = pg.QtCore.QTimer()
    #     # Timer signal binding update_data function
    #     self.timer.timeout.connect(self.update_data)
    #     # The timer interval is 50ms, which can be understood as refreshing data once in 50ms
    #     self.timer.start(50)
    #     # self.Viewsig_1.plotItem.setXRange(min(self.timer, default=0)+self.x)
    # # Data shift left
    # def update_data(self):
    #     if self.n < self.h :
    #         self.n += 10    
    #         self.data_line1.setData(self.data1[0 : 100+self.n])
    #         self.Viewsig_1.plotItem.setXRange(0+self.n, 300+self.n , padding=0)
    #     else :
    #         self.data_line1.setData(self.data1[0 : 100+self.n])
    #         self.Viewsig_1.plotItem.setXRange(self.h-1000 , self.h , padding=0)
##################################################################

    #----Buttons functions -----#
    # def opensignal1(self):
    #     self.readsignal1()
    #     self.pen = pg.mkPen(color=(255, 0, 0))
    #     self.data_line1 =  self.Viewsig_1.plot( self.x1,self.y1, pen=self.pen)
    #     self.Viewsig_1.plotItem.setLimits(xMin =0, xMax=12 , yMin =-0.6, yMax=0.6)
        
    def opensignal1(self):
        self.readsignal1()
        self.data_line1 = self.Viewsig_1.plot(self.data1, name="mode2")
        self.ptr1 = 0
        self.n = 0

        # Set timer
        self.timer = pg.QtCore.QTimer()
        
        # Timer signal binding update_data function
        self.timer.timeout.connect(self.update_data)
        # The timer interval is 50ms, which can be understood as refreshing data once in 50ms
        self.timer.start(50)
    #Data shift left
    def update_data(self):
        self.n += 10
        self.data_line1.setData(self.data1[0 : 100+self.n])
        self.data_line1.setPos(self.ptr1,0)
    

 
    def scrollf(self):
        self.Viewsig_1.plotItem.getViewBox().translateBy(x=-100,y=0)

    def scrollb(self):
        self.Viewsig_1.plotItem.getViewBox().translateBy(x=100,y=0)     

        # pos = self.Viewsig_1.xMax()
        # self.Viewsig_1.setXRange(pos-100,pos-50)
    
    # #     self.ptr1 = 0
    #     self.n = 0
    #     self.n += 10
    #     self.data_line1.setData(self.data1[0 : 100+self.n])
    #     self.data_line1.setPos(50,50)



    def zoominfn (self):
        self.Viewsig_1.plotItem.getViewBox().scaleBy(x=0.5,y=1)

    #     self.j1=0
    #     self.b1=True
    #     self.g1 = self.g1 + 1
    #    # self.k1=12-self.g1*0.5
    #     if (self.h1 == 0):

    #         self.k1 = 4000-self.g1 *50
    #     else:
    #         self.k1 = self.h1 - self.g1 *50
    #     # print(len(self.x1))
    #   #  self.k1=max(0,self.k1)
    #     print(f"k1 {self.k1}") 
    #     print(f"h1 {self.h1}")   
    #    # print(self.h1)
    #     if (self.k1>=0):
    #     #    self.h1 = self.k1 + self.j1 * 0.5
    #         self.Viewsig_1.setXRange(0,self.k1)
    #     else:
    #         self.k1=0
    #   #  self.Viewsig_1.setXRange(0,self.k1)
    #     print(f"k1 {self.k1}") 
    #     print(f"h1 {self.h1}")  
    #     # self.Viewsig_1.plotItem.setLimits(xMin =0)
    #   #  self.Viewsig_1.setYRange(0,self.h1)
    #   #  self.Viewsig_1[0].plotItem.getViewBox().scaleBy()

    def zoomoutfn (self):
        self.Viewsig_1.plotItem.getViewBox().scaleBy(x=2,y=1)

    #     self.g1=0
    #     self.j1 = self.j1+1
    #     print(self.b1)
    #  #   self.h1=12+self.j1*0.5
    #     if (not self.b1) :
    #         self.h1 = 4000+self.j1 *50
    #     else:
    #         self.h1 = self.k1 + self.j1 * 50

    #   #  self.h1=max(0,self.h1)  
    #     print(f"h1 {self.h1}")
    #     print(f"k1 {self.k1}")

    #   #  self.Viewsig_1.setXRange(0,self.h1)
 
    #     if (self.h1>=0):
    #     #    self.k1 = self.h1 - self.g1 *0.5  
    #         self.Viewsig_1.setXRange(0,self.h1)
    #     else:
    #         pass
    #     #    self.h1=20
            
