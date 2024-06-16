#!/usr/bin/env python3

#
# author : Michael Brockus.
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2024 Fossil Logic
#
from wrapdbui.wrapdbuimain import wrapdbui_main
from pathlib import Path
import sys


# If we run uninstalled, add the script directory to sys.path to ensure that
# we always import the correct wrapdbui modules even if PYTHON_PATH is mangled
wrapdbui_exe = Path(sys.argv[0]).resolve()
if (wrapdbui_exe.parent / "wrapdbui").is_dir():
    sys.path.insert(0, str(wrapdbui_exe.parent))


if __name__ == "__main__":
    sys.exit(wrapdbui_main())
