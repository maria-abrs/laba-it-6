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
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.label = QLabel("Новая задача")
        main_layout.addWidget(self.label)
        input_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Название задачи")
        input_layout.addWidget(self.task_input)
        self.add_button = QPushButton("Добавить")
        input_layout.addWidget(self.add_button)
        self.task_list = QListWidget()
        main_layout.addWidget(self.task_list)
        buttons_layout = QHBoxLayout()
        main_layout.addLayout(buttons_layout)
        self.delete_button = QPushButton("Удалить")
        buttons_layout.addWidget(self.delete_button)
        self.clear_button = QPushButton("Очистить всё")
        buttons_layout.addWidget(self.clear_button)
        self.counter_label = QLabel("Количество задач: 0")
        main_layout.addWidget(self.counter_label)