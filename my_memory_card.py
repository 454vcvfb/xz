from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton,  QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer 
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = [ Question('Какой национальности не существует?', 'Я не знаю', 'Смурфы', 'Чумельцы' ,'Алеут'),
                Question('Кто ты такой?', 'Инопрешеленец','я', 'Артур Пирожков', 'забор'),
                Question('Столица Бразилии?', 'Бразилия', 'Китай', 'Рио-Дежанейро', 'Бразилия'),
                Question('Сколько будет 2+2*6', '14' , '12', '6', '13'),
                Question('Do you speak English?', 'да', 'yes', 'нет', 'no'),
                Question('На какой планете ты живёшь?', 'Марс','Земля', 'Юпитер', 'Сатурн'),
                Question('Какой самый длинный орган у человека?', 'Язык', 'Печень', 'Кишечник', 'Кожа'),
                Question('Сколько будет 4+2*6', '16' , '12', '6', '13'),
                Question('Какого цвета енет на флаге Беларуси?', 'Ярко-красного', 'Красного', 'Зелёног', 'Белого'),
                Question('Кто написал стихотворение "Вы любите розы?"', 'Маяковский' , 'Пушкин', 'Лермонтов', 'Толстой'),]

app = QApplication([])
mw = QWidget()
mw.setWindowTitle('Memory Card')


lb_question = QLabel('Какой национальности не существует?')
btn_OK = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов:')

rbtn_1 = QRadioButton('Я не знаю')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чумельцы')
rbtn_4 = QRadioButton('Алеут')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('правильно/неправильно')
lb_Correct = QLabel('правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignVCenter)
AnsGroupBox.setLayout(layout_res)



layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()
layout_line3.addWidget(btn_OK, stretch = 2)
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

mw.setLayout(layout_card)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answers():
    if answers[0].isChecked():
        show_correct('Правильно!')
        print('Рейтинг:', mw.score/mw.total*100, '%')
        mw.score += 1
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно!')

def next_question():
    if len(question_list) > 0:
        print('Статистика\n-Всего вопросов:', mw.total, '\n-Правильных ответов:', mw.score)
        mw.total += 1
        cur_question = randint(0, len(question_list) -1)
        q = question_list[cur_question]
        ask(q)
        question_list.pop(cur_question)
    else:
        print('Чё самый умный? Вопросы закончились :)')
    
        
def click_OK():
    
    if btn_OK.text() =='Ответить':
        check_answers()
    else:
        next_question()
mw.score = 0
mw.total = 0
next_question()
btn_OK.clicked.connect(click_OK)

mw.show()
app.exec()