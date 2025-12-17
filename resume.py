from google import genai
import streamlit as st

st.title("Smart Resume Builder📄")
client = genai.Client(api_key="..................")

def resume(name,email,ph,location,education,skills,project):
   response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""You are an expert resume builder.

Create a professional resume using the following details:

Name: {name}
Email: {email}
Phone: {ph}
location:{location}
education:{education}
Skills: {skills}
project:{project}
do not give any extra line
Format it like a real resume with sections.
make attractive with columns and section 
At the end, add a short professional summary.
"""
        
    )
   return response
name=st.text_input("Enter your name:")
email=st.text_input("Enter your email address")
ph=st.text_input("Enter your phone number")
location=st.text_input("Enter your location")
education=st.text_input("Enter your education")
skills=st.text_area("add your skills")
project=st.text_area("add your project")
if st.button("Generate"):
    if not name or not ph or not location or not email or not skills or not education :
        st.warning("Please fill all required fields.")
    else:
        with st.spinner("Generating resume..."):
            result = resume(name, email, ph,location,education,skills,project)
            st.write(result.text)