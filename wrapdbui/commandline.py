#!/usr/bin/env python3

#
# author : Michael Gene Brockus - (Dreamer)
# contact: <mailto:michaelbrockus@gmail.com>
# license: Mozilla Public License 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2024 The Fossil Logic development team
#
from .projectinfo import ProjectInfo
import argparse


def wrapdbui_cli() -> argparse:
    data: ProjectInfo = ProjectInfo()

    parser: argparse = argparse.ArgumentParser(description="WrapDB-ui GUI.")

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=data.get_version(),
        help="print version number",
    )

    parser.parse_args()
