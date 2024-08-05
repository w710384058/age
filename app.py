import streamlit as st
from langchain.memory import ConversationBufferMemory

from wenxin import get_chat_response

st.title("💬 暴躁GPT")

st.write("雖然我脾氣比較暴，經常陰陽怪氣你們這些愚蠢的人類。")



if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "少來煩我!!!!"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:

    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("在想了，你最好别催我...."):
        response = get_chat_response(prompt, st.session_state["memory"],
                                     )
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)