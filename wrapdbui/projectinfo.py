#!/usr/bin/env python3

#
# author : Michael Gene Brockus - (Dreamer)
# contact: <mailto:michaelbrockus@gmail.com>
# license: Mozilla Public License 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2024 The Fossil Logic development team
#


info = """\
WrapDB-UI is an open source package GUI meant to be both extremely fast,
and, even more importantly, as user friendly as possible.

The main design point of WrapDB-UI is to provide a standalone portable
GUI for managing wrap files and allow the user to create new packages
easily without having to play wheres Woldo.
"""


class ProjectInfo:
    def get_description(self) -> str:
        return info

    def get_version(self) -> str:
        return "0.1.0"

    def get_license(self) -> str:
        return "Apache-2.0"

    def get_project_name(self) -> str:
        return "wrapdb-ui"

    def get_packages(self) -> list:
        return [
            "wrapdbui",
            "wrapdbui.containers",
            "wrapdbui.dashboard",
            "wrapdbui.wrapdbuilib",
            "wrapdbui.repository",
            "wrapdbui.models",
            "wrapdbui.view",
            "wrapdbui.ui",
            "wrapdbui.wrapdbuilib.appconfig",
            "wrapdbui.wrapdbuilib.backends",
            "wrapdbui.wrapdbuilib.ninjabuild",
            "wrapdbui.wrapdbuilib.wrapdbbuild",
            "wrapdbui.wrapdbuilib.wrapdbapi",
        ]
