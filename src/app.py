#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script:
    app.py
Description:
    Streamlit Application demo test.
Author:
    Jose Miguel Rios Rubio
Date:
    2024-06-10
Version:
    1.0.0
'''

###############################################################################
# Standard Libraries
###############################################################################

# Logging Library
import logging

# System Library
from sys import argv as sys_argv
from sys import exit as sys_exit


###############################################################################
# Local Libraries
###############################################################################

# User Interface Library
from ui import UserInterface


###############################################################################
# Logger Setup
###############################################################################

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


###############################################################################
# Constants & Configurations
###############################################################################

# Application Name
APP_NAME = "Streamlit Demo"

# Software Version
VERSION = "1.0.0"

# Software Version Date
DATE = "2024-06-11"

# Version String
VERSION_STRING = f"v{VERSION} ({DATE})"

# Footbar Text
FOOTBAR_TEXT = f"{APP_NAME} - {VERSION_STRING}"

# Application About Text
ABOUT_TEXT = "This is the Application about text."


###############################################################################
# Global Elements
###############################################################################

# User Interface
ui = UserInterface()


###############################################################################
# Left Sidebar Panel Button Functions
###############################################################################

def sidebar_btn_0_press():
    '''UI Left Sidebar Panel Button_0 Press Handler.'''
    print("Pressed Sidebar Button 0")


def sidebar_btn_1_press():
    '''UI Left Sidebar Panel Button_1 Press Handler.'''
    print("Pressed Sidebar Button 1")


def sidebar_btn_2_press():
    '''UI Left Sidebar Panel Button_2 Press Handler.'''
    print("Pressed Sidebar Button 2")


def sidebar_btn_3_press():
    '''UI Left Sidebar Panel Button_3 Press Handler.'''
    print("Pressed Sidebar Button 3")


def btn_clickme_press():
    '''UI Click-Me Button Pressed.'''
    print("Button Click-Me Pressed")


###############################################################################
# Main Function
###############################################################################

def main(argc, argv) -> int:
    '''Application Run.'''
    # Handle Application arguments
    logger.debug("Application Start")
    logger.debug("APP Number of Arguments: %d", argc)
    logger.debug("APP Arguments:")
    for arg in argv:
        logger.debug("  %s", str(arg))
    logger.debug("")
    # Create UI and bind function callbacks
    ui.callbacks.sidebar_btn_0.app = sidebar_btn_0_press
    ui.callbacks.sidebar_btn_1.app = sidebar_btn_1_press
    ui.callbacks.sidebar_btn_2.app = sidebar_btn_2_press
    ui.callbacks.sidebar_btn_3.app = sidebar_btn_3_press
    ui.callbacks.btn_clickme.app = btn_clickme_press
    # Generate and show UI
    ui.setup_page(APP_NAME, "centered", ABOUT_TEXT, FOOTBAR_TEXT)
    return 0


###############################################################################
# Runnable Main Script Detection
###############################################################################

if __name__ == "__main__":
    logger.debug("Application Launch")
    RETURN_CODE = main(len(sys_argv)-1, sys_argv[1:])
    logger.debug("Application Exit (%d)", RETURN_CODE)
    sys_exit(RETURN_CODE)
