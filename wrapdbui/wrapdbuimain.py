#!/usr/bin/env python3

#
# author : Michael Brockus.
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The WrapDB-UI development team
#
from .wrapdbuiinit import WrapDBUiApplication
from .wrapdbuilogs import wrapdbui_log
from .commandline import wrapdbui_cli
from PyQt5.QtGui import QIcon
import logging
import sys
import os


def wrapdbui_main():
    wrapdbui_log()
    wrapdbui_cli()

    logging.info(" Getting WrapDB-UI Application started")
    app: WrapDBUiApplication = WrapDBUiApplication(sys_argv=sys.argv)

    path = os.path.join(
        os.path.dirname(sys.modules[__name__].__file__),
        "..",
        "graphics",
        "wrapdb_app_ic.png",
    )
    app.setWindowIcon(QIcon(path))

    logging.info(" Running WrapDB-UI Application")
    app.runner_start()
    sys.exit(app.exec_())
