# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'electrum_nmc/electrum/gui/qt/forms/configurenamedialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfigureNameDialog(object):
    def setupUi(self, ConfigureNameDialog):
        ConfigureNameDialog.setObjectName("ConfigureNameDialog")
        ConfigureNameDialog.resize(545, 304)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfigureNameDialog.sizePolicy().hasHeightForWidth())
        ConfigureNameDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(ConfigureNameDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.labelNamespace = QtWidgets.QLabel(ConfigureNameDialog)
        self.labelNamespace.setText("TextLabel")
        self.labelNamespace.setObjectName("labelNamespace")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelNamespace)
        self.labelName = QtWidgets.QLabel(ConfigureNameDialog)
        self.labelName.setText("TextLabel")
        self.labelName.setTextFormat(QtCore.Qt.PlainText)
        self.labelName.setObjectName("labelName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelName)
        spacerItem = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label = QtWidgets.QLabel(ConfigureNameDialog)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_4 = QtWidgets.QLabel(ConfigureNameDialog)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.labelTransferTo = QtWidgets.QLabel(ConfigureNameDialog)
        self.labelTransferTo.setObjectName("labelTransferTo")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.labelTransferTo)
        self.transferToLayout = QtWidgets.QHBoxLayout()
        self.transferToLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.transferToLayout.setSpacing(0)
        self.transferToLayout.setObjectName("transferToLayout")
        self.transferTo = QPayToEdit(ConfigureNameDialog)
        self.transferTo.setObjectName("transferTo")
        self.transferToLayout.addWidget(self.transferTo)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.transferToLayout)
        self.labelTransferToHint = QtWidgets.QLabel(ConfigureNameDialog)
        self.labelTransferToHint.setObjectName("labelTransferToHint")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.labelTransferToHint)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dataEdit = QtWidgets.QLineEdit(ConfigureNameDialog)
        self.dataEdit.setMaxLength(520)
        self.dataEdit.setObjectName("dataEdit")
        self.horizontalLayout_3.addWidget(self.dataEdit)
        self.btnDNSEditor = QtWidgets.QPushButton(ConfigureNameDialog)
        self.btnDNSEditor.setObjectName("btnDNSEditor")
        self.horizontalLayout_3.addWidget(self.btnDNSEditor)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.formLayout)
        self.labelSubmitHint = QtWidgets.QLabel(ConfigureNameDialog)
        self.labelSubmitHint.setText("TextLabel")
        self.labelSubmitHint.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSubmitHint.setIndent(10)
        self.labelSubmitHint.setObjectName("labelSubmitHint")
        self.verticalLayout.addWidget(self.labelSubmitHint)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfigureNameDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labelNamespace.setBuddy(self.dataEdit)
        self.label.setBuddy(self.dataEdit)
        self.labelTransferTo.setBuddy(self.transferTo)

        self.retranslateUi(ConfigureNameDialog)
        self.buttonBox.accepted.connect(ConfigureNameDialog.accept)
        self.buttonBox.rejected.connect(ConfigureNameDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureNameDialog)

    def retranslateUi(self, ConfigureNameDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfigureNameDialog.setWindowTitle(_translate("ConfigureNameDialog", "Configure Name"))
        self.label.setText(_translate("ConfigureNameDialog", "&Data:"))
        self.label_4.setText(_translate("ConfigureNameDialog", "JSON string, e.g. {&quot;ip&quot;: [&quot;1.2.3.4&quot;, &quot;1.2.3.5&quot;]}<br>See <a href=\"https://github.com/namecoin/proposals\">JSON value specifications</a>."))
        self.labelTransferTo.setText(_translate("ConfigureNameDialog", "&Transfer to:"))
        self.labelTransferToHint.setText(_translate("ConfigureNameDialog", "(Leave empty if not transferring.)"))
        self.dataEdit.setToolTip(_translate("ConfigureNameDialog", "Enter JSON string that will be associated with the name"))
        self.btnDNSEditor.setText(_translate("ConfigureNameDialog", "DNS Editor…"))
from .qpaytoedit import QPayToEdit


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigureNameDialog = QtWidgets.QDialog()
    ui = Ui_ConfigureNameDialog()
    ui.setupUi(ConfigureNameDialog)
    ConfigureNameDialog.show()
    sys.exit(app.exec_())
