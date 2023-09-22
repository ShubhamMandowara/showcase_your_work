import gradio as gr

def return_hello_with_name(name:str) -> str:
    return 'Hello ' + name


if __name__ == '__main__':
    with gr.Blocks() as demo:
        name = gr.Textbox(label='Name')
        output = gr.Textbox(label='Output')
        gr_button = gr.Button('Cool!')
        gr_button.click(fn=return_hello_with_name, inputs=name, outputs=output, api_name='block_try')
        
    demo.launch()
