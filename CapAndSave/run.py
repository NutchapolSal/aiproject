import gradio as gr
from PIL import Image
from datetime import datetime

def save_image(run, image, count):
    if not run:
        return count
    datestring = datetime.now().strftime("%Y-%m-%d %H.%M.%S.%f")
    image.save(f"./assets/hands/{datestring}.png")
    count += 1
    return count

def print_images_count(count):
    print(f"Images count: {count}")
    return f"Images count: {count}"

with gr.Blocks() as app:
    ticker = gr.Timer(value=1, active=True)
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", sources="webcam", streaming=True)
            predict_button = gr.Checkbox(label="Run", every=1)
        with gr.Column():  
            images_count = gr.State(0)
            text_output = gr.Textbox(f"...")

            ticker.tick(fn=save_image, inputs=[predict_button, image_input, images_count], outputs=images_count)

            images_count.change(fn=print_images_count, inputs=images_count, outputs=text_output)


# app.launch()
app.launch(server_name="0.0.0.0")
