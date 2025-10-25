import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.schema import SystemMessage, HumanMessage,AIMessage
from prompts import SYSTEM_PROMPT

# Load env
load_dotenv()
def get_llm():
    api_key = os.environ.get("GEMAI_API_KEY")
    if not api_key:
        raise ValueError("GEMAI_API_KEY not found.")
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)

def chat_with_gemini(history, prompt):
    llm = get_llm()
    history.append(SystemMessage(content=SYSTEM_PROMPT))
    # Convert frontend chat history into LangChain messages
    history.append(HumanMessage(content=prompt))
    message=history
    for i in message:
        if isinstance(i,HumanMessage):
            print(i)

    # Ask Gemini
    response = llm.invoke(message)
    history.append(AIMessage(content=response.content))
    return response.content

if __name__ == "__main__":
    print("Chatbot: Hi! Type something (or 'quit' to exit).")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        try:
            response = chat_with_gemini(user_input)
            print("Chatbot:", response)
        except Exception as e:
            print("Error:", e)








