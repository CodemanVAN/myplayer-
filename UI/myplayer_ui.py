# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\myplayer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Myplayer(object):
    def setupUi(self, Myplayer):
        Myplayer.setObjectName("Myplayer")
        Myplayer.resize(835, 681)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Myplayer)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pre_bt = QtWidgets.QPushButton(Myplayer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pre_bt.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../Myplayer/pre.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pre_bt.setIcon(icon)
        self.pre_bt.setObjectName("pre_bt")
        self.gridLayout.addWidget(self.pre_bt, 0, 0, 1, 1)
        self.play_bt = QtWidgets.QPushButton(Myplayer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.play_bt.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../Myplayer/2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_bt.setIcon(icon1)
        self.play_bt.setObjectName("play_bt")
        self.gridLayout.addWidget(self.play_bt, 1, 0, 1, 1)
        self.next_bt = QtWidgets.QPushButton(Myplayer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.next_bt.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\../Myplayer/next.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_bt.setIcon(icon2)
        self.next_bt.setObjectName("next_bt")
        self.gridLayout.addWidget(self.next_bt, 2, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.username = QtWidgets.QLabel(Myplayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.horizontalLayout_3.addWidget(self.username)
        self.username_text = QtWidgets.QLabel(Myplayer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.username_text.setFont(font)
        self.username_text.setObjectName("username_text")
        self.horizontalLayout_3.addWidget(self.username_text)
        self.logout_bt = QtWidgets.QPushButton(Myplayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout_bt.sizePolicy().hasHeightForWidth())
        self.logout_bt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.logout_bt.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\../Myplayer/logout.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_bt.setIcon(icon3)
        self.logout_bt.setObjectName("logout_bt")
        self.horizontalLayout_3.addWidget(self.logout_bt)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nowplay = QtWidgets.QLabel(Myplayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nowplay.sizePolicy().hasHeightForWidth())
        self.nowplay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.nowplay.setFont(font)
        self.nowplay.setObjectName("nowplay")
        self.horizontalLayout_2.addWidget(self.nowplay)
        self.nowplay_info = QtWidgets.QLabel(Myplayer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.nowplay_info.setFont(font)
        self.nowplay_info.setObjectName("nowplay_info")
        self.horizontalLayout_2.addWidget(self.nowplay_info)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(Myplayer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.nowplay_posi = QtWidgets.QSlider(Myplayer)
        self.nowplay_posi.setSingleStep(1)
        self.nowplay_posi.setOrientation(QtCore.Qt.Horizontal)
        self.nowplay_posi.setObjectName("nowplay_posi")
        self.horizontalLayout_8.addWidget(self.nowplay_posi)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vulume_2 = QtWidgets.QLabel(Myplayer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.vulume_2.setFont(font)
        self.vulume_2.setObjectName("vulume_2")
        self.horizontalLayout.addWidget(self.vulume_2)
        self.vulumesilider = QtWidgets.QSlider(Myplayer)
        self.vulumesilider.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.vulumesilider.setMaximum(100)
        self.vulumesilider.setProperty("value", 20)
        self.vulumesilider.setSliderPosition(20)
        self.vulumesilider.setOrientation(QtCore.Qt.Horizontal)
        self.vulumesilider.setInvertedAppearance(False)
        self.vulumesilider.setInvertedControls(False)
        self.vulumesilider.setObjectName("vulumesilider")
        self.horizontalLayout.addWidget(self.vulumesilider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(Myplayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.songlist_choice = QtWidgets.QComboBox(Myplayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songlist_choice.sizePolicy().hasHeightForWidth())
        self.songlist_choice.setSizePolicy(sizePolicy)
        self.songlist_choice.setObjectName("songlist_choice")
        self.horizontalLayout_5.addWidget(self.songlist_choice)
        self.mode_choice = QtWidgets.QComboBox(Myplayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mode_choice.sizePolicy().hasHeightForWidth())
        self.mode_choice.setSizePolicy(sizePolicy)
        self.mode_choice.setObjectName("mode_choice")
        self.mode_choice.addItem("")
        self.mode_choice.addItem("")
        self.mode_choice.addItem("")
        self.horizontalLayout_5.addWidget(self.mode_choice)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(Myplayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.download_bar = QtWidgets.QProgressBar(Myplayer)
        self.download_bar.setProperty("value", 0)
        self.download_bar.setTextVisible(True)
        self.download_bar.setObjectName("download_bar")
        self.horizontalLayout_6.addWidget(self.download_bar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.serach_input = QtWidgets.QLineEdit(Myplayer)
        self.serach_input.setObjectName("serach_input")
        self.horizontalLayout_7.addWidget(self.serach_input)
        self.serach_bt = QtWidgets.QPushButton(Myplayer)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.serach_bt.setFont(font)
        self.serach_bt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\../Myplayer/serach.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.serach_bt.setIcon(icon4)
        self.serach_bt.setObjectName("serach_bt")
        self.horizontalLayout_7.addWidget(self.serach_bt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.songlist = QtWidgets.QListWidget(Myplayer)
        self.songlist.setObjectName("songlist")
        self.verticalLayout_2.addWidget(self.songlist)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(Myplayer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.pushButton = QtWidgets.QPushButton(Myplayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\../Myplayer/donate.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_9.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Myplayer)
        self.songlist_choice.setCurrentIndex(-1)
        self.mode_choice.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Myplayer)

    def retranslateUi(self, Myplayer):
        _translate = QtCore.QCoreApplication.translate
        Myplayer.setWindowTitle(_translate("Myplayer", "Myplayer-这风吹得我真冷"))
        self.pre_bt.setText(_translate("Myplayer", "上一首"))
        self.play_bt.setText(_translate("Myplayer", "   播放"))
        self.next_bt.setText(_translate("Myplayer", "下一首"))
        self.username.setText(_translate("Myplayer", "用户名："))
        self.username_text.setText(_translate("Myplayer", "NoneUser"))
        self.logout_bt.setText(_translate("Myplayer", "登出"))
        self.nowplay.setText(_translate("Myplayer", "正在播放："))
        self.nowplay_info.setText(_translate("Myplayer", "没在播放呢"))
        self.label_3.setText(_translate("Myplayer", "进度："))
        self.vulume_2.setText(_translate("Myplayer", "音量"))
        self.label.setText(_translate("Myplayer", "选择歌单："))
        self.mode_choice.setItemText(0, _translate("Myplayer", "顺序播放"))
        self.mode_choice.setItemText(1, _translate("Myplayer", "循环播放"))
        self.mode_choice.setItemText(2, _translate("Myplayer", "随机播放"))
        self.label_2.setText(_translate("Myplayer", "下载进度："))
        self.serach_bt.setText(_translate("Myplayer", "搜索"))
        self.label_4.setText(_translate("Myplayer", "CopyRight  Reserved   by 这风吹得我真冷"))
        self.pushButton.setText(_translate("Myplayer", "赏口饭（donate）"))
