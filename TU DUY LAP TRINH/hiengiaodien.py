import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QListView
from untitled import *
from PyQt6.QtCore import QStringListModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bntremove.hide()
        self.ui.buttonchangetodone.hide()
        self.ui.buttonremoveindone.hide()
        self.ui.buttonchangebacktotodolist.hide()
        self.connection()
    def show(self):
        super().show()
    def connection(self):
    #Well well well button to change page
        self.ui.todolistbutton.clicked.connect(lambda: self.home_page(0) )
        self.ui.donebutton.clicked.connect(lambda: self.home_page(1) )
        self.ui.quaylaitrangtodolist.clicked.connect(lambda: self.done_page(0)) #QUAY LAI TRANG BAN DAU
    #Button to interact with the page
        self.ui.bntadd.clicked.connect(self.add_item)
        self.ui.bntremove.clicked.connect(self.remove_item)
        self.ui.todolist_list.clicked.connect(self.show_remove_item) #KHI BAM VAO LIST SE HIEN CHUC NANG
        self.ui.buttonchangetodone.clicked.connect(self.additemtodone)
        self.ui.buttonchangebacktotodolist.clicked.connect(self.add_to_todolist)
        self.ui.buttonremoveindone.clicked.connect(self.delete_item)
        self.ui.done_list.clicked.connect(self.show_delete)
    #Todolist page
        self.todolist = QStringListModel()
        datatodolist = []
        self.todolist.setStringList(datatodolist)
        self.ui.todolist_list.setModel(self.todolist)
        self.todolist_index = None
        self.donelist_index = None
    #Done page
        self.tasktracker = QStringListModel()
        datadone = []
        self.tasktracker.setStringList(datadone)
        self.ui.done_list.setModel(self.tasktracker)

    #TO DO LIST FUNCTION:
    def add_item(self):

        adding = self.ui.add.text()
        current_list = self.todolist.stringList()
        current_list.append(adding)
        self.todolist.setStringList(current_list)
    #LUU VI TRI DE XOA/CHUYEN DU LIEU QUA DONE
    def show_remove_item(self, index):
        self.ui.bntremove.show()
        self.ui.buttonchangetodone.show()
        self.todolist_index = index
    #CHUC NANG XOA
    def remove_item(self):
        current_list = self.todolist.stringList()
        if self.todolist_index is None:
            return
        del current_list[self.todolist_index.row()]
        self.todolist.setStringList(current_list)
        self.ui.bntremove.hide()
        self.ui.buttonchangetodone.hide()
    #CHUYEN DU LIEU QUA DONE
    def additemtodone(self):
        done_list = self.tasktracker.stringList()
        to_do_list = self.todolist.stringList()
        if self.todolist_index is None:
            return
        value = self.todolist_index.data()
        done_list.append(value)
        del to_do_list[self.todolist_index.row()]
        self.todolist.setStringList(to_do_list)
        self.tasktracker.setStringList(done_list)
        self.ui.bntremove.hide()
        self.ui.buttonchangetodone.hide()
    #DONE FUNCTION:
    def show_delete(self, index):
        self.donelist_index = index
        self.ui.buttonremoveindone.show()
        self.ui.buttonchangebacktotodolist.show()
    def delete_item(self):
        if self.donelist_index is None:
            return
        done_List = self.tasktracker.stringList()
        del done_List[self.donelist_index.row()]
        self.tasktracker.setStringList(done_List)
        self.ui.buttonchangebacktotodolist.hide()
        self.ui.buttonremoveindone.hide()
    def add_to_todolist(self):
        todolist_list = self.todolist.stringList()
        done_list = self.tasktracker.stringList()
        if self.donelist_index is None:
            return
        value = self.donelist_index.data()
        todolist_list.append(value)
        del done_list[self.donelist_index.row()]
        self.todolist.setStringList(todolist_list)
        self.tasktracker.setStringList(done_list)
        self.ui.buttonremoveindone.hide()
        self.ui.buttonchangebacktotodolist.hide()


    #TRANG CHINH
    def home_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
    #TRANG DONE
    def done_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
