import gradio as gr

def get_name_with_hello(name:str)-> str:
    return 'Hello ' + name + '! '

if __name__ == '__main__':
    demo = gr.Interface(fn=get_name_with_hello, inputs='text', outputs='text')
    demo.launch()

    # inputs = 'text', 'audio', 'image'
    # outputs = 'text', 'audio', 'image'
