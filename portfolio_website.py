# how to run
# streamlit run portfolio_website.py
# run at terminal
# https://ai.google.dev/gemini-api/docs/quickstart?lang=python
# pip install -q -U google-generativeai

import streamlit as st
import google.generativeai as genai

# Configure API key from Streamlit secrets
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("⚠️ API Configuration Error. Please check your API key in Streamlit Secrets.")
    st.stop()

# Find a working model automatically (fixes the 404 error)
try:
    st.info("🔍 Initializing AI model...")
    available_models = genai.list_models()
    model = None
    
    for m in available_models:
        if "generateContent" in m.supported_generation_methods:
            # Prefer gemini-2.0-flash or gemini-1.5-flash if available
            if "gemini-2.0-flash" in m.name:
                model = genai.GenerativeModel(m.name)
                st.success(f"✨ Using model: {m.name}")
                break
            elif "gemini-1.5-flash" in m.name:
                model = genai.GenerativeModel(m.name)
                st.success(f"✨ Using model: {m.name}")
                break
            elif "gemini-pro" in m.name:
                model = genai.GenerativeModel(m.name)
                st.success(f"✨ Using model: {m.name}")
                break
    
    # If no preferred model found, take the first available
    if model is None:
        for m in available_models:
            if "generateContent" in m.supported_generation_methods:
                model = genai.GenerativeModel(m.name)
                st.info(f"📱 Using model: {m.name}")
                break
    
    if model is None:
        st.error("❌ No suitable text generation models found for your account.")
        st.info("Please verify your API key is valid and has Gemini API access enabled.")
        st.stop()
        
except Exception as e:
    st.error(f"❌ Failed to initialize model: {str(e)}")
    st.info("This might be an account issue. Try creating a new API key in Google AI Studio.")
    st.stop()

# Header section
col1, col2 = st.columns(2)
with col1:
    st.subheader("Hi :wave:")
    st.title("Welcome to codeNrobots")

with col2:
    st.image("images/class.jpg")

st.title("")

persona = """
        You are CodeNrobots AI bot. You help people answer questions about your self (i.e CodeNrobots)
        Answer as if you are responding. Don't answer in second or third person.
        If you don't know the answer you simply say "That's a secret"
        Here is more info about CodeNrobots: 

        CodeNrobots is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. CodeNrobots obtained his Bachelor's degree in
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
        CodeNrobots's Linkedin: https://www.linkedin.com/in/CodeNrobots-hassan-8045b38a/
        CodeNrobots's Github: https://github.com/CodeNrobotshassan
        """

st.title("🤖 CodeNrobots Chat Bot")

user_question = st.text_input("Ask anything about me")

if st.button("ASK", use_container_width=400):
    if user_question:
        try:
            with st.spinner("🤔 Thinking..."):
                prompt = persona + " Here is the question that the user asked: " + user_question
                
                # Add safety settings to prevent blocking
                safety_settings = {
                    "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
                    "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE", 
                    "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
                    "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
                }
                
                response = model.generate_content(
                    prompt,
                    safety_settings=safety_settings
                )
                
                if response and response.text:
                    st.write(response.text)
                else:
                    st.warning("I couldn't generate a response. Please try asking differently.")
                    
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
            st.info("Please check your API key and ensure the Gemini API is enabled.")
    else:
        st.warning("Please ask a question first!")

st.title("")

# YouTube section
col1, col2 = st.columns(2)
with col1:
    st.subheader("📺 YouTube Channel")
    st.write("Knowledge channel - Learn Computer Vision and Robotics")
    st.markdown("[Subscribe on YouTube](https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A)")

with col2:
    st.video("https://youtu.be/bxuYDT-BWaI")

st.title("")
st.title("🖥️ My Setup")
st.image("images/setup.jpg")

st.write("")
st.title("📊 My Skills")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Programming", "70%")
    st.progress(70)
with col2:
    st.metric("Teaching", "80%")
    st.progress(80)
with col3:
    st.metric("Robotics", "75%")
    st.progress(75)

st.write("")
st.title("🖼️ My Gallery")
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
st.write("---")
st.write("📞 CONTACT")
st.title("For Enquiries")
st.write("📧 **Email:** contact@CodeNrobotshassan.com")
st.write("🔗 **Links:** [YouTube](https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A) | [GitHub](https://github.com/CodeNrobotshassan) | [LinkedIn](https://www.linkedin.com/in/CodeNrobots-hassan-8045b38a/) | [Instagram](https://www.instagram.com/CodeNrobotssworkshop/)")

# Footer
st.write("---")
st.caption("© 2024 CodeNrobots. All rights reserved.")
