import streamlit as st
from PIL import Image

################################################################################
# Style aspects

st.markdown(
    """
    <style>
    body {
        background-color: #EFDCA8; /* Your desired background color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# change font to "OpenDyslexic" as defined in the "font.css" file
with open("./resources/font.css", "r") as file:
    css = file.read()

# link the CSS file using st.markdown
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #black;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    "## This is the sidebar"

################################################################################
# APP

# main Streamlit app
def main():

    icon = Image.open("./resources/icon.png")

    st.image(icon, width=100)

    st.markdown(
        '''
        # neuroCraft Project
        ''',
        unsafe_allow_html=True
    )

    st.markdown('''***''')

    st.markdown('''
                #### Our Mission \n
                ##### We aim to make life easier for neurodivergent students, especially those with dyslexia.
                '''
                )
    st.markdown(
            '''
            ***
            #### Why care about Dyslexia?
            ''')
    st.markdown('''
        ##### Dyslexia is a learning difficulty that affects reading and writing.
        - In (higher) education, most information is presented as text.
        - Students with dyslexia are therefore facing significant challenges!
        ''')
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '''
        **Read more on the [About Dyslexia](http://localhost:8501/About_Dyslexia) page.**
        ***
        ''')

    st.markdown('''
            #### What we do
            ''')
    st.markdown('''
            ##### We make text more accessible to neurodivergent students.
            - Our app determines the readability level of a text that is uploaded. \n
            - If the text is too difficult for a dyslexic, the app simplifies it.
            ''')

    st.markdown("<br>", unsafe_allow_html=True)

    surfer = Image.open("./resources/surfer.jpeg")

    st.image(surfer, width=250)

    st.markdown(
        '''
        ##### Meet the neuroCraft [Team](http://localhost:8501/Team)
        '''
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('''
            ***
            This Webpage uses [OpenDyslexic Font](https://opendyslexic.org/)
            '''
            )


if __name__ == '__main__':
    main()
