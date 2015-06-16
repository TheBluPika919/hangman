#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3

import sys

    
from PyQt5.uic import loadUiType

ui_Hangman,HangmanBaseClass = loadUiType('hangman.ui')

from PyQt5.QtCore import Qt

class Hangman(HangmanBaseClass, ui_Hangman):

    def __init__(self):
        super(Hangman, self).__init__()

        self.setupUi(self)


        self.word_to_guess = "cryptographic"
        self.guessed = "_"*len(self.word_to_guess)

        self.wordLabel.setText(self.guessed)

        self.setFocusPolicy(Qt.StrongFocus)

    def keyPressEvent(self, event):
        print("keyPressEvent: {}".format(event.text()))

        text = event.text().lower()

        if text:
            if text in self.word_to_guess:
                for i, c in enumerate(self.word_to_guess):
                    if c == text:
                        self.guessed = self.guessed[:i]+text+self.guessed[i+1:]

            self.wordLabel.setText(self.guessed)
            
        super(Hangman, self).keyPressEvent(event)


        

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    import sys
    app = QApplication(sys.argv)

    hangman = Hangman()
    hangman.show()

    app.exec()
