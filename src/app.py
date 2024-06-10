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

# Graphical USer Interface Library
from gui import GraphicUserInterface


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
DATE = "2024-06-01"

# Version String
VERSION_STRING = f"v{VERSION} ({DATE})"

# Footbar Text
FOOTBAR_TEXT = f"{APP_NAME} - {VERSION_STRING}"

# Application About Text
ABOUT_TEXT = "This is the Application about text."


###############################################################################
# Left Sidebar Panel Button Functions
###############################################################################

def sidebar_btn_device_info_press():
    '''GUI Left Sidebar Panel "Info" Button Press Handler.'''
    print("Showing Device Info Frame")


def sidebar_btn_flash_fw_press():
    '''GUI Left Sidebar Panel "Flash" Button Press Handler.'''
    print("Showing FW Flash Frame")


def sidebar_btn_debug_press():
    '''GUI Left Sidebar Panel "Debug" Button Press Handler.'''
    print("Showing Debug Frame")


def sidebar_btn_about_press():
    '''GUI Left Sidebar Panel "About" Button Press Handler.'''
    print("Showing About Frame")


###############################################################################
# Main Function
###############################################################################

def main(argc, argv) -> int:
    '''Application Run.'''
    logger.debug("Application Start")
    logger.debug("APP Number of Arguments: %d", argc)
    logger.debug("APP Arguments:")
    for arg in argv:
        logger.debug("  %s", str(arg))
    logger.debug("")
    gui = GraphicUserInterface()
    gui.setup_page(APP_NAME, "centered", ABOUT_TEXT, FOOTBAR_TEXT)
    gui.show_page_content()
    return 0


###############################################################################
# Runnable Main Script Detection
###############################################################################

if __name__ == "__main__":
    logger.debug("Application Launch")
    RETURN_CODE = main(len(sys_argv)-1, sys_argv[1:])
    logger.debug("Application Exit (%d)", RETURN_CODE)
    sys_exit(RETURN_CODE)
