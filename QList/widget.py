from PySide6.QtWidgets import (
    QWidget,
    QListWidget,
    QAbstractItemView,
    QPushButton,
    QVBoxLayout,
    QInputDialog,
    QLineEdit,
)
from PySide6.QtCore import QDir


class Widget(QWidget):

    # setup
    def __init__(self):
        super().__init__()

        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItem("One")
        self.list_widget.addItem("Two")

        self.list_widget.currentItemChanged.connect(self.currentItemChanged)
        self.list_widget.currentTextChanged.connect(self.currentTextChanged)

        button = QPushButton("Add Item")
        button.clicked.connect(self.add_item)

        button_delete = QPushButton("Delete Item")
        button_delete.clicked.connect(self.delete_item)

        button_rename = QPushButton("Rename Item")
        button_rename.clicked.connect(self.renameItem)

        button_item_count = QPushButton("Item Count")
        button_item_count.clicked.connect(self.count_items)

        button_select = QPushButton("Selected Items")
        button_select.clicked.connect(self.select_items)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.list_widget)
        v_layout.addWidget(button)
        v_layout.addWidget(button_delete)
        v_layout.addWidget(button_rename)
        v_layout.addWidget(button_select)
        v_layout.addWidget(button_item_count)

        self.setLayout(v_layout)

    # slots

    def currentItemChanged(self, item):
        print(f"Current Item : {item.text()}")

    def currentTextChanged(self, txt):
        print(f"Current Text changed : {txt}")

    def add_item(self):
        text, ok = QInputDialog().getText(
            self, "Add Item", "Name", QLineEdit.Normal, QDir.home().dirName()
        )
        if text and ok:
            self.list_widget.addItem(text)

    def delete_item(self):
        self.list_widget.takeItem(self.list_widget.currentRow())

    def count_items(self):
        print(f"number of items = {self.list_widget.count()}")

    def select_items(self):
        for item in self.list_widget.selectedItems():
            print(item.text())

    def renameItem(self):
        text, ok = QInputDialog().getText(
            self, "Rename Item", "Name", QLineEdit.Normal, QDir.home().dirName()
        )
        if text and ok:
            self.list_widget.currentItem().setText(text)
