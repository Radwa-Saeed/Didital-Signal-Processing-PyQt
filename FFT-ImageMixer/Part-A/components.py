## This is the abstract class that the students should implement
#from modesEnum import Modes
import numpy as np
import cv2

class inputimg():

    def __init__(self, imgPath: str):

        self.imgPath = imgPath
        self.img = cv2.imread(self.imgPath,flags=cv2.IMREAD_GRAYSCALE)
        self.imgShape = self.img.shape
        self.fft = np.fft.fft2(self.img)
        self.real = np.real(self.fft)
        self.imaginary = np.imag(self.fft)
        self.phase = np.angle(self.fft)
        self.amplitude = np.abs(self.fft)

        self.fftshift = np.fft.fftshift(self.fft)    
        self.magnitude = 20*np.log(np.abs(np.fft.fftshift(self.fft)))
        self.realshift = 20*np.log(np.real(np.fft.fftshift(self.fft)))  
        self.phaseshift = np.angle(np.fft.fftshift(self.fft))
        self.imaginaryshift = np.imag(np.fft.fftshift(self.fft))

        self.unimag = np.ones(np.shape(self.amplitude))
        self.uniphase = np.zeros(np.shape(self.phase))

    def mix(self, imgmix: 'inputimg', gain1: float, gain2: float, mode: str, type1: str, type2: str):

        gain1=gain1 / 100.0
        gain2=gain2 / 100.0
        mode= mode
        type1=type1
        type2= type2
        mixInverse = None


        if mode == "magphase":
            M1 = self.amplitude
            M2 = imgmix.amplitude
            P1 = self.phase
            P2 = imgmix.phase
            if (type1 == "Magnitude"):
                magnitudeMix = gain1*M1 + (1-gain1)*M2
                phaseMix = (1-gain2)*P1 + gain2*P2
            elif (type1 == "Phase"):
                phaseMix = gain1*P1 + (1-gain1)*P2
                magnitudeMix = gain2*M2 + (1-gain2)*M1
            combined = np.multiply(magnitudeMix, np.exp(1j * phaseMix))
            mixInverse = np.real(np.fft.ifft2(combined))

        elif mode == "realimg":
            R1 = self.real
            R2 = imgmix.real
            I1 = self.imaginary
            I2 = imgmix.imaginary
            if (type1 == "Real"):
                realMix = gain1*R1 + (1-gain1)*R2
                imaginaryMix = (1-gain2)*I1 + gain2*I2
            elif (type1== "Imaginary"):
                imaginaryMix= gain1*I1 + (1-gain1)*I2 
                realMix = gain2*R2 + (1-gain2)*R1
            combined = realMix + imaginaryMix * 1j
            mixInverse = np.real(np.fft.ifft2(combined))

        elif mode== "unimag": 
            if (type2== "Unimagnitude"):
                M1 = self.amplitude
                M2 = imgmix.unimag
                P1 = self.phase
                P2 = imgmix.phase
                phaseMix = gain1*P1 + (1-gain1)*P2
                magnitudeMix = gain2*M2 + (1-gain2)*M1
            elif(type1=="Unimagnitude"):
                M1 = self.unimag
                M2 = imgmix.amplitude
                P1 = self.phase
                P2 = imgmix.phase
                magnitudeMix = gain1*M1 + (1-gain1)*M2
                phaseMix = (1-gain2)*P1 + gain2*P2

            combined = np.multiply(magnitudeMix, np.exp(1j * phaseMix))
            mixInverse = np.real(np.fft.ifft2(combined))

            

        elif mode== "uniphase":
            if (type2== "Uniphase"):
                M1 = self.amplitude
                M2 = imgmix.unimag
                P1 = self.phase
                P2 = imgmix.uniphase
                magnitudeMix = gain1*M1 + (1-gain1)*M2
                phaseMix = (1-gain2)*P1 + gain2*P2
            elif(type1=="Uniphase"):
                M1 = self.amplitude
                M2 = imgmix.amplitude
                P1 = self.uniphase
                P2 = imgmix.phase
                phaseMix = gain1*P1 + (1-gain1)*P2
                magnitudeMix = gain2*M2 + (1-gain2)*M1
            combined = np.multiply(magnitudeMix, np.exp(1j * phaseMix))
            mixInverse = np.real(np.fft.ifft2(combined))
                

        elif mode== "uniuni":
            # print (mode)
            if (type1=="Unimagnitude"):
                M1 = self.unimag
                M2 = imgmix.amplitude
                P1 = self.phase
                P2 = imgmix.uniphase
                magnitudeMix = gain1*M1 + (1-gain1)*M2
                phaseMix = (1-gain2)*P1 + gain2*P2

            elif(type1=="uniphase"):
                M1 = self.amplitude
                M2 = imgmix.unimag
                P1 = self.uniphase
                P2 = imgmix.phase
                phaseMix = gain1*P1 + (1-gain1)*P2
                magnitudeMix = gain2*M2 + (1-gain2)*M1
                
            combined = np.multiply(magnitudeMix, np.exp(1j * phaseMix))
            mixInverse = np.real(np.fft.ifft2(combined))

 
        return (mixInverse)
