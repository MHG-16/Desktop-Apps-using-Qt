from PySide6.QtWidgets import (
    QWidget,
    QTabWidget,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout
)


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        tab_widget = QTabWidget()

        # Informations
        widget_form = QWidget()
        label_full_name = QLabel("Full Name: ")
        line_edit = QLineEdit()
        h_layout = QHBoxLayout()
        h_layout.addWidget(label_full_name)
        h_layout.addWidget(line_edit)
        widget_form.setLayout(h_layout)

        # buttons
        widget_buttons = QWidget()
        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        v_layout = QVBoxLayout()
        v_layout.addWidget(button1)
        v_layout.addWidget(button2)
        v_layout.addWidget(button3)
        widget_buttons.setLayout(v_layout)
        
        #add tabs
        tab_widget.addTab(widget_form, "Informations")
        tab_widget.addTab(widget_buttons, "buttons")
        
        v_layout = QVBoxLayout()
        v_layout.addWidget(tab_widget)
        self.setLayout(v_layout)