import streamlit as st
import requests
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

#### MOCK FUNCTIONS FOR CLASSIFICATION AND SIMPLIFICATION - TO TEST, AS API WAS NOT YET READY ###

# mock function to simulate classifying text
def mock_classify(text):
    # simulating classification while waiting for the actual API
    return "Mock Classification"

####

# function to classify text via local API
def classify(text):
    classifier_api_url = 'https://neurocraft-loe4rmocka-ew.a.run.app/average-prediction'
    api_key = st.secrets.api_key

    payload = {'text': text}

    headers = {
        'accept': 'application/json'
    }

    try:
        response = requests.post(classifier_api_url, params=payload, headers=headers)

        if response.status_code == 200:
            result = response.text
            classification_mapping = {
                '0': "Hard to read.",
                '1': "Not so easy, but also not too hard to read.",
                '2': "Easy to read."
            }

            classification_result = classification_mapping.get(result, "Unknown")
            return classification_result

        else:
            return "Failed to classify text"

    except requests.RequestException as e:
        st.error(f"Error classifying text: {e}")
        return "Failed to classify text"

################################################################################

# main Streamlit app - classifier
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
        if st.button("Classify Text"):
            classification_result = classify(text)
            st.markdown('''
            ##### This Text is:
            ''')
            st.write(classification_result)

            st.write("---")
            st.write("Go to the **Text Simplifier** page if you want to simplify the uploaded text.")

    # check if the classification is not "easy" (can be implemented after the API is running)
    # if classification_result != 2:
    #    st.write("This text is classified as ...")
    #    st.write("Go to the Text Simplifier page to get a simplified version of your text.")

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
