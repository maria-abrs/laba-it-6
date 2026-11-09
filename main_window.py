from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.resize(500, 400)
        self.init_ui()
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.label = QLabel("Новая задача")
        layout.addWidget(self.label)
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Название задачи")
        layout.addWidget(self.task_input)
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)
        buttons_layout = QHBoxLayout()
        layout.addLayout(buttons_layout)
        self.add_button = QPushButton("Добавить")
        buttons_layout.addWidget(self.add_button)
        self.delete_button = QPushButton("Удалить")
        buttons_layout.addWidget(self.delete_button)
        self.clear_button = QPushButton("Очистить всё")
        buttons_layout.addWidget(self.clear_button)
        self.counter_label = QLabel("Количество задач: 0")
        layout.addWidget(self.counter_label)