import gradio as gr

def get_hello_with_name(name:str) -> str:
    return 'Hello ' + name + '! '

if __name__ == '__main__':
    demo = gr.Interface(fn=get_hello_with_name, inputs = gr.Textbox(lines=3), outputs= 'text', placeholder="Write your name")
    demo.launch()