import sys


from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from untitled import *
from xuly import *
from PyQt6.QtCore import QStringListModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.removebut.hide()
        self.ui.button_to_done.hide()
        self.ui.remarkablebut.hide()
        self.ui.removebutprior.hide()
        self.ui.removebutdone.hide()
        self.ui.button_to_todo.hide()
        self.ui.unmarkbutton.hide()
        self.ui.editbut.hide()


        # Todolist page
        self.todolist = QStringListModel()
        datatodolist = []
        self.todolist.setStringList(datatodolist)
        self.ui.listcv.setModel(self.todolist)
        self.todolist_index = None

        # Done page
        self.done = QStringListModel()
        datadone = []
        self.done.setStringList(datadone)
        self.ui.listcvhoanthanh.setModel(self.done)
        self.donelist_index = None

        #RANDOM CÂU TRUYỀN ĐỘNG LỰC
        randoms = "No"
        self.ui.linetruyendongluc.setText(motivation(randoms))
        self.connection()

        #PRIORITY
        self.prioritytask = QStringListModel()
        dataprior = []
        self.prioritytask.setStringList(dataprior)
        self.ui.listcvquantrong.setModel(self.prioritytask)
        self.prior_index = None

    def show(self):
        super().show()

    def connection(self):

    #Well well well button to change page
        self.ui.todolistbutton.clicked.connect(lambda: self.home_page(0) )
        self.ui.donebutton.clicked.connect(lambda: self.home_page(1) )

    #Button to interact with the page
        self.ui.addbut.clicked.connect(self.add_item)
        self.ui.removebut.clicked.connect(self.remove_item)
        self.ui.listcv.clicked.connect(self.show_item) #KHI BAM VAO LISTCV SE HIEN CHUC NANG
        self.ui.button_to_done.clicked.connect(self.additemtodone)
        self.ui.button_to_todo.clicked.connect(self.add_to_todolist)
        self.ui.removebutdone.clicked.connect(self.delete_item)
        self.ui.listcvhoanthanh.clicked.connect(self.show_delete) #KHI BAM VAO LISTCV SE HIEN CHUC NANG
        self.ui.remarkablebut.clicked.connect(self.add_to_prior)
        self.ui.unmarkbutton.clicked.connect(self.add_back_todolist)
        self.ui.listcvquantrong.clicked.connect(self.show_prior) #KHIBAM VAO LISTCV SE HIEN CHUC NANG
        self.ui.removebutprior.clicked.connect(self.erase_item_in_prior)
        self.ui.editbut.clicked.connect(self.edit)

    #TO DO LIST FUNCTION:
    def add_item(self):

        adding = self.ui.fill.text()
        current_list = self.todolist.stringList()
        current_list.append(adding)
        self.todolist.setStringList(current_list)
    def edit(self):
        if self.todolist_index is None:
            QMessageBox.warning(self, "Lỗi", "Chưa chọn gì cả")
            return
        current_list = self.todolist.stringList()
        new = self.ui.fill.text()
        if not new:
            QMessageBox.warning(self,"Lỗi", "Chưa nhập gì cả")
            return
        current_list[self.todolist_index.row()] = new
        self.todolist.setStringList(current_list)
        self.todolist_index = None
        self.ui.editbut.hide()
        self.ui.addbut.show()
        self.ui.removebut.hide()
        self.ui.button_to_done.hide()
        self.ui.remarkablebut.hide()


    #LUU VI TRI DE XOA/CHUYEN DU LIEU QUA DONE
    def show_item(self, index):

        self.ui.removebut.show()
        self.ui.button_to_done.show()
        self.ui.remarkablebut.show()
        self.todolist_index = index
        value = self.todolist_index.data()
        self.ui.fill.setText(value)
        self.ui.addbut.hide()
        self.ui.editbut.show()

    #CHUC NANG XOA
    def remove_item(self):

        current_list = self.todolist.stringList()
        if self.todolist_index is None:
            return
        del current_list[self.todolist_index.row()]
        self.todolist.setStringList(current_list)
        self.ui.removebut.hide()
        self.ui.button_to_done.hide()
        self.ui.remarkablebut.hide()
        self.ui.editbut.hide()
        self.ui.addbut.show()

    #CHUYEN DU LIEU QUA DONE
    def additemtodone(self):

        random = "Yes"
        self.ui.linetruyendongluc.setText(motivation(random))
        done_list = self.done.stringList()
        to_do_list = self.todolist.stringList()
        if self.todolist_index is None:
            return
        value = self.todolist_index.data()
        done_list.append(value)
        del to_do_list[self.todolist_index.row()]
        self.todolist.setStringList(to_do_list)
        self.done.setStringList(done_list)

        self.ui.removebut.hide()
        self.ui.button_to_done.hide()
        self.ui.remarkablebut.hide()
        self.ui.editbut.hide()
        self.ui.addbut.show()
        self.ui.listcv.clearSelection()

    def add_to_prior(self):

        if self.todolist_index is None:
            return
        todolist = self.todolist.stringList()
        priorlist = self.prioritytask.stringList()
        priorlist.append(self.todolist_index.data())
        del todolist[self.todolist_index.row()]
        self.todolist.setStringList(todolist)
        self.prioritytask.setStringList(priorlist)
        self.ui.removebut.hide()
        self.ui.remarkablebut.hide()
        self.ui.button_to_done.hide()
        self.ui.editbut.hide()
        self.ui.addbut.show()

    #PRIORITY FUNCTION:
    def show_prior(self, index):

        self.prior_index = index
        self.ui.unmarkbutton.show()
        self.ui.removebutprior.show()

    def add_back_todolist(self):

        if self.prior_index is None:
            return
        todolist = self.todolist.stringList()
        priorlist = self.prioritytask.stringList()
        todolist.append(self.prior_index.data())
        del priorlist[self.prior_index.row()]
        self.todolist.setStringList(todolist)
        self.prioritytask.setStringList(priorlist)
        self.ui.unmarkbutton.hide()
        self.ui.removebutprior.hide()

    def erase_item_in_prior(self):

        if self.prior_index is None:
            return
        priorlist = self.prioritytask.stringList()
        del priorlist[self.prior_index.row()]
        self.prioritytask.setStringList(priorlist)
        self.ui.removebutprior.hide()
        self.ui.unmarkbutton.hide()

    #DONE FUNCTION:
    def show_delete(self, index):

        self.donelist_index = index
        self.ui.removebutdone.show()
        self.ui.button_to_todo.show()

    def delete_item(self):

        if self.donelist_index is None:
            return
        done_List = self.done.stringList()
        del done_List[self.donelist_index.row()]
        self.done.setStringList(done_List)
        self.ui.button_to_todo.hide()
        self.ui.removebutdone.hide()

    def add_to_todolist(self):

        todolist_list = self.todolist.stringList()
        done_list = self.done.stringList()
        if self.donelist_index is None:
            return
        value = self.donelist_index.data()
        todolist_list.append(value)
        del done_list[self.donelist_index.row()]
        self.todolist.setStringList(todolist_list)
        self.done.setStringList(done_list)
        self.ui.removebutdone.hide()
        self.ui.button_to_todo.hide()

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

