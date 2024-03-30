import sqlite3
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog


querys = {
    "delete": "DELETE FROM coffee",
    "get": "SELECT * FROM coffee"
}


class Ui_MainWindow:
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 595)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 0, 431, 23))
        self.pushButton.setObjectName("pushButton")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 761, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 30, 201, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 30, 201, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        t = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(t("MainWindow", "MainWindow"))
        self.pushButton.setText(t("MainWindow", "Показать информацию о кофе"))
        self.pushButton_2.setText(t("MainWindow", "Добавить запись"))
        self.pushButton_3.setText(t("MainWindow", "Редактировать запись"))



class Ui_dialog:
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(610, 374)

        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(230, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")

        self.verticalLayoutWidget = QtWidgets.QWidget(dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 20, 381, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")

        self.verticalLayout.addWidget(self.lineEdit_1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 160, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")

        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.label_5)
        self.verticalLayout_2.addWidget(self.label_6)

        self.retranslateUi(dialog)

        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)

        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        t = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(t("dialog", "Dialog"))
        self.label.setText(t("dialog", "Название сорта"))
        self.label_2.setText(t("dialog", "Степень обжарки"))
        self.label_3.setText(t("dialog", "Молотый/в зернах"))
        self.label_4.setText(t("dialog", "Описание вкуса"))
        self.label_5.setText(t("dialog", "Цена"))
        self.label_6.setText(t("dialog", "Объём упаковки"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initDB()
        self.initUI()
        self.pushButton.clicked.connect(self.showAll)
        self.pushButton_2.clicked.connect(lambda: self.addRow([]))
        self.pushButton_3.clicked.connect(self.editDB)

    def initDB(self):
        self.cur = sqlite3.connect("../data/coffee.sqlite").cursor()

    def initUI(self):
        columns = ["ID",
                   "Название сорта",
                   "Степень обжарки",
                   "Молотый/в зернах",
                   "Описание вкуса",
                   "Цена",
                   "Объем упаковки"]
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.resizeColumnsToContents()
        self.rowMarked = -1
        self.tableWidget.cellClicked.connect(self.markRow)

    def removeDB(self):
        self.cur.execute(querys["delete"]).fetchall()

    def showAll(self):
        columns = ["ID",
                   "Название сорта",
                   "Степень обжарки",
                   "Молотый/в зернах",
                   "Описание вкуса",
                   "Цена",
                   "Объем упаковки"]
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)
        result = self.cur.execute(querys["get"]).fetchall()
        table = self.tableWidget
        table.setRowCount(len(result))

        for i, row in enumerate(result):
            for j, col in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(col)))

        table.resizeColumnsToContents()

        if result:
            message = f"Нашлось {str(len(result))} записей"
        else:
            message = "К сожалению, ничего не нашлось"

        self.statusBar().showMessage(message)

    def markRow(self, row, column):
        self.rowMarked = row

    def addRow(self, data):
        newDialog = QDialog(self)
        newWindow = Ui_dialog()
        newWindow.setupUi(newDialog)
        newDialog.setWindowTitle("Добавить новую запись")
        newWindow.buttonBox.accepted.connect(lambda: self.saveRow(newWindow.verticalLayout))
        if data:
            vert = newWindow.verticalLayout
            for i, text in enumerate(data):
                vert.itemAt(i).widget().setText(text)
        newDialog.show()

    def saveRow(self, layout):
        vert = layout

        data = []
        for i in range(layout.count()):
            vert.itemAt(i).widget().text()

        if all(data):
            values = "NULL, " + ', '.join(map(lambda x: f"'{x}'", data))
            query = f"""
                    INSERT INTO coffee
                    VALUES ({values})
                    """
            try:
                self.cur.execute(query)
                self.cur.connection.commit()
                self.showAll()
            except:
                self.saveRow(layout)
        else:
            self.addRow(data)

    def editDB(self):
        if self.rowMarked < 0:
            return
        table = self.tableWidget
        columnsNum = table.columnCount()
        newDialog = QDialog(self)
        newWindow = Ui_dialog()
        newWindow.setupUi(newDialog)
        newDialog.setWindowTitle("Редактировать запись")

        data = []
        for col in range(columnsNum):
            data.append(table.item(self.rowMarked, col).text())

        vert = newWindow.verticalLayout

        for i, text in enumerate(data[1:]):
            vert.itemAt(i).widget().setText(text)

        newWindow.buttonBox.accepted.connect(lambda: self.updateRow(data[0], newWindow.verticalLayout))
        newDialog.show()

    def updateRow(self, rowId, layout):
        vert = layout
        data = []

        for i in range(layout.count()):
            data.append(vert.itemAt(i).widget().text())

        if all(data):
            query = f"""
            UPDATE coffee
            SET sortName = '{data[0]}',
            grillRate = '{data[1]}',
            beansOrGround = '{data[2]}',
            tasteDescription = '{data[3]}',
            price = '{data[4]}',
            volume = '{data[5]}'
            WHERE id = '{rowId}'
            """
            try:
                self.cur.execute(query)
                self.rowMarked = -1
                self.cur.connection.commit()
                self.showAll()
            except:
                self.updateRow(rowId, layout)


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
