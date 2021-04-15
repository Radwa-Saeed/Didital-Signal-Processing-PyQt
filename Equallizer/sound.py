# import os

# import sys

# from PyQt5 import QtCore, QtMultimedia

# # CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

# def main():

#     filename = os.path.join(CURRENT_DIR, "test (1).wav")

#     app = QtCore.QCoreApplication(sys.argv)

#     QtMultimedia.QSound.play(filename)

#     # end in 5 seconds:

#     QtCore.QTimer.singleShot(5 * 1000, app.quit)

#     sys.exit(app.exec_())

# if __name__ == "__main__":

#     main()


from PyQt5.QtCore import QCoreApplication
from PyQt5.QtMultimedia import QSound
import sys

if __name__ == '__main__':
    app = QCoreApplication(sys.argv)
    sound = QSound("1.wav")
    sound.play()
    sys.exit(app.exec_())