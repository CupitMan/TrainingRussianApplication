from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QListWidgetItem, QInputDialog
from PyQt5 import QtCore
import HelpingFunctionsMainWindow as support
import HelpingFuctionsAccentsWindow as acsupport
import HelpingFunctionsSpellingsWindow as assupport
import HelpingEndWindow as endsupport
import datetime
import JsonWorking
from ClassAccent import *
import FileWorkingClass as bd
import random
from HelpingFuctionsAccentsWindow import FONT_FAMILY
from ClassSpellingWord import SpellingWord
import Statistic as stat
import HelpingFunctionStatisticWindow as stsupport
from StatisticWidget import StatisticWidget


accents_worker = bd.FileWorker('AllAccents.csv', 'HardAccents.csv')
spelling_worker = bd.FileWorker('AllSpelling.csv', 'HardSpelling.csv')


class MainDesign(object):


    # Main Function of design main window
    def MainDesign(self, window: QMainWindow):

        # Constants
        SIZE = (1100, 800)
        TITLE = "ЕГЭ ПО РУССКОМУ 2022"
        self.window = window
        self.vowels = ["Э", "Ё", "Ю", "Я", "И", "А", "О", "Ы", "Е", "У"]

        # Window size, title and central widget
        self.StandartWindowSettings(window, SIZE, TITLE)

        # Layouts
        self.MainLayoutSetup()

        # Header
        support.CreateMainWindowHeader(self, "header1.png", "ТРЕНАЖЕР ПО УДАРЕНИЯМ И ОРФОГРАФИИ")

        # Buttons
        self.CreateMainTestButtons()

        # Labels
        self.label_all_accents = support.CreateButtonsLabel(1)
        self.label_all_spelling = support.CreateButtonsLabel(3)
        self.label_hard_accents = support.CreateButtonsLabel(2)
        self.label_hard_spelling = support.CreateButtonsLabel(4)

        # Button title labels
        self.label_accents = support.CreateButtonTitleLabel("УДАРЕНИЯ")
        self.label_spelling = support.CreateButtonTitleLabel("ОРФОГРАФИЯ")


        # Vectors
        self.AcSpLabels = [self.label_all_accents, self.label_hard_accents,
                           self.label_all_spelling, self.label_hard_spelling]
        self.AcSpButtons = [self.button_all_accents, self.button_hard_accents,
                            self.button_all_spelling, self.button_hard_spelling]
        self.AcSpTitleLabels = [self.label_accents, self.label_spelling]

        AcSpLayout = support.CreateVerticalWithHorizontals(self.AcSpButtons, self.AcSpLabels, self.AcSpTitleLabels)

        self.window_buttons_layout.addLayout(AcSpLayout)

        support.AddBorderToInfo(self.window_information_layout)
        support.AddInfoToInfo(self.window_information_layout, self)

        self.button_all_accents.clicked.connect(self.StartDialogAllAccents)
        self.button_hard_accents.clicked.connect(self.StartDialogHardAccents)
        self.button_all_spelling.clicked.connect(self.StartDialogAllSpellings)
        self.button_hard_spelling.clicked.connect(self.StartDialogHardSpellings)


    # Function layouts of main window
    def MainLayoutSetup(self):

        # Main Window Layout
        self.window_main_layout = QVBoxLayout(self.window.central)
        self.window_main_layout.setContentsMargins(0, 0, 0, 0)
        self.window_main_layout.setSpacing(0)

        # Header
        self.window_header_widget = support.CreateHeaderWidget()
        self.window_main_layout.addWidget(self.window_header_widget)

        # Header Layout
        self.window_header_layout = QHBoxLayout(self.window_header_widget)

        # Body Widget
        self.window_body_widget = support.CreateBodyWidget()
        self.window_main_layout.addWidget(self.window_body_widget)

        # Horizontal Body Layout
        self.window_body_layout = QHBoxLayout(self.window_body_widget)
        self.window_body_layout.setContentsMargins(0, 0, 0, 0)
        self.window_body_layout.setSpacing(0)

        # Buttons Widget
        self.window_buttons_widget = support.CreateButtonsWidget()
        self.window_body_layout.addWidget(self.window_buttons_widget)

        # Vertical Layout
        self.window_buttons_layout = QVBoxLayout(self.window_buttons_widget)
        self.window_buttons_layout.setContentsMargins(0, 0, 0, 0)

        # Info Widget
        self.window_information_widget = support.CreateInfoWidget()
        self.window_body_layout.addWidget(self.window_information_widget)

        # Info Layout
        self.window_information_layout = QHBoxLayout(self.window_information_widget)
        self.window_information_layout.setContentsMargins(0, 0, 0, 0)
        self.window_information_layout.setSpacing(0)


    # Settings: size, title, central widget
    def StandartWindowSettings(self, window: QMainWindow, size: tuple, title: str):
        window.resize(size[0], size[1])
        window.setWindowTitle(title)
        window.central = QWidget()
        window.central.setStyleSheet("""
        QWidget {
            background-color: #FFFFFF;
        }
        """)
        window.setCentralWidget(window.central)
        window.setMinimumWidth(1060)


    # Create test buttons on main screen
    def CreateMainTestButtons(self):

        self.button_all_accents = support.CreateMainButtonsDesign("Все ударения")
        self.button_all_spelling = support.CreateMainButtonsDesign("Вся орфография")
        self.button_hard_accents = support.CreateMainButtonsDesign("Сложные ударения")
        self.button_hard_spelling = support.CreateMainButtonsDesign("Сложная орфография")

    # Start dialog window about all accents
    def StartDialogAllAccents(self):
        Information, IsOkAnswer = QInputDialog.getText(self, 'Ударения', 'Введите количество слов: ')
        if IsOkAnswer:
            check = acsupport.Checker(Information, self.vector_numbers[0])
            if check:
                self.number_of_tests = int(Information)
                self.StartAccents('all')
            else:
                if acsupport.Else(self, IsOkAnswer, check, self.vector_numbers[0]):
                    self.StartAccents('all')


    # Start dialog window about hard accents
    def StartDialogHardAccents(self):
        Information, IsOkAnswer = QInputDialog.getText(self, 'Ударения', 'Введите количество слов: ')
        if IsOkAnswer:
            check = acsupport.Checker(Information, self.vector_numbers[1])
            if check:
                self.number_of_tests = int(Information)
                self.StartAccents('hard')
            else:
                if acsupport.Else(self, IsOkAnswer, check, self.vector_numbers[1]):
                    self.StartAccents('hard')


    # Layouts for testing for both options of test
    def TestLayoutSetup(self, title):

        # Widget Header
        self.window_header_widget = support.CreateHeaderWidget()
        self.window_main_layout.addWidget(self.window_header_widget, QtCore.Qt.AlignTop)

        # Layout Header
        self.window_header_layout = QHBoxLayout(self.window_header_widget)
        acsupport.CreateAccentsWindowHeader(self, "header1.png", title)

        # Label Widget
        self.window_label_widget = acsupport.CreateWindowLabelWidget()
        self.window_main_layout.addWidget(self.window_label_widget)

        # Label Layout
        self.window_label_layout = QHBoxLayout(self.window_label_widget)
        self.window_label_layout.setSpacing(0)

        # Word Widget
        self.window_word_widget = acsupport.CreateWindowWordWidget()
        self.window_main_layout.addWidget(self.window_word_widget)

        # Word Layout
        self.window_word_layout = QHBoxLayout(self.window_word_widget)
        self.window_word_layout.setSpacing(15)
        self.window_word_layout.setContentsMargins(0, 0, 0, 0)
        self.window_word_layout.setAlignment(QtCore.Qt.AlignHCenter)

        # Widget Bottom
        self.window_bottom_widget = acsupport.CreateWindowBottomWidget()
        self.window_main_layout.addWidget(self.window_bottom_widget)

        # Bottom layout
        self.window_bottom_layout = QHBoxLayout(self.window_bottom_widget)
        self.window_bottom_layout.setSpacing(0)

        # Layouts Vector
        self.vector_layouts = [self.window_label_layout, self.window_bottom_layout, self.window_word_layout]


    # Start dialog window about hard spellings
    def StartDialogHardSpellings(self):
        Information, IsOkAnswer = QInputDialog.getText(self, 'Орфография', 'Введите количество слов: ')
        if IsOkAnswer:
            check = acsupport.Checker(Information, self.vector_numbers[3])
            if check:
                self.number_of_tests = int(Information)
                self.StartSpellings('hard')
            else:
                if assupport.Else(self, IsOkAnswer, check, self.vector_numbers[3]):
                    self.StartSpellings('hard')


    # Function for button "return to main window"
    def button_return(self):
        self.number_of_tests = 0
        self.test_starting_time = 0
        self.MainDesign(self.window)



    def StartAccents(self, flag):

        # Clear Layout
        acsupport.DeleteAll(self)

        # SelfFlag
        self.flag = flag

        # Create new Layouts
        self.TestLayoutSetup("ТРЕНАЖЕР ПО УДАРЕНИЯМ")

        # Time
        self.test_starting_time = round(datetime.datetime.now().timestamp())

        # Words
        self.all_curent_words = list()
        for word in random.sample(accents_worker.get_words(flag), self.number_of_tests):
            w = AccentWord(word)
            self.all_curent_words.append(w)


        # Number (not index) word
        self.current_number_word = 1
        self.number_right_words = 0
        self.number_wrong_words = 0

        # Current word
        self.current_word = self.all_curent_words[self.current_number_word - 1]

        # Display
        self.DisplayWord()
        self.DisplayOther()

    def DisplayWord(self):
        self.word_pushbuttons_vector = acsupport.GetVectorPushButtons(self.current_word)

        for button in self.word_pushbuttons_vector:
            self.window_word_layout.addWidget(button)
            button.clicked.connect(self.ClickLetterButton)
            if button.text().upper() not in self.vowels:
                button.setEnabled(False)

    def DisplayOther(self):

        # Label Select
        self.select_label = acsupport.CreateLabelSelectWord()
        self.window_label_layout.addWidget(self.select_label)

        # Layout All, Wrongs and Rights
        self.InfoLabels()

        # Button add or button remove
        self.button_bottom = acsupport.ReturnButtonBottom(self.flag)
        self.window_bottom_layout.addWidget(self.button_bottom, alignment=QtCore.Qt.AlignLeft)
        self.button_bottom.clicked.connect(self.add_or_remove_word_accent)

        # Create Button Next
        self.button_next = acsupport.CreateButtonNext()
        self.button_next.setEnabled(False)
        self.button_next.clicked.connect(self.NextStep)
        self.window_bottom_layout.addWidget(self.button_next, alignment=QtCore.Qt.AlignRight)

    def add_or_remove_word_accent(self):
        self.button_bottom.setEnabled(False)
        if self.button_bottom.text() == 'Удалить слово':
            accents_worker.delete(self.current_word.word, 'hard')
        else:
            accents_worker.addition(self.current_word.word, 'hard')

    def NextStep(self):

        self.button_bottom.setEnabled(True)

        if self.current_number_word == len(self.all_curent_words) - 1:
            self.button_next.setText("Завершить")

        if self.current_number_word == len(self.all_curent_words):
            self.StartEnd()
        else:

            # Delete from word layout
            acsupport.DeleteWidgetFromLayout(self.window_word_layout)

            # Create new word
            self.current_number_word += 1
            self.current_word = self.all_curent_words[self.current_number_word - 1]
            self.DisplayWord()

            # Next button disabled
            self.button_next.setEnabled(False)


    # Update statistic on screen
    def UpdateStatisticWords(self):
        self.label_wrong_words.setText(f"Неправильных: {self.number_wrong_words}/{len(self.all_curent_words)}")
        self.label_right_words.setText(f"Правильных: {self.number_right_words}/{len(self.all_curent_words)}")
        self.label_all_words.setText(f"Всего пройдено: {self.current_number_word}/{len(self.all_curent_words)}")

    def right_answer(self, current):
        self.number_right_words += 1
        self.word_pushbuttons_vector[current].setStyleSheet("""
    QPushButton {{
        background-color: #41B72E;
        color: white;
        min-height: 55px;
        min-width: 55px;
        font-family: {};
        font-size: 40px;
        border-radius: 10px;
    }}
    
    QPushButton:hover {{
    }}
    
    QPushButton:disabled {{
        background-color: #41B72E;
        border-radius: 10px;
    }}
    
    QPushButton:pressed {{
        background-color: #41B72E;
    }}
    """.format(FONT_FAMILY))

    def wrong_answer(self, current, right):
        self.number_wrong_words += 1
        self.word_pushbuttons_vector[current].setStyleSheet("""
            QPushButton {{
                background-color: #C95733;
                color: white;
                min-height: 55px;
                min-width: 55px;
                font-family: {};
                font-size: 40px;
                border-radius: 10px;
            }}

            QPushButton:hover {{
            }}

            QPushButton:disabled {{
                background-color: #C95733;
                border-radius: 10px;
            }}

            QPushButton:pressed {{
                background-color: #C95733;
            }}
            """.format(FONT_FAMILY))
        self.word_pushbuttons_vector[right].setStyleSheet("""
            QPushButton {{
                background-color: #41B72E;
                color: white;
                min-height: 55px;
                min-width: 55px;
                font-family: {};
                font-size: 40px;
                border-radius: 10px;
            }}

            QPushButton:hover {{
            }}

            QPushButton:disabled {{
                background-color: #41B72E;
                border-radius: 10px;
            }}

            QPushButton:pressed {{
                background-color: #41B72E;
            }}
            """.format(FONT_FAMILY))


    # Block buttons from vector
    def BlockButtons(self, buttons: list):

        for button in buttons:
            button.setEnabled(False)


    def ProccesingAnswer(self, right_index: int, current_index: int):

        if right_index == current_index:
            self.right_answer(current_index)
        else:
            self.wrong_answer(current_index, right_index)


    def ClickLetterButton(self):

        right_index = self.current_word.index_stress
        sender_button = self.sender()
        current_index = self.word_pushbuttons_vector.index(sender_button)

        # Two ways: user answer right or wrong (select right index of buttons or not)
        self.ProccesingAnswer(right_index, current_index)

        # Update statistic on screen
        self.UpdateStatisticWords()

        # Do available "next" button
        self.button_next.setEnabled(True)

        # Block all buttons
        self.BlockButtons(self.word_pushbuttons_vector)

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            if self.label_text == 'ТРЕНАЖЕР ПО УДАРЕНИЯМ':
                if self.button_next.isEnabled():
                    self.NextStepAccents()
            else:
                if self.button_next.isEnabled():
                    self.NextStepSpelling()

    def InfoLabels(self):
        self.window_info_layout = QVBoxLayout()
        self.window_info_layout.setSpacing(0)
        self.window_info_layout.setContentsMargins(0, 0, 0, 0)
        self.window_label_layout.addLayout(self.window_info_layout)

        self.label_all_words = acsupport.CreateThreeButtons("#000000")
        self.label_all_words.setText(f"Всего пройдено: {self.current_number_word - 1}/{len(self.all_curent_words)}")

        self.label_right_words = acsupport.CreateThreeButtons("#76A552")
        self.label_right_words.setText(f"Правильных: {self.number_right_words}/{len(self.all_curent_words)}")

        self.label_wrong_words = acsupport.CreateThreeButtons("#9C3030")
        self.label_wrong_words.setText(f"Неправильных: {self.number_wrong_words}/{len(self.all_curent_words)}")

        self.statistic_labels = [self.label_all_words, self.label_right_words, self.label_wrong_words]

        for label in self.statistic_labels:
            self.window_info_layout.addWidget(label, QtCore.Qt.AlignRight)

    def EndLayoutsSetup(self):

        # Delete
        self.window_label_widget.deleteLater()
        self.window_word_widget.deleteLater()
        self.window_bottom_widget.deleteLater()

        # Create Result
        self.end_time = round(datetime.datetime.now().timestamp())
        if self.flag == 'all':
            self.statistic = stat.Statistic("Ударения (полностью)", self.test_starting_time,
                                            self.end_time, self.number_of_tests, self.number_right_words, self.number_wrong_words)
        else:
            self.statistic = stat.Statistic("Ударения (сложные)", self.test_starting_time,
                                            self.end_time, self.number_of_tests, self.number_right_words,
                                            self.number_wrong_words)


        # Widgets
        self.window_label_result_widget = endsupport.WidgetLabelResult()
        self.window_main_layout.addWidget(self.window_label_result_widget)

        self.window_label_percent_result_widget = endsupport.WidgetPercentsResult()
        self.window_main_layout.addWidget(self.window_label_percent_result_widget)

        self.window_three_labels_widget = endsupport.WidgetThreeLabelsResult(self)
        self.window_main_layout.addWidget(self.window_three_labels_widget)

        # Result
        self.label_result= endsupport.ResultLabel()
        self.label_result.setText("Ваш результат")

        self.label_percents = endsupport.PercentsLabel()
        self.label_percents.GiveText(self.statistic.PercentsResultTest())

        three_items = [endsupport.InformationLabelLeft(f"Время прохождения теста составило: {self.statistic.GetTimeTest()}"),
                       endsupport.InformationLabelLeft(f"Количество верных ответов составило: {str(self.statistic.items['rightCount'])}"),
                       endsupport.InformationLabelLeft("Больше информации")]

        self.window_label_percent_result_widget.layout.addWidget(self.label_percents)
        self.window_label_result_widget.layout.addWidget(self.label_result)
        self.window_three_labels_widget.CreateLayouts(three_items)

        # Commit result to json
        JsonWorking.WriteToJson(self.statistic.items)

    def StartEnd(self):

        # Layouts
        self.EndLayoutsSetup()

    def StartSpellings(self, flag):

        # Clear Layout
        acsupport.DeleteAll(self)

        # SelfFlag
        self.flag = flag

        # Create new Layouts
        self.TestLayoutSetup("ТРЕНАЖЕР ПО ОРФОГРАФИИ")

        # Time
        self.test_starting_time = round(datetime.datetime.now().timestamp())

        # Words
        self.all_curent_words = list()
        for word in random.sample(spelling_worker.get_words(flag), self.number_of_tests):
            w = SpellingWord(word)
            self.all_curent_words.append(w)

        # Number (not index) word
        self.current_number_word = 1
        self.number_right_words = 0
        self.number_wrong_words = 0

        # Current word
        self.current_word = self.all_curent_words[self.current_number_word - 1]

        # Display
        self.DisplayWordSpelling()
        self.DisplayOtherSpelling()



    def StartDialogAllSpellings(self):
        Information, IsOkAnswer = QInputDialog.getText(self, 'Орфография', 'Введите количество слов: ')
        if IsOkAnswer:
            check = acsupport.Checker(Information, self.vector_numbers[2])
            if check:
                self.number_of_tests = int(Information)
                self.StartSpellings('all')
            else:
                if assupport.Else(self, IsOkAnswer, check, self.vector_numbers[2]):
                    self.StartSpellings('all')


    def DisplayWordSpelling(self):

        self.word_pushbuttons_vector = assupport.GetWordVectors(self.current_word)

        for element in self.word_pushbuttons_vector:

            self.window_word_layout.addWidget(element)

            if element.text() == '':
                element.textChanged.connect(self.UnblockNext)

    def UnblockNext(self):
        self.button_next.setEnabled(True)

    def DisplayOtherSpelling(self):

        # Label Select
        self.select_label = acsupport.CreateLabelSelectWord()
        self.window_label_layout.addWidget(self.select_label)

        # Layout All, Wrongs and Rights
        self.InfoLabels()

        # Button add or button remove
        self.button_bottom = acsupport.ReturnButtonBottom(self.flag)
        self.window_bottom_layout.addWidget(self.button_bottom, alignment=QtCore.Qt.AlignLeft)
        self.button_bottom.clicked.connect(self.add_or_remove_word_spelling)

        # Create Button Next
        self.button_next = acsupport.CreateButtonNext()
        self.button_next.setEnabled(False)
        self.button_next.clicked.connect(self.NextStepSpelling())
        self.window_bottom_layout.addWidget(self.button_next, alignment=QtCore.Qt.AlignRight)

    def NextStepSpelling(self):

        self.button_bottom.setEnabled(True)

        if self.word_pushbuttons_vector[self.current_word.spell].text().upper() == self.current_word.word[self.current_word.spell]:
            self.word_pushbuttons_vector[self.current_word.spell].Right(self.current_word)
            self.number_right_words += 1
        else:
            self.word_pushbuttons_vector[self.current_word.spell].Wrong(self.current_word)
            self.number_wrong_words += 1

        self.UpdateStatisticWords()

        if self.current_number_word == len(self.all_curent_words) - 1:
            self.button_next.setText("Завершить")

        if self.current_number_word == len(self.all_curent_words):
            self.button_next.setEnabled(False)
            self.EndScreenSetupSpelling()
        else:

            # Delete from word layout
            acsupport.DeleteWidgetFromLayout(self.window_word_layout)

            # Create new word
            self.current_number_word += 1
            self.current_word = self.all_curent_words[self.current_number_word - 1]
            self.DisplayWordSpelling()

            # Next button disabled
            self.button_next.setEnabled(False)


    def add_or_remove_word_spelling(self):
        self.button_bottom.setEnabled(False)
        if self.button_bottom.text() == 'Удалить слово':
            spelling_worker.delete(self.current_word.word, 'hard')
        else:
            spelling_worker.addition(self.current_word.word, 'hard')

    # Generation result screen
    def EndScreenSetupSpelling(self):

        # Delete
        self.DeleteWidgets([self.window_label_widget, self.window_word_widget, self.window_bottom_widget])

        # Create end time for statistic
        self.end_time = round(datetime.datetime.now().timestamp())

        # Statistic
        self.WriteStatisticSpelling()

        # Widgets
        self.CreateEndScreenWidgets()

        # Result widgets
        self.CreateResultsWidgets()

        # Bottom widgets
        self.CreateEndBottomWidgets()



    def StartStatisticSetup(self):

        acsupport.DeleteAll(self)

        self.window.central.setStyleSheet('background-color:#313336;')

        self.window_main_layout.setAlignment(QtCore.Qt.AlignTop)

        # Header
        self.window_header_widget = support.CreateHeaderWidget()
        self.window_main_layout.addWidget(self.window_header_widget, QtCore.Qt.AlignTop)
        self.window_header_layout = QHBoxLayout(self.window_header_widget)
        support.CreateStatisticWindowHeader(self, "header1.png", "СТАТИСТИКА")

        # Buttons Widget
        self.window_buttons_widget = stsupport.ButtonsWidget()
        self.window_main_layout.addWidget(self.window_buttons_widget)


        # Vector Buttons
        self.widget_vector = stsupport.GetWidgetsVector(['Название', 'Процент', 'Время', 'Количество\nслов'])
        self.window_buttons_widget.layout.setSpacing(5)

        for widget_number in range(len(self.widget_vector)):
            if widget_number % 3 == 0:
                self.window_buttons_widget.layout.addStretch(20)
            self.window_buttons_widget.layout.addWidget(self.widget_vector[widget_number])

        self.widget_vector[1].clicked.connect(self.SortUpName)
        self.widget_vector[2].clicked.connect(self.SortDownName)
        self.widget_vector[4].clicked.connect(self.SortUpPercent)
        self.widget_vector[5].clicked.connect(self.SortDownPercent)
        self.widget_vector[7].clicked.connect(self.SortUpTime)
        self.widget_vector[8].clicked.connect(self.SortDownTime)
        self.widget_vector[10].clicked.connect(self.SortUpCount)
        self.widget_vector[11].clicked.connect(self.SortDownCount)

        # List
        self.window_list_widget = stsupport.ListWidget()
        self.window_main_layout.addWidget(self.window_list_widget)
        self.statistic_list = QListWidget()
        self.window_list_widget.layout.addWidget(self.statistic_list)

        # Get Data
        self.statistic_data = JsonWorking.ReadJson()['items']

        for element in self.statistic_data:
            new_item = StatisticWidget(element, self.statistic_data.index(element) + 1)
            list_widget_item = QListWidgetItem(self.statistic_list)
            list_widget_item.setSizeHint(new_item.sizeHint())
            new_item.setEnabled(False)
            self.statistic_list.addItem(list_widget_item)
            self.statistic_list.setItemWidget(list_widget_item, new_item)



    # Display statistic list
    def DisplayList(self):

        self.statistic_list.clear()

        for element in self.statistic_data:
            new_item = StatisticWidget(element, self.statistic_data.index(element) + 1)
            list_widget_item = QListWidgetItem(self.statistic_list)
            list_widget_item.setSizeHint(new_item.sizeHint())
            new_item.setEnabled(False)
            self.statistic_list.addItem(list_widget_item)
            self.statistic_list.setItemWidget(list_widget_item, new_item)


    def SortUpName(self):

        self.statistic_data = sorted(self.statistic_data, key=lambda x: x['name'])
        self.DisplayList()

    def SortDownName(self):

        self.statistic_data = sorted(self.statistic_data, key=lambda x: x['name'], reverse=True)
        self.DisplayList()

    def SortUpPercent(self):
        self.statistic_data = sorted(self.statistic_data, key=lambda x: x['rightCount'] / x['allCount'])
        self.DisplayList()

    def SortDownPercent(self):
        self.statistic_data = sorted(self.statistic_data, key=lambda x: x['rightCount'] / x['allCount'], reverse=True)
        self.DisplayList()

    def SortUpTime(self):
        self.statistic_data = sorted(self.statistic_data, key=lambda x: x['timeEnd'] - x['timeStart'])
        self.DisplayList()

    def SortDownTime(self):
        self.statistic_data = sorted(self.statistic_data, key=lambda x: x['timeEnd'] - x['timeStart'], reverse=True)
        self.DisplayList()

    def SortUpCount(self):
        self.statistic_data = sorted(self.statistic_data, key=lambda x: x['allCount'])
        self.DisplayList()

    def SortDownCount(self):
        self.statistic_data = sorted(self.statistic_data, key=lambda x: x['allCount'], reverse=True)
        self.DisplayList()


    # Write statistic for spelling
    def WriteStatisticSpelling(self):

        # Divide on "all" and "hard"
        if self.flag == 'all':
            self.statistic = stat.Statistic("Орфография (полностью)", self.test_starting_time,
                                            self.end_time, self.number_of_tests, self.number_right_words,
                                            self.number_wrong_words)
        else:
            self.statistic = stat.Statistic("Орфография (сложные)", self.test_starting_time,
                                            self.end_time, self.number_of_tests, self.number_right_words,
                                            self.number_wrong_words)

        # Commit result to json
        JsonWorking.WriteToJson(self.statistic.items)


    # Delete widgets
    def DeleteWidgets(self, widgets: list):

        for widget in widgets:
            widget.deleteLater()


    # Create End widgets for anyone way
    def CreateEndScreenWidgets(self):

        # Widgets
        self.window_label_result_widget = endsupport.WidgetLabelResult()
        self.window_main_layout.addWidget(self.window_label_result_widget)

        self.window_label_percent_result_widget = endsupport.WidgetPercentsResult()
        self.window_main_layout.addWidget(self.window_label_percent_result_widget)

        self.window_three_labels_widget = endsupport.WidgetThreeLabelsResult(self)
        self.window_main_layout.addWidget(self.window_three_labels_widget)


    # Bottom widgets
    def CreateEndBottomWidgets(self):

        three_items = [
            endsupport.InformationLabelLeft(f"Время прохождения теста составило: {self.statistic.GetTimeTest()}"),
            endsupport.InformationLabelLeft(
                f"Количество верных ответов составило: {str(self.statistic.items['rightCount'])}"),
            endsupport.InformationLabelLeft("Больше информации")]

        self.window_label_percent_result_widget.layout.addWidget(self.label_percents)
        self.window_label_result_widget.layout.addWidget(self.label_result)
        self.window_three_labels_widget.CreateLayouts(three_items)


    # Create result widgets: label result and label percents
    def CreateResultsWidgets(self):

        # Result
        self.label_result = endsupport.ResultLabel()
        self.label_result.setText("Ваш результат")

        self.label_percents = endsupport.PercentsLabel()
        self.label_percents.GiveText(self.statistic.PercentsResultTest())



