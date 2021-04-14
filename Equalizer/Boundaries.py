    def opensignal1(self):
        self.xmin = 0 
        self.xmax = 0
        self.ScrollRate = 1
        self.speed = 1


        # Data shift left
    def update_data(self):
        if self.n1 < self.h1 :
            if self.n1 < 1000 :    
                self.n1 = self.n1 +  10 * self.speed 
                self.data_line1.setData(self.data1[0 : self.n1])
                self.signal_1.plotItem.setXRange(0, self.r1 , padding=0)
                self.xmin = 0 
                self.xmax = self.r1
            
            else :
                self.nn1  =  self.nn1 + 10 * self.speed
                self.n1 = self.n1 + 10 *self.speed
                self.data_line1.setData(self.data1[0 : self.n1])
                self.signal_1.plotItem.setXRange(self.nn1,self.r1 +self.nn1 , padding=0)
                self.xmin = self.nn1
                self.xmax = self.r1 +self.nn1
            self.z1 = 1
            
        else :
            
            self.data_line1.setData(self.data1[0 : self.n1])
            self.signal_1.plotItem.setXRange(0 , self.h1 * self.z1 , padding=0)
            self.xmin = 0 
            self.xmax = self.h1 * self.z1

    def zoomin(self):
        if (self.check_1.isChecked()==True):
            self.signal_1.plotItem.getViewBox().scaleBy(x=0.5,y=1)
            self.r1=self.r1*0.5
            self.z1 = self.z1 * 0.5
            self.ScrollRate *=  0.5

    def zoomout(self):
        if (self.check_1.isChecked()==True):
            self.signal_1.plotItem.getViewBox().scaleBy(x=2,y=1)
            self.r1=self.r1*2
            self.z1 = self.z1 * 2
            self.ScrollRate *= 2

    def scrlleft(self):
        if (self.check_1.isChecked()==True):
            if self.xmin > 0 :
                self.signal_1.plotItem.getViewBox().translateBy(x=-100 * self.ScrollRate ,y=0)
                self.xmin -= 100 * self.ScrollRate
                self.xmax -= 100 * self.ScrollRate

                
    def scrlright(self):
        if (self.check_1.isChecked()==True):
            if self.n1 < 1000 :
                if self.xmax < self.n1 :
                    self.signal_1.plotItem.getViewBox().translateBy(x=100 * self.ScrollRate, y=0)
                    self.xmax += 100 * self.ScrollRate
                    self.xmin += 100 * self.ScrollRate
            else:
                if self.xmax < 1000 +self.nn1 :
                    self.signal_1.plotItem.getViewBox().translateBy(x=100 * self.ScrollRate, y=0)
                    self.xmax += 100 * self.ScrollRate
                    self.xmin += 100 * self.ScrollRate
    def SpeedUp(self):
        if (self.check_1.isChecked()==True):
            self.speed  *=  2

    def SpeedUp(self):
        if (self.check_1.isChecked()==True):
            self.speed  *=  0.5
