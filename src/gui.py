#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script:
    gui.py
Description:
    Streamlit Graphical USer Interface.
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

# None


###############################################################################
# Third-Party Libraries
###############################################################################

# StreamLit
import streamlit as st


###############################################################################
# Project Local Libraries
###############################################################################

# None


###############################################################################
# Auxiliary Classes
###############################################################################

class Button():
    '''Button UI element class.'''
    def __init__(self, uid, label, callback):
        self.uid = uid
        self.label = label
        self.callback = callback


###############################################################################
# GUI Class
###############################################################################

class GraphicUserInterface():
    '''
    Graphical User Interface Class that defines all the visual elements
    of an Application.
    '''

    def __init__(self):
        '''GraphicUserInterface Constructor.'''
        self.gui_objects = []
        self.window = None
        self.window_width = 0
        self.window_height = 0
        self.left_sidebar = None
        self.up_headbar = None
        self.btn_id = 0
        self.cb_buttons = {}
        self.footbar_text = ""

    def set_button(self, label, callback):
        '''Set a button on the left sidebar menu.'''
        btn = Button(self.btn_id, label, callback)
        self.btn_id = self.btn_id + 1
        self.cb_buttons[btn.uid] = btn

    def setup_page(self, title, layout, about, footbar_text, icon=None):
        '''
        Setup Streamlit Web Page Configuration and General Stuffs.
        Layout: "centered" or "wide".
        '''
        # Page Configuration
        st.set_page_config(page_title=title, page_icon=icon, layout=layout,
            menu_items={"Get help": None, "Report a Bug": None, "About": about}
        )
        # Hide Deploy Button
        # Notice: At 01/06/2024, Streamlit doesn't provide an API function
        # to hide the Deploy button, so it's done by modifying the CSS style
        # of that element (this approach could be invalid in the future)
        st.markdown("<style>.stDeployButton {display:none;}</style>",
                    unsafe_allow_html=True)
        # Application Title, SideBar, Footer & Header
        st.title(title)
        self.setup_sidebar()
        self.setup_footer(footbar_text)

    def setup_header(self, text=""):
        '''Setup Page Header.'''
        st.header(text)
        st.markdown("---")

    def setup_footer(self, foot_text):
        '''Setup Page Footer.'''
        footer = """
        <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #1D6AB8;
                color: white;
                z-index: 1000;
                padding-right: 20px;
                height: 30px;
                text-align: right;
            }
        </style>
        """
        footer = f"{footer}<div class='footer'><p>{foot_text}</p></div>"
        st.markdown(footer, unsafe_allow_html=True)

    def setup_sidebar(self):
        '''Setup SideBar Menu.'''
        # Sidebar Title
        st.sidebar.title("Menu")
        st.sidebar.markdown("---")
        # Setup Buttons
        self.set_button("Texts", self.show_content_text)
        self.set_button("Inputs & Outputs", self.show_content_io)
        self.set_button("Selectors", self.show_content_selector)
        self.set_button("Others", self.show_content_other)
        # Draw Buttons
        if "menu_option" not in st.session_state:
            st.session_state.menu_option = 0
        for i in range(len(self.cb_buttons)):
            btn = self.cb_buttons[i]
            if st.sidebar.button(btn.label):
                st.session_state.menu_option = btn.uid
                #btn.callback()

    def show_page_content(self):
        '''Show Content based on Sidebar Menu Option selected.'''
        self.cb_buttons[st.session_state.menu_option].callback()

    def show_content_text(self):
        '''Show Page Content: Text.'''
        self.setup_header("A variety of Streamlit Elements")
        # Text Label: Standard
        st.subheader("Standard Text")
        st.write("This demo shows a some Streamlit elements in action.")
        st.markdown("---")
        # Text Label: Markdown
        st.subheader("Markdown Text")
        st.markdown("This is an *example* of **markdown** text.")
        st.markdown("---")
        # Text Label: Code
        st.subheader("Code Text")
        st.code("print('Hello, World!')")
        st.markdown("---")
        # Text Label: LaTeX
        st.subheader("LaTeX")
        st.latex(r'''a + ar + ar^2 + ar^3 + \cdots + ar^n''')

    def show_content_io(self):
        '''Show Page Content: Inputs / Outputs.'''
        self.setup_header("Inputs / Outputs Elements")
        # Text Input
        st.subheader("Text Input")
        name = st.text_input("Enter your name:")
        if name:
            st.write(f"Hello, {name}!")
        st.markdown("---")
        # Button
        st.subheader("Button")
        if st.button("Click me"):
            st.write("Button clicked!")
        st.markdown("---")
        # Checkbox
        st.subheader("CheckBox")
        checkvalue = st.checkbox("Show/Hide")
        if checkvalue:
            checkvalue = "checked"
        else:
            checkvalue = "not-checked"
        st.write(f"Checkbox: {checkvalue}")

    def show_content_selector(self):
        '''Show Page Content: Selector.'''
        self.setup_header("Selectors Elements")
        # SelectBox
        st.subheader("SelectBox")
        option1 = st.selectbox("Select Option",
                            ["Option 1", "Option 2", "Option 3"])
        st.write(f"Selected options: {option1}")
        st.markdown("---")
        # SelectSlide
        st.subheader("SelectSlide")
        option2 = st.select_slider("Select Slider Option",
                                ["Option 1", "Option 2", "Option 3"])
        st.write(f"Selected options: {option2}")
        st.markdown("---")
        # SelectMultiple
        st.subheader("SelectMultiple")
        options = st.multiselect("Select Multiple Options",
                                ["Option 1", "Option 2", "Option 3"])
        st.write(f"Selected options: {options}")
        st.markdown("---")

    def show_content_other(self):
        '''Show Page Content: Others.'''
        self.setup_header("Other Elements")
        # Slider
        st.subheader("Slider")
        slider_val = st.slider("Select a value", 0, 100)
        st.write(f"Slider value: {slider_val}")
