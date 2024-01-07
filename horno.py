from PyQt5.QtWidgets import (
    QApplication,QWidget,
    QFileDialog, 
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout, QMainWindow, QPushButton
)
import PIL
import os

app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle('Easy Editor')
lb_image = QLabel("Kartinka")
btn_dir = QPushButton("Papka")
lw_files = QListWidget()

btn_left = QPushButton("Levo")
btn_right = QPushButton("Pravo")
btn_flip = QPushButton("Zerko")
btn_sharp = QPushButton("Pezkost")
btn_bw = QPushButton("ch/B")

row =QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image,95)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 20)
win.setLayout(row)

def chooseWorkdir():
    global workdir 
    workdir = QFileDialog.getExistingDirectory()
btn_dir.clicked.connect(chooseWorkdir)


def filter(filenames):
  filtered_filenames = []
  for filename in filenames:
    filename_parts = filename.split(".")
    if filename_parts[-1] in ("png", "jpg"):
      filtered_filenames.append(filenames)
  return filtered_filenames

print()





win.show()
app.exec()