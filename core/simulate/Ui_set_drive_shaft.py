# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs/core/simulate/set_drive_shaft.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(377, 289)
        Dialog.setMinimumSize(QtCore.QSize(377, 289))
        Dialog.setMaximumSize(QtCore.QSize(377, 289))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.Shaft_num = QtWidgets.QTextBrowser(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Shaft_num.sizePolicy().hasHeightForWidth())
        self.Shaft_num.setSizePolicy(sizePolicy)
        self.Shaft_num.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Shaft_num.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Shaft_num.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Shaft_num.setObjectName("Shaft_num")
        self.verticalLayout.addWidget(self.Shaft_num)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Shaft_Center = QtWidgets.QComboBox(Dialog)
        self.Shaft_Center.setObjectName("Shaft_Center")
        self.gridLayout.addWidget(self.Shaft_Center, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.Start_Angle = QtWidgets.QDoubleSpinBox(Dialog)
        self.Start_Angle.setMinimum(0.0)
        self.Start_Angle.setMaximum(360.0)
        self.Start_Angle.setProperty("value", 0.0)
        self.Start_Angle.setObjectName("Start_Angle")
        self.gridLayout.addWidget(self.Start_Angle, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.End_Angle = QtWidgets.QDoubleSpinBox(Dialog)
        self.End_Angle.setMinimum(0.0)
        self.End_Angle.setMaximum(360.0)
        self.End_Angle.setProperty("value", 360.0)
        self.End_Angle.setObjectName("End_Angle")
        self.gridLayout.addWidget(self.End_Angle, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.References = QtWidgets.QComboBox(Dialog)
        self.References.setObjectName("References")
        self.gridLayout.addWidget(self.References, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.Demo_angle_enable = QtWidgets.QCheckBox(Dialog)
        self.Demo_angle_enable.setChecked(True)
        self.Demo_angle_enable.setObjectName("Demo_angle_enable")
        self.verticalLayout_2.addWidget(self.Demo_angle_enable)
        self.Demo_angle = QtWidgets.QDoubleSpinBox(Dialog)
        self.Demo_angle.setMaximum(360.0)
        self.Demo_angle.setProperty("value", 180.0)
        self.Demo_angle.setObjectName("Demo_angle")
        self.verticalLayout_2.addWidget(self.Demo_angle)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Drive Shaft"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Setting two Points for the New Drive Shaft.</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>New Shaft number</p></body></html>"))
        self.Shaft_Center.setWhatsThis(_translate("Dialog", "Start point for next link."))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>Start Angle</p></body></html>"))
        self.Start_Angle.setSuffix(_translate("Dialog", "°"))
        self.label.setText(_translate("Dialog", "Shaft Center"))
        self.End_Angle.setSuffix(_translate("Dialog", "°"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p>End Angle</p></body></html>"))
        self.References.setWhatsThis(_translate("Dialog", "End point for next link."))
        self.label_2.setText(_translate("Dialog", "References"))
        self.Demo_angle_enable.setText(_translate("Dialog", "Demo Angle"))
        self.Demo_angle.setSuffix(_translate("Dialog", "°"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

