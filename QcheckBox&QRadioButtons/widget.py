from PySide6.QtWidgets import QWidget, QCheckBox, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup

class Widget(QWidget):
    
    def __init__(self):
        super().__init__()
        
        os= QGroupBox("Choose operating system")
        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linuxToggled)
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windowsToggled)
        macOS = QCheckBox("MacOS")
        macOS.toggled.connect(self.macOSToggled)
        
        os_layout = QVBoxLayout()
        os_layout.addWidget(linux)
        os_layout.addWidget(windows)
        os_layout.addWidget(macOS)
        
        os.setLayout(os_layout)
        
        drinks = QGroupBox("choose your drink")
        coffee = QCheckBox("Coffee")
        milkShake = QCheckBox("Milk shake")
        juice = QCheckBox("Juice")
        coffee.setChecked(True)
        
        # Makes the check boxes exclusive
        exclusive_buttons = QButtonGroup(self)
        exclusive_buttons.addButton(coffee)
        exclusive_buttons.addButton(milkShake)
        exclusive_buttons.addButton(juice)
        exclusive_buttons.setExclusive(True)
        
        drinks_layout = QVBoxLayout()
        drinks_layout.addWidget(coffee)
        drinks_layout.addWidget(milkShake)
        drinks_layout.addWidget(juice)
        
        drinks.setLayout(drinks_layout)
        
        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drinks)
        
        answers = QGroupBox("Choose answers")
        answerA = QRadioButton("A")
        answerB = QRadioButton("B")
        answerC = QRadioButton("C")
        
        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answerA)
        answers_layout.addWidget(answerB)
        answers_layout.addWidget(answerC)
        
        answers.setLayout(answers_layout)
        
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(answers)
        self.setLayout(v_layout)
        
    
    def linuxToggled(self, checked):
        print("linux is checked" if checked else "linux is not checked")
    
    def windowsToggled(self, checked):
        print("windows is checked" if checked else "window is not checked")
    
    def macOSToggled(self, checked):
        print("macOS is checked" if checked else "mac is not checked")
            