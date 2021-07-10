import Fourier
import time
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
Error=[]
MeanSquareError=[]
TransformedDataDFT=[]
TransformedDataFFT=[]
Sampels=[]
TimeBeforeFFT=[]
TimeAfterFFT=[]
TimeDifferenceFFT=[]
TimeBeforeDFT=[]
TimeAfterDFT=[]
TimeDifferenceDFT=[]
NumberOfData=[]
for i in range (5):
    Sampels.append([random.randint(1,10000) for _ in range(2**(4+i*3))])   
    NumberOfData.append(len(Sampels[i]))
for i in range(5):
    TimeBeforeFFT.append(time.time())
    TransformedDataFFT.append(Fourier.FFT(Sampels[i]))
    TimeAfterFFT.append(time.time())
    TimeDifferenceFFT.append(TimeAfterFFT[i]-TimeBeforeFFT[i])
    TimeBeforeDFT.append(time.time())
    TransformedDataDFT.append(Fourier.DFT(Sampels[i]))
    TimeAfterDFT.append(time.time())
    TimeDifferenceDFT.append(TimeAfterDFT[i]-TimeBeforeDFT[i])
    MeanSquareError.append(np.square(np.subtract(TransformedDataDFT[i],TransformedDataFFT[i])).mean())
print(MeanSquareError)
for i in range(len(MeanSquareError)):
    Error.append(abs(MeanSquareError[i]))

plt.plot(NumberOfData,Error)
plt.ylim(-2,2)
plt.show()
TimeDifferenceDFT=np.array(TimeDifferenceDFT)
TimeDifferenceFFT=np.array(TimeDifferenceFFT)
NumberOfData=np.array(NumberOfData)
print(f'Sampels:\n{len(Sampels)}')
print(f'TimeDifferenceFFT:\n{TimeDifferenceFFT}')
print(f'TimeDifferenceDFT:\n{TimeDifferenceDFT}')

# For Fitting a curve
cubic_interploation_model = interp1d(NumberOfData, TimeDifferenceDFT, kind = "cubic")
N=np.linspace(NumberOfData.min(), NumberOfData.max(), 500)
NSquare=cubic_interploation_model(N)
cubic_interploation_model = interp1d(NumberOfData, TimeDifferenceFFT, kind = "cubic")
NlogN=cubic_interploation_model(N)
#Plotting
plt.plot(N,NSquare,label='NSquare')
plt.plot(N,NlogN,label='NlogN')
plt.legend()
plt.ylabel("Time(s)")
plt.xlabel("NumberOfSampels")
plt.show()

# print(Error)
# print(TransformedDataDFT)
# print(TransformedDataFFT)
# print(len(Error[4]))
# print(len(TransformedDataDFT[4]))
# print(len(TransformedDataFFT[4]))
# print(ErrorMean)
