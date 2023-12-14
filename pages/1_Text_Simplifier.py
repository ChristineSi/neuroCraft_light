import streamlit as st
from PIL import Image
import requests
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


################################################################################
# style aspects

# Increase the font size for all text elements
global_css = """
    body {
        font-size: 18px !important;
    }
"""

# Apply the global CSS using st.markdown with unsafe_allow_html=True
st.markdown(f'<style>{global_css}</style>', unsafe_allow_html=True)


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
# functions

#### MOCK FUNCTIONS FOR CLASSIFICATION AND SIMPLIFICATION - TO TEST, AS API WAS NOT YET READY ###

# mock function to simulate simplifying text
def mock_simplify(text):
    # simulating simplification while waiting for the actual API
    return "Mock Simplification"

####

# function to simplify text via API
def simplify(text):
    simplification_api_url = 'https://neurocraft-loe4rmocka-ew.a.run.app/simplified-text'
    api_key = st.secrets.api_key
    payload = {'text': text}
    headers = {
        'accept': 'application/json'
    }

    try:
        response = requests.post(simplification_api_url, params=payload, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            if isinstance(response_data, list) and len(response_data) > 0:
                simplified_text = response_data[0]  # Accessing the first element in the list
                simplified_text = simplified_text.strip('\"')  # Remove surrounding quotes
                simplified_text = simplified_text.replace("\\", "")  # Remove escape characters
                return simplified_text
            else:
                return "Simplified text not found in response"
        else:
            return f"Failed to simplify text. Status code: {response.status_code}"
    except requests.RequestException as e:
        st.error(f"Error simplifying text: {e}")
        return "Failed to simplify text"

def simplify_pdf(text):
    simplification_api_url = 'https://neurocraft-final-loe4rmocka-ew.a.run.app/pdf-simplification'
    api_key = st.secrets.api_key
    #payload = {'file': st.session_state.uploaded_file}
    headers = {
        'accept': 'application/json',
        'Content-Type': 'multipart/form-data'
    }
    payload = {
        'filename': st.session_state.uploaded_filename
    }

    try:
        response = requests.post(simplification_api_url, headers=headers, files={'file': st.session_state.uploaded_file}, params=payload)

        if response.status_code == 200:
            response_data = response.json()
            if isinstance(response_data, list) and len(response_data) > 0:
                simplified_text = response_data[0]  # Accessing the first element in the list
                simplified_text = simplified_text.strip('\"')  # Remove surrounding quotes
                simplified_text = simplified_text.replace("\\", "")  # Remove escape characters
                return simplified_text
            else:
                return "Simplified text not found in response"
        else:
            return f"Failed to simplify text. Status code: {response.status_code}"
    except requests.RequestException as e:
        st.error(f"Error simplifying text: {e}")
        return "Failed to simplify text"


# function to generate PDF from text
def generate_pdf(text):
    pdf_bytes = io.BytesIO()
    pdf = canvas.Canvas(pdf_bytes, pagesize=letter)

    text_object = pdf.beginText(100, 700)  # starting position
    text_object.setFont("Helvetica", 12)  # font and size

    lines = text.split('\n')  # split text by newline to handle paragraphs

    for line in lines:
        words = line.split(' ')
        line = ''
        for word in words:
            if pdf.stringWidth(line + word) < letter[0] - 200:  # width constraint
                line += word + ' '
            else:
                text_object.textLine(line)  # add line to the canvas
                line = word + ' '
        text_object.textLine(line)  # add the remaining line to the canvas

    pdf.drawText(text_object)
    pdf.save()

    pdf_stream = pdf_bytes.getvalue()
    return pdf_stream

# function to create a download link for the PDF file
def get_binary_file_downloader_html(bin_file, file_label, button_text):
    with io.BytesIO(bin_file) as f:
        btn = st.download_button(
            label=button_text,
            data=f,
            file_name=file_label,
            mime='application/pdf'
        )
    return btn



################################################################################
# main Streamlit app - simplifier
def main():
    icon = Image.open("./resources/icon.png")

    st.image(icon, width=100)

    st.markdown(
        '''
        # neuroCraft Project
        ***
        '''
    )

    if 'extracted_text' not in st.session_state:
        st.error("No text has been uploaded yet.")
    else:
        text = st.session_state.extracted_text
        filename = st.session_state.uploaded_filename
        st.write(f"Uploaded file: {filename}")
        st.write("***")
        if st.button("Simplify Text"):
            simplified_text = simplify(text)
            st.markdown('''
            ##### Simplified Text:
            ''')
            if simplified_text and simplified_text != "Simplified text not found in response":
                st.write(simplified_text)

                pdf_data = generate_pdf(simplified_text)
                st.markdown(get_binary_file_downloader_html(pdf_data, 'Simplified_Text.pdf', 'Download Simplified Text'), unsafe_allow_html=True)

            else:
                st.write("Simplified text not available or encountered an issue.")


    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '''
        ***
        This Webpage uses [OpenDyslexic Font](https://opendyslexic.org/)
        '''
    )

if __name__ == '__main__':
    main()
