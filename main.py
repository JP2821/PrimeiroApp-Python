import sys
import os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_splash_screen import Ui_SplashScreen
from ui_main import Ui_MainWindow
from ui_functions import *

#globais
counter = 0
jumper = 0 
#Essa variavel vai nos ajudar a determinar se a janela está maximizada ou não
WINDOW_SIZE=0
#Para as barras de progresso
valor = 70
valor_agua = 60

## ==> Nossa Aplicação
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ## => remove a barra de titulo e as bordas da janela
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #remove a barra de titulo
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) #faz o background ficar transparente

        ## Aplicando efeitos de sombra
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,120))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #Eventos dos Botões da tela
        #Botão de minimizar
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())

        #maximizar a janela
        self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())

        #fechar a janela
        self.ui.closeButton.clicked.connect(lambda: self.close())

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nivel_dos_gases))

        # Configuração dos botões de aumentar e diminuir
        
        # Configuração do botão de hidrogênio (+)
        self.ui.pushButton.clicked.connect(lambda: self.aumentar_hidrogenio())

        # Configuração do botão de hidrogênio (-)
        self.ui.pushButton_2.clicked.connect(lambda: self.diminuir_hidrogenio())

        # Configuração do botão da água (+)
        self.ui.pushButton_3.clicked.connect(lambda: self.aumentar_agua())

        # Configuração do botão da água (-)
        self.ui.pushButton_4.clicked.connect(lambda: self.diminuir_agua())


        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.configuracoes))

    def aumentar_hidrogenio(self):
        global valor
        valor = valor + 1
        if valor >= 100:
            valor = 100
        self.ui.progressBar.setValue(valor)

    def diminuir_hidrogenio(self):
        global valor
        valor = valor - 1
        if valor <= 0:
            valor = 0
        self.ui.progressBar.setValue(valor)

    def aumentar_agua(self):
        global valor_agua
        valor_agua = valor_agua + 1
        if valor_agua >= 100:
            valor_agua = 100
        self.ui.progressBar_2.setValue(valor_agua)

    def diminuir_agua(self):
        global valor_agua
        valor_agua = valor_agua - 1
        if valor_agua <= 0:
            valor_agua = 0
        self.ui.progressBar_2.setValue(valor_agua)    

    def restore_or_maximize_window(self):
        global WINDOW_SIZE
        win_status = WINDOW_SIZE

        if win_status == 0:
            # se a tela não estiver maximizada
            WINDOW_SIZE = 1
            self.showMaximized()
    
        else:
            #se a janela já estive no seu maior tamanho
            WINDOW_SIZE = 0
            self.showNormal()


## ==> Janela de carregamento
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ##Colocado a inicialização da barra apartir do zero
        self.progressBarValue(0)

        ## => remove a barra de titulo e as bordas da janela
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #remove a barra de titulo
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) #faz o background ficar transparente

        ## Aplicando efeitos de sombra
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## ==>QTimer == Start
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        #Timer em milisegundos
        self.timer.start(15)
        

        #######################################################
        #testando as funções da barra de progresso
        # self.progressBarValue(50) , deu certo ;) <3
        #######################################################

        #para exebir a tela 
        self.show()

    #definindo o loading
    def progress(self):
        global counter
        global jumper
        value = counter

        #Um pouco de HTML para a o texto de porcentagem
        htmlText = """ <p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:48pt; vertical-align:super;">%</span></p> """

        #Trocando os valores no HTML
        newhtml = htmlText.replace("{VALUE}",str(jumper))
        if (value> jumper):
            #Aplicando a nova porcentegam ao texto
            self.ui.labelPercentage.setText(newhtml)
            jumper += 10

        #colocando os valores da barra de progresso
        #definindo o valor maximo para evitar problemas futuros caso seja maior que 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        if counter > 100:
            self.timer.stop()
            #Exibir a Janela Principal
            self.main = MainWindow()
            self.main.show()

            #fechando Janela
            self.close()

        counter += 0.5

    #definindo a barra de progresso
    def progressBarValue(self, value):
        #estilo da barra de progresso
        styleSheet = """
        QFrame{
	        border-radius: 150px;
	        background-color:qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """
        #inserindo os valores da nossa barra de progresso, converter o FLOAT e inverter o VALUES
        #parar 1.000 para 0.000
        progress = (100 - value) / 100.0

        #inserindo os novos valores
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        #colocando os valores no styleSheet
        new_styleSheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        #aplicando o styleSheet aos novos valores
        self.ui.circularProgress.setStyleSheet(new_styleSheet)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
