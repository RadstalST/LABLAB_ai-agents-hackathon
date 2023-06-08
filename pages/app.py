import os
import streamlit as st
import pandas as pd
st.title("Dark search engine")
st.subheader("A search engine personal demography")
st.write("This is a search engine that uses GPT-3 to search for information about people. It is a personal demography search engine.")

linked_in_profile = st.text_input("Linked in profile url:",placeholder="https://www.linkedin.com/in/....")
facebook_profile = st.text_input("Facebook profile url:",placeholder="https://www.facebook.com/....")
twitter_profile = st.text_input("Twitter profile url:",placeholder="https://twitter.com/....")
instagram_profile = st.text_input("Instagram profile url:",placeholder="https://www.instagram.com/....")
youtube_profile = st.text_input("Youtube profile url:",placeholder="https://www.youtube.com/....")
st.header("interests based on social media profiles")
st.markdown('''
1. Main interest:
John Doe's main interest lies in the field of Artificial Intelligence (AI) and its related disciplines. He is particularly interested in Machine Learning, Deep Learning, Data Science, Robotics, Computer Vision, Natural Language Processing, and Technology Ethics. These areas of interest reflect his passion for advanced technologies and their potential applications.

2. Personality:
John Doe appears to be intellectually curious and driven. His active involvement in various AI projects and research indicates a strong motivation to explore and contribute to cutting-edge technologies. He is likely a detail-oriented individual who enjoys delving into complex problems and finding innovative solutions. Moreover, his interest in technology ethics suggests a conscientious and ethical mindset, indicating a desire to consider the broader implications and societal impact of technological advancements.

3. Career journey:
John Doe's career journey has revolved around his passion for AI and technology. He started as a software engineer, likely acquiring foundational skills and knowledge in software development. As his interest in AI grew, he delved deeper into Machine Learning, Deep Learning, and other AI-related disciplines. This progression likely involved continuous learning, either through self-study or formal education, to acquire the necessary expertise.

His involvement in AI projects and research demonstrates practical application of his skills and knowledge. It is possible that he has worked on AI-related projects in various industries, leveraging AI techniques to solve complex problems and optimize processes. He may have also collaborated with other professionals, contributing to the advancement of AI technologies.

Overall, John Doe's journey showcases a focused and dedicated approach to his career, centered around his passion for AI.
''')
st.header("interests based on social media profiles")
# add a table of interests
interests_df = pd.DataFrame({
    "interest":["interest1","interest2","interest3"],
    "description":["description1","description2","description3"],
    "found on":["facebook","twitter","instagram"],
    "score":[0.9,0.8,0.7]})
st.table(interests_df)

involvement_df = pd.DataFrame({
  "involvement": [
    "He actively participates in projects and research related to Artificial Intelligence.",
    "He actively engages in projects and research related to Machine Learning.",
    "He actively contributes to projects and research in the field of Deep Learning.",
    "He actively involves himself in projects and research related to Data Science.",
    "He actively participates in projects and research related to Robotics.",
    "He actively engages in projects and research related to Computer Vision.",
    "He actively contributes to projects and research in the field of Natural Language Processing.",
    "He has a passive involvement in the field of Education, which means he may have an interest in it but does not actively participate or contribute.",
    "He has a passive involvement in the field of Entrepreneurship, which means he may have an interest in it but does not actively participate or contribute.",
    "He has a passive involvement in the field of Technology Ethics, which means he may have an interest in it but does not actively participate or contribute."
  ],
  "interest": [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Robotics",
    "Computer Vision",
    "Natural Language Processing",
    "Education",
    "Entrepreneurship",
    "Technology Ethics"
  ]
}).set_index("interest")

st.table(involvement_df)
# multiinput base on interests
st.header("Which of these interests are you interested in?")
interests = st.multiselect("Interests",interests_df["interest"].tolist())
for interest in interests:

    st.subheader(interest)
    st.write("summary of interest based on internet search")
    st.write("sasfasfasfasfasfasfa")
    st.write("person involvement in the interest")
    st.write("involvement")

st.divider()
st.header("With all the these information, what would you like to do?")
prompt = st.text_area(
    "prompt",
    placeholder="write a cover letter for a job application that was addressed to this person",
    )
extra_context = st.text_area(
    "additional context",
    placeholder="your resume and job posting",
    )


