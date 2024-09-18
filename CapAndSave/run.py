import gradio as gr
from PIL import Image
from datetime import datetime

def save_image(run, image, count):
    if not run:
        return count, "..."
    datestring = datetime.now().strftime("%Y-%m-%d %H.%M.%S.%f")
    image_path = f"./assets/hands/{datestring}.png"
    image.save(image_path)
    count += 1
    return count, f"Image count: {count}\nLatest image: {image_path}"

def print_images_count(count):
    print(f"Images count: {count}")
    return f"Images count: {count}"

with gr.Blocks() as app:
    ticker = gr.Timer(value=0.1, active=True)
    with gr.Column():
        image_input = gr.Image(type="pil", sources="webcam", streaming=True)
        run_checkbox = gr.Checkbox(label="Run", every=1)
        images_count = gr.State(0)
        text_output = gr.Textbox(f"...")

        ticker.tick(fn=save_image, inputs=[run_checkbox, image_input, images_count], outputs=[images_count, text_output])

# app.launch()
app.launch(server_name="0.0.0.0")
