import streamlitapp as st
from voicecommand import get_voice_command
from powerautomatesender import send_to_flow

st.title("🎙️ Voice-Controlled Power BI")

if st.button("Start Listening"):
    command = get_voice_command()
    st.write("You said:", command)
    send_to_flow(command)