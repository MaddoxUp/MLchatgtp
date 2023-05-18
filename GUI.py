import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QMenu, QListView, QListWidgetItem, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QIcon, QKeyEvent
from PyQt5.QtCore import Qt, QEvent

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Chat GUI')

        # List View
        self.session_list = QListView()
        self.session_list.setModel(QStandardItemModel())

        # Add item to the list
        self.session_list.model().appendRow(QStandardItem("Session 1"))

        # Text Edit
        self.text_edit = QTextEdit()
        self.text_edit.installEventFilter(self)

        # Button
        self.send_button = QPushButton('Send', self)
        self.send_button.clicked.connect(self.on_click)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.session_list)
        vbox.addWidget(self.text_edit)
        vbox.addWidget(self.send_button)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.show()

    def eventFilter(self, obj, event):
        if obj == self.text_edit:
            if event.type() == QEvent.KeyPress:
                keyEvent = QKeyEvent(event)
                if keyEvent.key() == Qt.Key_Return and not keyEvent.isAutoRepeat():
                    # Enter pressed, do something
                    print('Enter pressed')
                    return True
        # pass the event on to the parent class
        return QMainWindow.eventFilter(self, obj, event)

    def on_click(self):
        print('Button clicked, do something')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec_())
