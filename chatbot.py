import openai
import gradio as gr
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{"role": "system", "content": "You are a customizable personal AI chatbot"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gr.Interface(
    fn=CustomChatGPT,
    inputs=gr.Textbox(lines=2, placeholder="Enter your message here...", label="Input"),
    outputs=gr.Textbox(lines=4, label="Output"),
    title="Morphia",
    theme="default",  # You can change this to "dark", "glass", or create a custom theme.
    live=False,  # Disable live updates
    css="""
    .panel-title {
        font-family: 'Courier New', Courier, monospace;
        font-size: 24px;
        color: #333;
    }
    #user_input {
        background-color: #f0f0f0;
        border-radius: 10px;
    }
    #output {
        background-color: #e0e0e0;
        border-radius: 10px;
    }
    .btn-primary {
        background-color: #ff5722;
        border-color: #ff5722;
    }
    """
)

demo.launch(share=True)
