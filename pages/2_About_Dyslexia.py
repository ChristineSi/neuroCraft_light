import streamlit as st
from PIL import Image

################################################################################
# Style aspects

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
        ***
        '''
        )
    st.markdown('''
            ## About Dyslexia
            '''
            )
    girl = Image.open("./resources/girl.jpeg")
    st.image(girl, width=300, output_format='auto')


    st.markdown('''
            #### What is Dyslexia?
            '''
            )
    st.markdown('''
                Dyslexia is a learning disability that primarily affects language skills, especially reading, writing, and spelling.
                It can affect a person's academic success, but with appropriate teaching methods, people with dyslexia can learn successfully.
                '''
                )
    st.markdown('''
                #### What are the causes?
                '''
                )
    st.markdown('''
                Differences in the brain and difficulties in identifying speech sounds contribute to dyslexia.
                Dyslexia can affect people of all backgrounds and intelligence levels.
                '''
                )
    st.markdown('''
                #### How common is it?
                '''
                )
    st.markdown('''
                About 15-20\% of the population have symptoms. \n
                So 1 in 10 people you know will be affected!
                '''
                )
    st.markdown('''
                #### How does it show?
                Problems with word recognition, fluency, spelling, and writing are common. \n
                Dyslexia can lead to problems with spoken language and self-image, affecting academic and personal life.
                '''
                )
    st.markdown('''
                #### What can be done?
                ''')
    st.markdown('''
                Early identification is essential. A comprehensive assessment includes an assessment of language skills.
                With specialised teaching methods and accommodations, people with dyslexia can excel academically and emotionally.
                '''
                )


    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
                """
                ##### For more Resources and Help visit [British Dyslexia Association](https://www.bdadyslexia.org.uk/)
                """
                )

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
