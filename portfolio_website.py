# how to run
# streamlit run portfolio_website.py
# run at terminal
# https://ai.google.dev/gemini-api/docs/quickstart?lang=python
# pip install -q -U google-generativeai
import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key="api_key")

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)
with col1:
    st.subheader("Hi:wave:")
    st.title("Welcome to codeNrobots")

with col2:
    st.image("images/class.jpg")

st.title("")
persona = """
        You are CodeNrobots AI bot. You help people answer questions about your self (i.e CodeNrobots)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about CodeNrobots: 

        CodeNrobots is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. CodeNrobots obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
        Bristol University (UK). He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        CodeNrobots worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.

        CodeNrobots's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        CodeNrobots's Email: contact@CodeNrobotshassan.com 
        CodeNrobots's Facebook: https://www.facebook.com/CodeNrobotssworkshop
        CodeNrobots's Instagram: https://www.instagram.com/CodeNrobotssworkshop/
        CodeNrobots's Linkdin: https://www.linkedin.com/in/CodeNrobots-hassan-8045b38a/
        CodeNrobots's Github :https://github.com/CodeNrobotshassan
        """


st.title("codeNrobots chat bot")


user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona +"Here is the question that the user asked: " +  user_question
    response = model.generate_content(prompt)
    st.write(response.text)



st.title("")





col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube channel")
    st.write("Knowedge channel")

with col2:
    st.video("https://youtu.be/bxuYDT-BWaI")

st.title("")
st.title("My setup")
st.image("images/setup.jpg")
st.write("")
st.title("My skills")
st.slider("Programming",0,100,70)
st.slider("Teaching",0,100,80)
st.slider("Robotics",0,100,75)

st.write("")
st.title("My Gallery")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")
with col2:
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")
with col3:
    st.image("images/g7.jpg")
    st.image("images/g8.jpg")
    st.image("images/g9.jpg")

st.write("")
st.write("CONTACT")
st.title("For enquires")
st.write("email")

















