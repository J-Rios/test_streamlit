
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Page Title",
    page_icon=None,
    layout="centered", # "centered" or "wide"
    menu_items={
        "Get help": None,
        "Report a Bug": None,
        "About": "This is the Application about text."
    }
)

# Hide Deploy Button
# Notice: At 01/06/2024, Streamlit doesn't provide an API function to
# disable/hide the Deploy button, so it is disabled by modifying the CSS
# style of that element (this approach could be invalid in the future)
st.markdown("<style>.stDeployButton {display:none;}</style>",
            unsafe_allow_html=True)

# Application Title
st.title("Streamlit Demo")

# Application Header
st.header("A variety of Streamlit elements")

st.markdown("---")

# Text Label: Standard
st.subheader("Standard Text")
st.write("This demo shows a variety of Streamlit elements in action.")

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

st.markdown("---")

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

st.markdown("---")

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

# Slider
st.subheader("Slider")
slider_val = st.slider("Select a value", 0, 100)
st.write(f"Slider value: {slider_val}")

st.markdown("---")
