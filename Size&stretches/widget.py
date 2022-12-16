from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sizes polices and stretches")
        
        label = QLabel("Some Text: ")
        line_edit = QLineEdit()
        
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(line_edit)
        #horizontal alignment and vertical alignment
        line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        
        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        
        #divise h_layout in 4 grid . The first button get 2 grid and the rest get eachone 1 grid
        
        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(button_1, 2)
        h_layout2.addWidget(button_2, 1)
        h_layout2.addWidget(button_3, 1)
        
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout2)
        self.setLayout(v_layout)