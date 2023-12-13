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

def main():
    icon = Image.open("./resources/icon.png")

    st.image(icon, width=100)

    st.markdown(
        '''
        # neuroCraft Project
        ***
        '''
        )
    st.markdown(
        '''
        ## Our Team
        '''
        )

    team_data = [
        {
            'name': 'Andrea Calcagni',
            'role': 'Data Scientist & ML Engineer - Focus on Text Classification',
            'description': 'Andrea is a Business professional in Italy, specializing in industrial machinery and printed electronics. He is now actively pursuing expertise in data science and AI to pivot towards the tech industry.',
            'image': '/Users/christine/code/ChristineSi/neuroCraft_front-end/resources/andrea.jpeg'
        },
        {
            'name': 'Pei-Yu Chen',
            'role': 'Data Scientist & ML Engineer - Focus on Large Language Models',
            'description': 'Pei is a multilingual marketer who is fascinated by data science. She is now transitioning from digital marketing to combine language affinity with data precision.',
            'image': '/Users/christine/code/ChristineSi/neuroCraft_front-end/resources/pei.jpeg'
        },
        {
            'name': 'Patricia Moreno Gaona',
            'role': 'Data Scientist & ML Engineer - Focus on Feature and Back-End Engineering',
            'description': 'Patricia is passionate about merging health and data for impactful solutions. She is a dedicated learner on a mission to revolutionize the tech and health industries.',
            'image': '/Users/christine/code/ChristineSi/neuroCraft_front-end/resources/patricia.jpeg'
        },
        {
            'name': 'Christine Sigrist',
            'role': 'Data Scientist, ML Engineer, & Project Leader - Focus on Transformers and Web Interface',
            'description': 'Christine is a mental health professional and researcher passionate about solving problems with data. She is eager to make the transition from academia to industry.',
            'image': '/Users/christine/code/ChristineSi/neuroCraft_front-end/resources/chris.jpeg'
        }
    ]


    for person in team_data:
        st.subheader(person['name'])
        st.image(person['image'], width=150)  # Adjust image width as needed
        st.write(f"**Role:** {person['role']}")
        st.write(f"**Bio:** {person['description']}")
        st.markdown('---')  # Add a horizontal line between team members

    st.markdown(
        '''
        This Webpage uses [OpenDyslexic Font](https://opendyslexic.org/)
        '''
        )

if __name__ == '__main__':
    main()
