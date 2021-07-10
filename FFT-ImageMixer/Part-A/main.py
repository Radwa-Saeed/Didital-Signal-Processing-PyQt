# Importing Packages
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import numpy as np
from mixer import Ui_MainWindow
import cv2
#from modesEnum import Modes
from components import image_components

# importing module
import logging

# Create and configure logger
logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    format='%(lineno)s - %(levelname)s - %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()


# choose item from combo
# change combo content

class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        """
        Main loop of the UI
        :param mainWindow: QMainWindow Object
        """
        #super(ApplicationWindow, self).setupUi(starterWindow)
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load Buttons
        #self.loadButtons = [self.actionImage1, self.actionImage2]

        # Images Lists
        self.inputImages = [self.ui.img1,self.ui.img2]
        self.updatedImages = [self.ui.img1_component,self.ui.img2_component]
        self.outputImages = [self.ui.output1,self.ui.output2]
        self.imagesModels = [..., ...]
        self.imageWidgets = [self.ui.img1,self.ui.img2, self.ui.img1_component,self.ui.img2_component,self.ui.output1,self.ui.output2]

        self.heights = [..., ...]
        self.weights = [..., ...]

        # Combo Lists
        self.imagecombos = [self.ui.img1_combo,self.ui.img2_combo]
        #self.imageCombos = [self.ui.img1_combo,self.ui.img2_combo]
        #self.componentCombos = [self.combo_select_mode1, self.combo_select_mode2]
        
        self.counter=-1
        self.data=[]
        self.ui.pause.clicked.connect(lambda:self.loadFile())
        self.ui.actionOpen.triggered.connect(lambda:self.Components())
        self.ui.img1_combo.currentTextChanged.connect(lambda:self.Components(0))
        self.ui.img2_combo.currentTextChanged.connect(lambda:self.Components(1))
        self.setupImagesView()
        
    def loadFile(self, imgID):
        """
        Load the File from User
        :param imgID: 0 or 1
        :return:
        """
        # Open File & Check if it was loaded correctly
        logger.info("Browsing the files...")
        repo_path = "D:\Study\Courses\Python\DSP Tasks - 3rd Year\sbe309-2020-task3-Abdullah-Alrefaey\images"
        self.filename, self.format = QtWidgets.QFileDialog.getOpenFileName(None, "Load Image", repo_path,
                                                                           "*.jpg;;" "*.jpeg;;" "*.png;;")
        imgName = self.filename.split('/')[-1]
        if self.filename == "":
            pass
        else:
            image = cv2.imread(self.filename, flags=cv2.IMREAD_GRAYSCALE).T
            self.heights[imgID], self.weights[imgID] = image.shape
            self.imagesModels[imgID] = image_components(self.filename)

            if ty# Importing Packages
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import numpy as np
from mixer import Ui_MainWindow
import cv2
#from modesEnum import Modes
from components import image_components

# importing module
import logging

# Create and configure logger
logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    format='%(lineno)s - %(levelname)s - %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()


# choose item from combo
# change combo content

class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        """
        Main loop of the UI
        :param mainWindow: QMainWindow Object
        """
        #super(ApplicationWindow, self).setupUi(starterWindow)
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load Buttons
        #self.loadButtons = [self.actionImage1, self.actionImage2]

        # Images Lists
        self.inputImages = [self.ui.img1,self.ui.img2]
        self.updatedImages = [self.ui.img1_component,self.ui.img2_component]
        self.outputImages = [self.ui.output1,self.ui.output2]
        self.imagesModels = [..., ...]
        self.imageWidgets = [self.ui.img1,self.ui.img2, self.ui.img1_component,self.ui.img2_component,self.ui.output1,self.ui.output2]

        self.heights = [..., ...]
        self.weights = [..., ...]

        # Combo Lists
        self.imagecombos = [self.ui.img1_combo,self.ui.img2_combo]
        #self.imageCombos = [self.ui.img1_combo,self.ui.img2_combo]
        #self.componentCombos = [self.combo_select_mode1, self.combo_select_mode2]
        
        self.counter=-1
        self.data=[]
        self.ui.pause.clicked.connect(lambda:self.loadFile())
        self.ui.actionOpen.triggered.connect(lambda:self.Components())
        self.ui.img1_combo.currentTextChanged.connect(lambda:self.Components(0))
        self.ui.img2_combo.currentTextChanged.connect(lambda:self.Components(1))
        self.setupImagesView()
        
    def loadFile(self, imgID):
        """
        Load the File from User
        :param imgID: 0 or 1
        :return:
        """
        # Open File & Check if it was loaded correctly
        logger.info("Browsing the files...")
        repo_path = "D:\Study\Courses\Python\DSP Tasks - 3rd Year\sbe309-2020-task3-Abdullah-Alrefaey\images"
        self.filename, self.format = QtWidgets.QFileDialog.getOpenFileName(None, "Load Image", repo_path,
                                                                           "*.jpg;;" "*.jpeg;;" "*.png;;")
        imgName = self.filename.split('/')[-1]
        if self.filename == "":
            pass
        else:
            image = cv2.imread(self.filename, flags=cv2.IMREAD_GRAYSCALE).T
            self.heights[imgID], self.weights[imgID] = image.shape
            self.imagesModels[imgID] = image_components(self.filename)

            if type(self.imagesModels[~imgID]) == type(...):
                # Create and Display Original Image
                self.displayImage(self.imagesModels[imgID].imgByte, self.inputImages[imgID])
                self.updateCombos[imgID].setEnabled(True)
                logger.info(f"Added Image{imgID + 1}: {imgName} successfully")
            else:
                if self.heights[1] != self.heights[0] or self.weights[1] != self.weights[0]:
                    self.showMessage("Warning!!", "Image sizes must be the same, please upload another image",
                                     QMessageBox.Ok, QMessageBox.Warning)
                    logger.warning("Warning!!. Image sizes must be the same, please upload another image")
                else:
                    self.displayImage(self.imagesModels[imgID].imgByte, self.inputImages[imgID])
                    self.updateCombos[imgID].setEnabled(True)
                    logger.info(f"Added Image{imgID + 1}: {imgName} successfully")

            if self.updateCombos[0].isEnabled() and self.updateCombos[1].isEnabled():
                self.enableOutputCombos()
                logger.info("ComboBoxes have been enabled successfully")



    def displayImage(self, data, widget):
        """
        Display the given data
        :param data: 2d numpy array
        :param widget: ImageView object
        :return:
        """
        widget.setImage(data)
        widget.view.setRange(xRange=[0, self.imagesModels[0].imgShape[0]], yRange=[0, self.imagesModels[0].imgShape[1]],
                             padding=0)
        widget.ui.roiPlot.hide()

    def setupImagesView(self):
        """
        Adjust the shape and scales of the widgets
        Remove unnecessary options
        :return:
        """
        for widget in self.imageWidgets:
            widget.ui.histogram.hide()
            widget.ui.roiBtn.hide()
            widget.ui.menuBtn.hide()
            widget.ui.roiPlot.hide()
            widget.getView().setAspectLocked(False)
            widget.view.setAspectLocked(False)

def main():
    """
    the application startup functions
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
