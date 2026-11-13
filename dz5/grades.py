import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QPushButton, QComboBox, QListWidget,
    QVBoxLayout, QHBoxLayout, QMessageBox, QScrollArea, QFrame
)


class GradeCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.grades = []
        self.setWindowTitle("Калькулятор оценок")
        self.resize(480, 600)

        ## Прокрутка для небольших экранов
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        widget = QWidget()
        scroll.setWidget(widget)
        self.setCentralWidget(scroll)

        layout = QVBoxLayout(widget)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(8)

        ## Заголовок
        title = QLabel("Калькулятор оценок")
        title.setObjectName("title")
        layout.addWidget(title)

        ## Средний балл
        self.average_label = QLabel("Средний балл: —")
        self.average_label.setObjectName("average")
        layout.addWidget(self.average_label)

        self.count_label = QLabel("Количество оценок: 0")
        layout.addWidget(self.count_label)

        ## Выбор и добавление оценки
        layout.addWidget(QLabel("Выберите оценку:"))
        row = QHBoxLayout()
        self.grade_input = QComboBox()
        self.grade_input.addItems(["2", "3", "4", "5"])
        row.addWidget(self.grade_input)

        add_button = QPushButton("Добавить оценку")
        add_button.clicked.connect(self.add_grade)
        row.addWidget(add_button)
        layout.addLayout(row)

        ## Список оценок
        layout.addWidget(QLabel("Мои оценки:"))
        self.grade_list = QListWidget()
        self.grade_list.setMinimumHeight(90)
        self.grade_list.setMaximumHeight(150)
        layout.addWidget(self.grade_list)

        delete_button = QPushButton("Удалить выбранную оценку")
        delete_button.clicked.connect(self.delete_grade)
        layout.addWidget(delete_button)

        ## Выбор желаемого среднего балла
        layout.addWidget(QLabel("Желаемый средний балл:"))
        self.target = QComboBox()
        self.target.addItems(["3.0", "3.5", "4.0", "4.5", "4.8"])
        self.target.setCurrentText("4.5")
        layout.addWidget(self.target)

        calculate_button = QPushButton("Рассчитать")
        calculate_button.clicked.connect(self.calculate)
        layout.addWidget(calculate_button)

        ## Результат расчёта
        self.result = QLabel("")
        self.result.setWordWrap(True)
        self.result.setMinimumHeight(65)
        self.result.setObjectName("result")
        layout.addWidget(self.result)

        ## Светлая тема с контрастным текстом
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #f6f7fb;
                color: #222222;
                font-size: 14px;
            }
            QLabel {
                color: #222222;
                background: transparent;
            }
            QLabel#title {
                font-size: 23px;
                font-weight: bold;
            }
            QLabel#average {
                color: #394fc3;
                font-size: 21px;
                font-weight: bold;
                padding: 10px;
                background: #e6ebff;
                border-radius: 8px;
            }
            QLabel#result {
                color: #263a8d;
                font-weight: bold;
                padding: 8px;
            }
            QComboBox, QListWidget {
                color: #222222;
                background-color: #ffffff;
                border: 1px solid #9da7c4;
                border-radius: 6px;
                padding: 7px;
                min-height: 22px;
            }
            QComboBox QAbstractItemView {
                color: #222222;
                background-color: #ffffff;
                selection-color: #ffffff;
                selection-background-color: #596bcd;
            }
            QPushButton {
                background-color: #596bcd;
                color: #ffffff;
                border: none;
                border-radius: 6px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #4053b0;
            }
        """)

    ## Добавление оценки
    def add_grade(self):
        grade = int(self.grade_input.currentText())
        self.grades.append(grade)
        self.grade_list.addItem(str(grade))
        self.update_average()

    ## Удаление выбранной оценки
    def delete_grade(self):
        index = self.grade_list.currentRow()

        if index == -1:
            QMessageBox.warning(self, "Ошибка", "Сначала выберите оценку в списке!")
            return

        self.grades.pop(index)
        self.grade_list.takeItem(index)
        self.update_average()

    ## Пересчёт среднего балла
    def update_average(self):
        count = len(self.grades)
        self.count_label.setText(f"Количество оценок: {count}")

        if count > 0:
            average = sum(self.grades) / count
            self.average_label.setText(f"Средний балл: {average:.2f}")
        else:
            self.average_label.setText("Средний балл: —")

        self.result.clear()

    ## Расчёт количества пятёрок
    def calculate(self):
        if len(self.grades) == 0:
            QMessageBox.warning(self, "Ошибка", "Сначала добавьте оценки!")
            return

        desired = float(self.target.currentText())
        total = sum(self.grades)
        count = len(self.grades)

        if total / count >= desired:
            self.result.setText("Желаемый средний балл уже достигнут!")
            return

        needed = 0
        while (total + needed * 5) / (count + needed) < desired:
            needed += 1

        ## Подбираем правильное окончание слова
        if needed % 10 == 1 and needed % 100 != 11:
            word = "пятёрку"
        elif needed % 10 in (2, 3, 4) and needed % 100 not in (12, 13, 14):
            word = "пятёрки"
        else:
            word = "пятёрок"

        self.result.setText(
            f"Для среднего балла {desired} нужно получить ещё {needed} {word}."
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradeCalculator()
    window.show()
    sys.exit(app.exec())

