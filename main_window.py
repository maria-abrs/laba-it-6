from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.resize(500, 400)
        self.init_ui()
        self.connect_signals()
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
    def connect_signals(self):
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
    def delete_task(self):
        row = self.task_list.currentRow()
        if row >= 0:
            answer = QMessageBox.question(
                self,
                "Удаление",
                "Удалить выбранную задачу?"
            )
            if answer == QMessageBox.StandardButton.Yes:
                self.task_list.takeItem(row)
        else:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Выберите задачу для удаления"
            )
    def add_task(self):
        text = self.task_input.text().strip()
        if text:
            self.task_list.addItem(text)
            self.task_input.clear()
        else:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Введите название задачи"
            )