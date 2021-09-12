from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
import sys
from urllib.request import urlopen
StyleSheet = '''
QCheckBox {
    spacing: 5px;
    font-size:25px;     /* <--- */
}

QCheckBox::indicator {
    width:  33px;
    height: 33px;
}
QListWidget {
    spacing: 5px;
    font-size:20px;     /* <--- */
}
QInputDialog {
    spacing: 5px;
    font-size:30px;     /* <--- */
}

QPlainTextEdit {
    spacing: 5px;
    font-size:30px;     /* <--- */
}

'''   
class MainWindow(QMainWindow):
    def closeEvent(self, e):
        if not text.document().isModified():
            return
        answer = QMessageBox.question(
            window, None,
            "You have unsaved changes. Save before closing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        if answer & QMessageBox.Save:
            save()
            if text.document().isModified():
            	# This happens when the user closes the Save As... dialog.
            	# We do not want to close the window in this case because it
            	# would throw away unsaved changes.
                event.ignore()
        elif answer & QMessageBox.Cancel:
            e.ignore()
    def __init__(self):
        super().__init__()
        text, ok = QInputDialog.getText( self,'MSSV', 'Nhập thông tin MSSV')
        if ok==False:
            sys.exit(0)
        self.username = str(text).strip()
        if len(self.username)<=0:
            sys.exit(0)



        self.html = urlopen("https://raw.githubusercontent.com/phunghx/UTEClass/main/data.py").read().decode()
        self.html = self.html.replace("[MSSV]", self.username)

    
    
app = QApplication([])
app.setApplicationName("Chương trình đánh giá điểm")
text = QPlainTextEdit()
window = MainWindow()
window.setCentralWidget(text)

text.setPlainText(window.html)


menu = window.menuBar().addMenu("&File")
'''
open_action = QAction("&Load")
def open_file():
    global file_path
    path = QFileDialog.getOpenFileName(window, "Open")[0]
    if path:
        text.setPlainText(open(path).read())
        file_path = path
open_action.triggered.connect(open_file)
open_action.setShortcut(QKeySequence.Open)
menu.addAction(open_action)
'''
save_action = QAction("&Export")
file_path = 'E' + window.username + '.bin'
import numpy as np
def save():
    data = text.toPlainText()
    #with open(file_path, "w") as f:
    #        f.write()
    np.save(file_path,data)
    text.document().setModified(False)
save_action.triggered.connect(save)
save_action.setShortcut(QKeySequence.Save)
menu.addAction(save_action)


close = QAction("&Close")
close.triggered.connect(window.close)
menu.addAction(close)

help_menu = window.menuBar().addMenu("&Help")
about_action = QAction("&About")
help_menu.addAction(about_action)
def show_about_dialog():
    text = "<center>" \
           "<h1>Text Editor</h1>" \
           "&#8291;" \
           "<img src=icon.svg>" \
           "</center>" \
           "<p>Version 31.4.159.265358<br/>" \
           "Copyright &copy; Company Inc.</p>"
    QMessageBox.about(window, "About Text Editor", text)
about_action.triggered.connect(show_about_dialog)



window.showMaximized() #FullScreen()
app.setStyleSheet(StyleSheet)
app.exec_()
