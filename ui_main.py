# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainRrXMMW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import closebutton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/pngwing.com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_top)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(100, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.frame)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/minimize-icon-23794.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon1)
        self.minimizeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.minimizeButton)

        self.restoreButton = QPushButton(self.frame)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/PinClipart.com_window-clip-art-black_824912.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon2)
        self.restoreButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.restoreButton)

        self.closeButton = QPushButton(self.frame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/close-button-icon-png-0.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.closeButton)


        self.horizontalLayout_3.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_top_menus)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(100, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	padding-left: 30px;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/1976053_home_home page_homepage_homepages_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_1.setIcon(icon4)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(100, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	padding-left: 50px;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/kisspng-natural-gas-symbol-icon-flames-pic-5a7609a5a49717.3794125015176851576742.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_2.setIcon(icon5)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.btn_page_2)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.btn_page_3 = QPushButton(self.frame_left_menu)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	padding-left: 63px;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/pngegg (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_3.setIcon(icon6)

        self.verticalLayout_3.addWidget(self.btn_page_3)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_7 = QVBoxLayout(self.home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.login_form_frame = QFrame(self.home)
        self.login_form_frame.setObjectName(u"login_form_frame")
        self.login_form_frame.setFrameShape(QFrame.StyledPanel)
        self.login_form_frame.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.login_form_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 320, 120, 80))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 50, 75, 23))
        font = QFont()
        font.setFamily(u"Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.progressBar = QProgressBar(self.login_form_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 340, 221, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	border : 2px solid grey;\n"
"	border-radius: 4px;\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: rgb(85, 255, 127);\n"
"	width: 20px;\n"
"} ")
        self.progressBar.setValue(70)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar_2 = QProgressBar(self.login_form_frame)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(320, 340, 261, 23))
        self.progressBar_2.setStyleSheet(u"QProgressBar{\n"
"	border : 2px solid grey;\n"
"	border-radius: 4px;\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: rgb(0, 85, 255);\n"
"	width: 20px;\n"
"} ")
        self.progressBar_2.setValue(60)
        self.label_8 = QLabel(self.login_form_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 300, 251, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Black")
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_8.setFont(font1)
        self.label_13 = QLabel(self.login_form_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(310, 300, 251, 31))
        self.label_13.setFont(font)
        self.label_16 = QLabel(self.login_form_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(370, 170, 181, 20))
        self.label_16.setFont(font)
        self.pushButton_2 = QPushButton(self.login_form_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 370, 75, 23))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.pushButton_3 = QPushButton(self.login_form_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(320, 370, 75, 23))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_4 = QPushButton(self.login_form_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(510, 370, 75, 23))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.frame_3 = QFrame(self.login_form_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(370, 0, 171, 161))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-radius:10px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(0, 10, 171, 141))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: none;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/Screenshot_20210818-084815_WhatsApp.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setIconSize(QSize(150, 150))
        self.pushButton_7 = QPushButton(self.login_form_frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(500, 300, 31, 31))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: none;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/toppng.com-free-download-gota-de-agua-png-clipart-drop-clip-art-imagen-de-gotas-de-agua-441x754.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(20, 20))
        self.calendarWidget = QCalendarWidget(self.login_form_frame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 10, 331, 201))
        self.frame_circle_4 = QFrame(self.login_form_frame)
        self.frame_circle_4.setObjectName(u"frame_circle_4")
        self.frame_circle_4.setGeometry(QRect(620, 80, 250, 250))
        self.frame_circle_4.setMinimumSize(QSize(250, 250))
        self.frame_circle_4.setMaximumSize(QSize(250, 250))
        self.frame_circle_4.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_circle_4.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_circle_4)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 50, 10, 50)
        self.label_17 = QLabel(self.frame_circle_4)
        self.label_17.setObjectName(u"label_17")
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(11)
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_circle_4)
        self.label_18.setObjectName(u"label_18")
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(8)
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"border: none;\n"
" color: rgb(128, 102, 168);")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_circle_4)
        self.label_19.setObjectName(u"label_19")
        font4 = QFont()
        font4.setFamily(u"Roboto Thin")
        font4.setPointSize(57)
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_circle_4)
        self.label_20.setObjectName(u"label_20")
        font5 = QFont()
        font5.setFamily(u"Roboto")
        font5.setPointSize(10)
        self.label_20.setFont(font5)
        self.label_20.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_20)

        self.frame_3.raise_()
        self.frame_4.raise_()
        self.progressBar.raise_()
        self.progressBar_2.raise_()
        self.label_8.raise_()
        self.label_13.raise_()
        self.label_16.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_7.raise_()
        self.calendarWidget.raise_()
        self.frame_circle_4.raise_()

        self.verticalLayout_7.addWidget(self.login_form_frame)

        self.stackedWidget.addWidget(self.home)
        self.nivel_dos_gases = QWidget()
        self.nivel_dos_gases.setObjectName(u"nivel_dos_gases")
        self.verticalLayout_6 = QVBoxLayout(self.nivel_dos_gases)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.nivel_dos_gases)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.drop_shadow_frame = QFrame(self.frame_2)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setGeometry(QRect(-10, -61, 911, 621))
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        font6 = QFont()
        font6.setFamily(u"Roboto Condensed Light")
        font6.setPointSize(14)
        self.frame_title.setFont(font6)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_title)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font7 = QFont()
        font7.setFamily(u"Roboto")
        font7.setPointSize(14)
        self.label_title.setFont(font7)
        self.label_title.setStyleSheet(u"color: rgb(60, 231, 195);")

        self.verticalLayout_9.addWidget(self.label_title)


        self.horizontalLayout_5.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_maximize)

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_close)


        self.horizontalLayout_5.addWidget(self.frame_btns)


        self.verticalLayout_4.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.content_bar)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.stackedWidget_2 = QStackedWidget(self.content_bar)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"background-color: none;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_11 = QVBoxLayout(self.page_home)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.page_home)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_content_home)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_infos = QFrame(self.frame_content_home)
        self.frame_infos.setObjectName(u"frame_infos")
        self.frame_infos.setFrameShape(QFrame.StyledPanel)
        self.frame_infos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_infos)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_circle_1 = QFrame(self.frame_infos)
        self.frame_circle_1.setObjectName(u"frame_circle_1")
        self.frame_circle_1.setMinimumSize(QSize(250, 250))
        self.frame_circle_1.setMaximumSize(QSize(250, 250))
        self.frame_circle_1.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_circle_1.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_circle_1)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 50, 10, 50)
        self.label_2 = QLabel(self.frame_circle_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_circle_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"border: none;\n"
" color: rgb(128, 102, 168);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_circle_1)
        self.label_4.setObjectName(u"label_4")
        font8 = QFont()
        font8.setFamily(u"Roboto Thin")
        font8.setPointSize(60)
        self.label_4.setFont(font8)
        self.label_4.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_circle_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_5)


        self.horizontalLayout_7.addWidget(self.frame_circle_1)

        self.frame_circle_2 = QFrame(self.frame_infos)
        self.frame_circle_2.setObjectName(u"frame_circle_2")
        self.frame_circle_2.setMinimumSize(QSize(250, 250))
        self.frame_circle_2.setMaximumSize(QSize(250, 250))
        self.frame_circle_2.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_circle_2.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_circle_2)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, 50, 10, 50)
        self.label_6 = QLabel(self.frame_circle_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_circle_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font8)
        self.label_7.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_7)

        self.label_9 = QLabel(self.frame_circle_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)


        self.horizontalLayout_7.addWidget(self.frame_circle_2)

        self.frame_circle_3 = QFrame(self.frame_infos)
        self.frame_circle_3.setObjectName(u"frame_circle_3")
        self.frame_circle_3.setMinimumSize(QSize(250, 250))
        self.frame_circle_3.setMaximumSize(QSize(250, 250))
        self.frame_circle_3.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60, 231, 195);\n"
"	border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_circle_3.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_circle_3)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 50, 10, 50)
        self.label_10 = QLabel(self.frame_circle_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_circle_3)
        self.label_11.setObjectName(u"label_11")
        font9 = QFont()
        font9.setFamily(u"Roboto Thin")
        font9.setPointSize(37)
        self.label_11.setFont(font9)
        self.label_11.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_circle_3)
        self.label_12.setObjectName(u"label_12")
        font10 = QFont()
        font10.setFamily(u"Roboto")
        font10.setPointSize(13)
        self.label_12.setFont(font10)
        self.label_12.setStyleSheet(u"border: none;\n"
" color: rgb(128, 102, 168);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_12)


        self.horizontalLayout_7.addWidget(self.frame_circle_3)


        self.verticalLayout_12.addWidget(self.frame_infos)

        self.frame_texts = QFrame(self.frame_content_home)
        self.frame_texts.setObjectName(u"frame_texts")
        self.frame_texts.setMinimumSize(QSize(600, 0))
        self.frame_texts.setMaximumSize(QSize(16777215, 100))
        self.frame_texts.setFrameShape(QFrame.StyledPanel)
        self.frame_texts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_texts)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.frame_texts)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(600, 50))
        font11 = QFont()
        font11.setFamily(u"Roboto Light")
        font11.setPointSize(14)
        self.label_14.setFont(font11)
        self.label_14.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(33, 33, 75);\n"
"border-radius: 10px;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_14)


        self.verticalLayout_12.addWidget(self.frame_texts, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_content_home)

        self.stackedWidget_2.addWidget(self.page_home)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.frame_content_credits = QFrame(self.page_credits)
        self.frame_content_credits.setObjectName(u"frame_content_credits")
        self.frame_content_credits.setGeometry(QRect(90, 70, 120, 80))
        self.frame_content_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_content_credits.setFrameShadow(QFrame.Raised)
        self.stackedWidget_2.addWidget(self.page_credits)

        self.verticalLayout_10.addWidget(self.stackedWidget_2)


        self.verticalLayout_4.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: rgb(33, 33, 75);")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font12 = QFont()
        font12.setFamily(u"Roboto")
        self.label_credits.setFont(font12)
        self.label_credits.setStyleSheet(u"color: rgb(128, 102, 168);")

        self.verticalLayout_17.addWidget(self.label_credits)


        self.horizontalLayout_8.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_grip)


        self.verticalLayout_4.addWidget(self.credits_bar)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.nivel_dos_gases)
        self.configuracoes = QWidget()
        self.configuracoes.setObjectName(u"configuracoes")
        self.verticalLayout_8 = QVBoxLayout(self.configuracoes)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.configuracoes)
        self.label.setObjectName(u"label")
        font13 = QFont()
        font13.setPointSize(40)
        self.label.setFont(font13)
        self.label.setStyleSheet(u"color: #FFF;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidget.addWidget(self.configuracoes)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText("")
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.closeButton.setText("")
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"       Home", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"             N\u00edvel  ", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"       Config", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"    %p%", None))
        self.progressBar_2.setFormat(QCoreApplication.translate("MainWindow", u"   %p%", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"   Consumo de Hidrog\u00eanio", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"   Consumo de \u00c1gua", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Bem-Vinda Bianca", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_5.setText("")
        self.pushButton_7.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Gerada X Consumida", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Setor: Boa viagem,Pina,Brasilia teimosa", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Temp: 30C\u00ba", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"This Is My App - Title Bar", None))
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nivel de Hidrog\u00eanio", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Gal\u00e3o Principal", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"85%", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Temp: -255C\u00ba", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nivel de \u00c1gua", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"40%", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Temp: 25C\u00ba", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Quantidade De Energia Produzida", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"100kWh", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Total Da Semana:  6MW", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\"If you control the code, you control the world.\"", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"By: Wanderson M. Pimenta", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
    # retranslateUi

