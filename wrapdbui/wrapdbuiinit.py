#!/usr/bin/env python3

#
# author : Michael Gene Brockus - (Dreamer)
# contact: <mailto:michaelbrockus@gmail.com>
# license: Mozilla Public License 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2024 The Fossil Logic development team
#
from PyQt5.QtWidgets import QApplication
from .models.appmodel import MainModel
from .view import main_activity
import logging


class WrapDBUiApplication(QApplication):
    def __init__(self, sys_argv):
        super(self.__class__, self).__init__(sys_argv)
        self._model = MainModel()

    def runner_start(self):
        logging.info(" Init WrapDB-UI Application runner")
        self.activity = main_activity.MainActivity(self._model)
        self.activity.show()
