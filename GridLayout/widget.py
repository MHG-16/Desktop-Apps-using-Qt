from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QSizePolicy


class Widget(QWidget):
    
    def __init__(self):
        super().__init__()
        buttons = [QPushButton(msg) for msg in ["one", "two", "three", "four", "five", "six", "seven"]]
        buttons[2].setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        
        gridLayout = QGridLayout()
        gridLayout.addWidget(buttons[0], 0, 0)
        gridLayout.addWidget(buttons[1], 0, 1, 1, 2)
        gridLayout.addWidget(buttons[2], 1, 0, 2, 1)
        gridLayout.addWidget(buttons[3], 1, 1)
        gridLayout.addWidget(buttons[4], 1, 2)
        gridLayout.addWidget(buttons[5], 2, 1)
        gridLayout.addWidget(buttons[6], 2, 2)
        
        self.setLayout(gridLayout)