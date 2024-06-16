#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This script is used to start the streamlit app.

import os
import subprocess as sp
import shlex
import sys

pwd = os.path.abspath(os.path.dirname(__file__))
bundle_dir = getattr(sys, "_MEI", pwd)
abs_path_app_file = os.path.abspath(os.path.join(bundle_dir, "src", "app.py"))
abs_path_app_file = abs_path_app_file.replace("\\", "\\\\")

sp.call(shlex.split("streamlit run " + abs_path_app_file), shell=True)
