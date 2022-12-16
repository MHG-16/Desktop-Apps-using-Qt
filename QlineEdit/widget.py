from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit 

class Widget(QWidget):
    def init_line_edit(self):
        self.line_edit = QLineEdit()
        self.set_slots_line_edit()
    
    def set_slots_line_edit(self):
        self.line_edit.textChanged.connect(self.changed)
        self.line_edit.cursorPositionChanged.connect(self.cursorPositionChanged)
        self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.returnPressed.connect(self.return_pressed)
        self.line_edit.selectionChanged.connect(self.selectionChanged)
        self.line_edit.textEdited.connect(self.textEdited)
        
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QLabel and QLineEdit")
        
        #A set of signals we can connect to
        label = QLabel("Full name: ")
        self.init_line_edit()
        
        button = QPushButton("Grab data...")
        button.clicked.connect(self.button_Clicked)
        self.text_holder_label = QLabel("I am here")
        
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)
        
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)
        
        self.setLayout(v_layout)
    
    def button_Clicked(self):
        self.text_holder_label.setText(f"I am {self.line_edit.text()}")
        
    def changed(self):
        self.text_holder_label.setText(self.line_edit.text())
    
    def cursorPositionChanged(self, old, new):
        print (f"old position:{old}, new position:{new}")
    
    def editing_finished(self):
        print ("editing finished")
    
    def return_pressed(self):
        print ("return pressed")
        
    def selectionChanged(self):
        print (f"Selection changed : {self.line_edit.selectedText()}")
    
    def textEdited(self, newText: str):
        print (f"textEdited : {newText}")