import gradio as gr
import random

def random_response(message, history):
    return random.choice(['yes', 'no'])

if __name__ == '__main__':
    demo = gr.ChatInterface(random_response)
    demo.launch()