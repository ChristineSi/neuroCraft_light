import streamlit as st
from PyPDF2 import PdfReader
from PIL import Image

################################################################################
# Style aspects

font_css = """
@font-face {
  font-family: 'OpenDyslexic';
  src: url('https://raw.githubusercontent.com/ChristineSi/neuroCraft_front-end/main/resources/OpenDyslexic-Regular.woff') format('woff'),
       url('https://raw.githubusercontent.com/ChristineSi/neuroCraft_front-end/main/resources/OpenDyslexic-Regular.otf') format('opentype');
}

/* Apply the font-family to elements */
body {
  font-family: 'OpenDyslexic', sans-serif;
  color: black;
  background-color: #EFDCA8; /* Set your background color here */
}

/* Change the color of horizontal lines (markdown '***' syntax) */
hr {
  border-color: black; /* Set the color of horizontal lines to black */
}

* {
  color: black;
}
"""

# Apply the font and other styles using st.markdown with unsafe_allow_html=True
st.markdown(f'<style>{font_css}</style>', unsafe_allow_html=True)

# change font to "OpenDyslexic" as defined in the "font.css" file
with open("./resources/font.css", "r") as file:
    css = file.read()

# link the CSS file using st.markdown
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# sidebar
st.markdown(
    """
    <style>
    .sidebar .css-1aumxhk {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

################################################################################
# Functions

# function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)
    # assuming only the first page of the PDF will be processed
    page = pdf_reader.pages[0]
    return page.extract_text()

################################################################################
# APP

# Main Streamlit app - Text upload
def main():
    icon = Image.open("./resources/icon.png")

    st.image(icon, width=100)

    st.markdown(
        '''
        # neuroCraft Project
        ***
        '''
        )
    st.markdown("<br>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Please upload a PDF file:", type="pdf")
    if uploaded_file:
        filename = uploaded_file.name
        text = extract_text_from_pdf(uploaded_file)
        st.session_state.extracted_text = text
        st.session_state.uploaded_filename = filename
        st.markdown('''
        ***
        ##### Extracted Text from PDF:
        ''')
        st.write(text)
        st.write("---")
        st.write("Go to the **Text Classifier** page to classify the uploaded text.")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
        '''
        This Webpage uses [OpenDyslexic Font](https://opendyslexic.org/)
        '''
        )

if __name__ == '__main__':
    main()
