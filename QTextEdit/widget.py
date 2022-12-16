from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout

class Widget(QWidget):
    
    def set_button(self, message:str, slot):
        button = QPushButton(message)
        button.clicked.connect(slot)
        return button
    
    def __init__(self):
        super().__init__()
        
        self.text_edited = QTextEdit()
        
        button_copy = self.set_button("Copy", self.text_edited.copy)
        button_cut = self.set_button("Cut", self.text_edited.cut)
        button_paste = self.set_button("Paste", self.text_edited.paste)
        button_undo = self.set_button("Undo", self.text_edited.undo)
        button_rendo = self.set_button("Redo", self.text_edited.redo)
        button_clear = self.set_button("Clear", self.text_edited.clear)
        button_html = self.set_button("set Html", self.set_plain_html)
        
        h_layout = self.add_multi_widgets_in_Hlayout([button_copy, button_cut, button_paste,button_undo, button_rendo, button_clear, button_html])
        
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edited)
        
        self.setLayout(v_layout)
        
    def add_multi_widgets_in_Hlayout(self, widgets):
        h_layout = QHBoxLayout()
        for widget in widgets:
            h_layout.addWidget(widget)
        return h_layout
    
    def set_plain_html(self):
        self.text_edited.setHtml(self.text_edited.toPlainText())