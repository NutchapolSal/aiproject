import gradio as gr
from PIL import Image
from datetime import datetime
import numpy as np
import tensorflow as tf
from pathlib import Path

model = tf.keras.models.load_model('./assets/vgg-added-6types-kfold-1.keras')
class_names = ['gun', 'lizard', 'paper', 'rock', 'scissors', 'trident']

auths = [
    ('non', '-----'),
    ('save', '-----'),
    ('beem', '-----'),
    ('arm', '-----'),
    ('benz', '-----'),
    ('kiwi', '-----'),
    ('pond', '-----')
]

def predict_image(image: Image.Image) -> str:
    if image is None:
        return 'no image imput (make sure to press 🔴 on the webcam)'
    img_array = np.array(image)
    img_array = tf.image.resize(img_array, [224, 224])
    img_array = img_array  / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    print(predictions)
    predicted_class = np.argmax(predictions, axis=1)
    print(predicted_class)
    return class_names[predicted_class[0]]

def save_image(image, tag, username, model_guess, count):
    if tag == "none":
        return count, "..."
    if image is None:
        return count, "waiting"
    datestring = datetime.now().strftime("%Y-%m-%d %H.%M.%S.%f")
    image_path = Path("./assets/PublicMining") / tag / username / ("true" if tag == model_guess else "false") / f"{datestring}.jpeg"
    image_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(image_path)
    count += 1
    return count, f"Image count: {count}\nLatest image: {image_path}"

def generate_thumb(image):
    if image is None:
        return None
    thumb = image.copy()
    thumb.thumbnail((150,225))
    return thumb

def predict_and_save_image(image, tag, username, count):
    prediction = predict_image(image)
    count, output = save_image(image, tag, username, prediction, count)
    thumb = generate_thumb(image)
    return prediction, count, output, thumb
def print_images_count(count):
    print(f"Images count: {count}")
    return f"Images count: {count}"

def get_username_from_request(request: gr.Request):
    return request.username

with gr.Blocks() as demo:
    username_box = gr.Textbox("...", label="username", interactive=False)
    demo.load(get_username_from_request, outputs=username_box)
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", sources="webcam", streaming=True, height=400, width=600, mirror_webcam=False)
        with gr.Column():
            run_button = gr.Button(value="Capture")
            image_tag_as = gr.Radio(class_names+["none"],label="tag as",value="none")
            image_output_preview = gr.Image(type="pil", height=150, width=225, interactive=False)
            images_count = gr.State(0)
            text_output = gr.Textbox(f"...", label="output", interactive=False)
            estimation_output = gr.Textbox(f"...", label="model guesses:", interactive=False)

            # run_button.click(fn=save_image, inputs=[authorized, image_input, images_count], outputs=[images_count, text_output])
            run_button.click(fn=predict_and_save_image, inputs=[image_input, image_tag_as, username_box, images_count], outputs=[estimation_output, images_count, text_output, image_output_preview])

# demo.launch()
demo.launch(server_name="0.0.0.0", auth=auths)
