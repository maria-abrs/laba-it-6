from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
    QListWidgetItem,
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
        self.done_button = QPushButton("Выполнить")
        buttons_layout.addWidget(self.done_button)
        self.delete_button = QPushButton("Удалить")
        buttons_layout.addWidget(self.delete_button)
        self.clear_button = QPushButton("Очистить всё")
        buttons_layout.addWidget(self.clear_button)
        self.counter_label = QLabel("Количество задач: 0 (выполнено: 0)")
        main_layout.addWidget(self.counter_label)
        self.statusBar().showMessage("Готово к работе")
    def connect_signals(self):
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.done_button.clicked.connect(self.toggle_done)
        self.delete_button.clicked.connect(self.delete_task)
        self.clear_button.clicked.connect(self.clear_tasks)
        self.task_list.itemChanged.connect(self.update_counter)
    def add_task(self):
        text = self.task_input.text().strip()
        if text:
            item = QListWidgetItem(text)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.task_list.addItem(item)
            self.task_input.clear()
            self.update_counter()
            self.statusBar().showMessage("Задача добавлена", 3000)
        else:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Введите название задачи"
            )
    def toggle_done(self):
        item = self.task_list.currentItem()
        if item is not None:
            if item.checkState() == Qt.CheckState.Checked:
                item.setCheckState(Qt.CheckState.Unchecked)
                self.statusBar().showMessage("Задача снова активна", 3000)
            else:
                item.setCheckState(Qt.CheckState.Checked)
                self.statusBar().showMessage("Задача выполнена", 3000)
        else:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Выберите задачу для отметки"
            )
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
                self.update_counter()
                self.statusBar().showMessage("Задача удалена", 3000)
        else:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Выберите задачу для удаления"
            )
    def clear_tasks(self):
        if self.task_list.count() > 0:
            answer = QMessageBox.question(
                self,
                "Очистка",
                "Удалить все задачи?"
            )
            if answer == QMessageBox.StandardButton.Yes:
                self.task_list.clear()
                self.update_counter()
                self.statusBar().showMessage("Список очищен", 3000)
        else:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Список задач пуст"
            )
    def update_counter(self):
        count = self.task_list.count()
        done = sum(
            1
            for i in range(count)
            if self.task_list.item(i).checkState() == Qt.CheckState.Checked
        )
        self.counter_label.setText(
            f"Количество задач: {count} (выполнено: {done})"
        )
        if count > 0:
            self.setWindowTitle(f"Менеджер задач — задач: {count}")
        else:
            self.setWindowTitle("Менеджер задач")