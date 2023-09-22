import gradio as gr
import numpy as np

def get_name(name):
    return 'Hello' + name


if __name__ == '__main__':
    # TUT - 1 : Text
    # demo = gr.Interface(fn=get_name, inputs='image', outputs='image')
    # demo.launch()

    #inputs : text, image, audio
    #outputs : text, image, audio

    # TUT - 2 : Textbox
    # demo  = gr.Interface(fn=get_name, 
    #                      inputs=gr.Textbox(lines=2, 
    #                     placeholder='Name here...'), outputs='text')
    # demo.launch()

    # TUT-3 : multiple input and output Components

    # def greet(name, is_morning, temperature):
    #     salutation = "Good morning" if is_morning else "Good evening"
    #     greeting = f"{salutation} {name}. It is {temperature} degrees today"
    #     celsius = (temperature - 32) * 5 / 9
    #     return greeting, round(celsius, 2)
    # demo = gr.Interface(fn=greet, inputs =['text', 'checkbox', gr.Slider(0,100)],
    #                     outputs = ['text', 'number'])
    # demo.launch()

    # TUT-4 : Images
    demo = gt.Interface(function_name, gr.Image(shape=(200,200)), "image")
    demo.launch()
    


