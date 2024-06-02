#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess as sp
import shlex

sp.call(shlex.split("streamlit run streamlit_demo.py"), shell=True)
