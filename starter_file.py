from PyQt5 import QtWidgets,QtCore
from equalizer import Ui_MainWindow
import sys
from  PyQt5.QtWidgets  import QFileDialog
import numpy as np
import sounddevice as sd
import wave
from scipy import fftpack
from scipy.io.wavfile import write
import os
import winsound
from popwindow import  Ui_ui_mainWindow


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.data=[]
        self.y=[]
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.values = [1,1,1,1,1,1,1,1,1,1]
        self.sliders=[self.ui.verticalSlider,self.ui.verticalSlider_2,
                 self.ui.verticalSlider_3,self.ui.verticalSlider_4,self.ui.verticalSlider_5,
                 self.ui.verticalSlider_6,self.ui.verticalSlider_7,self.ui.verticalSlider_8,
                 self.ui.verticalSlider_9,self.ui.verticalSlider_10]
        self.funcs=[lambda:self.changeValue(0),lambda:self.changeValue(1),
                    lambda:self.changeValue(2),lambda:self.changeValue(3),lambda:self.changeValue(4),
                    lambda:self.changeValue(5),lambda:self.changeValue(6),lambda:self.changeValue(7),
                    lambda:self.changeValue(8),lambda:self.changeValue(9)]
        
        
        for i in range(10):
            self.sliders[i].valueChanged['int'].connect(self.funcs[i])
            
            
    def subbands(self):
        global bands1
        global ham
        global han
        global fft_out
        self.file = QFileDialog.getOpenFileName(self, 'Open file','',' *.wav')[0]
        winsound.PlaySound(self.file, winsound.SND_ASYNC)
        self.data=wave.open(self.file,'r')
        sz = 44100 # Read and process 1 second at a time.
        da = np.fromstring(self.data.readframes(sz), dtype=np.int16)
        left= da[0::2]
        Fourier= fftpack.rfft(left)
        fft_out = abs(Fourier)
        fft_out=np.flip(fft_out)
        #freqs = np.arange(len(left))
        freqs=fftpack.rfftfreq(len(left))*sz
        bands1=[fft_out[0:4410],fft_out[4410:8820],fft_out[8820:13230],
                fft_out[13230:17640],fft_out[17640:22050],fft_out[22050:26460],
                fft_out[26460:30870],fft_out[30870:35280],fft_out[35280:39690],
                fft_out[39690:44100]]
        self.new = bands1
    
        bands2=[freqs[0:4410],freqs[4410:8820],freqs[8820:13230],
                freqs[13230:17640],freqs[17640:22050],freqs[22050:26460],
                freqs[26460:30870],freqs[30870:35280],freqs[35280:39690],freqs[39690:44100]]

        Nsamps = len(bands1[0])
        print(Nsamps)
        ham= np.hamming(Nsamps*2)
        han= np.hanning(Nsamps*2)
        
        self .ui. MplWid1.canvas.axes.clear ()
        for m ,k in zip(bands1,bands2):
            self.ui.MplWid1.canvas.axes.plot(k,m)
            self.ui.MplWid1.canvas.axes.legend ((  'Fourier' ,  ),loc = 'upper right' ) 
            self.ui.MplWid1.canvas.draw()
            
    def changeValue(self,i):
        
        if self.ui.comboBox.currentText()=="hamming":
            self.values[i]=self.sliders[i].value()*ham[int(0.25*len(ham)):int(0.75*len(ham))]
        
        if self.ui.comboBox.currentText()=="rectangular":
            self.values[i]=self.sliders[i].value()
            
        if self.ui.comboBox.currentText()=="hanning":
            self.values[i]=self.sliders[i].value()*han[int(0.25*len(han)):int(0.75*len(han))]
        
        new=self.values[i]*bands1[i]
        self.new[i]=bands1[i]*0+new
        self.y=np.concatenate(self.new)
        self.ui.MplWid1.canvas.axes.clear ()
        self.ui.MplWid1.canvas.axes.plot(self.y)
        self.ui.MplWid1.canvas.axes.legend ((  'Fourier' ,  ),loc = 'upper right' ) 
        self.ui.MplWid1.canvas.draw()
        
    def reset(self):
        for i in range(10):
            self.sliders[i].setValue(1)
            
        self.ui.MplWid1.canvas.axes.clear ()
        self.ui.MplWid1.canvas.axes.plot(fft_out)
        self.ui.MplWid1.canvas.axes.legend ((  'Fourier' ,  ),loc = 'upper right' ) 
        self.ui.MplWid1.canvas.draw()
        self.ui.comboBox.setCurrentText("window")
        
    def play(self):
        
        data=fftpack.irfft(self.y)
        print(data)
        sd.play(data / data.max(), 44100)
        
    def stop(self):
        winsound.PlaySound(None, winsound.SND_PURGE)
        sd.stop()
   
    def save(self):
        out=np.array(fftpack.irfft(self.y),dtype=np.int16)
        write('out.wav',44100,out)
        os.startfile("out.wav")
        
    def difference(self):
        self.window= QtWidgets.QMainWindow()
        self.u= Ui_ui_mainWindow()
        self.u.setupUi(self.window)
        self.window.show()
        self.u.MplWid2.canvas.axes.clear ()
        self.u.MplWid2.canvas.axes.plot(self.y,color='black')
        self.u.MplWid2.canvas.axes.legend ((  'freqs_new' ,  ),loc = 'upper right')
        self.u.MplWid2.canvas.axes1.clear()
        self.u.MplWid2.canvas.axes1.plot(fft_out)
        self.u.MplWid2.canvas.axes1.legend ((  'freqs_old' ,  ),loc = 'upper right')
        self.u.MplWid2.canvas.draw()
        
    
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()