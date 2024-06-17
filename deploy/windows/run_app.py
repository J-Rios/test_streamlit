#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This script is used to start the streamlit app.

# Use this approach for a fully builtin streamlit in the Binary

from os import path as os_path
import sys

from streamlit.web import cli as st_cli

pwd = os_path.abspath(os_path.dirname(__file__))
bundle_dir = getattr(sys, "_MEI", pwd)
abs_path_app_file = os_path.abspath(os_path.join(bundle_dir, "src", "app.py"))
abs_path_app_file = abs_path_app_file.replace("\\", "\\\\")

sys.exit(st_cli.main_run([abs_path_app_file]))

###############################################################################

# Use this Second Approach if you don't want to add Streamlit to the Binary

#import os
#import subprocess as sp
#import shlex
#import sys
#
#pwd = os.path.abspath(os.path.dirname(__file__))
#bundle_dir = getattr(sys, "_MEI", pwd)
#abs_path_app_file = os.path.abspath(os.path.join(bundle_dir, "src", "app.py"))
#abs_path_app_file = abs_path_app_file.replace("\\", "\\\\")
#
#sp.call(shlex.split("streamlit run " + abs_path_app_file), shell=True)
