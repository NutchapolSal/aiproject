import gradio as gr
from PIL import Image
import numpy as np
import tensorflow as tf
import random


model = tf.keras.models.load_model('C:\\Users\\ADMIN\\Desktop\\TestAi\\model1.keras')


def predict_image(image: Image.Image) -> str:
    img_array = np.array(image)
    img_array = tf.image.resize(img_array, [224, 224])  
    img_array = img_array  / 255.0  
    img_array = np.expand_dims(img_array, axis=0)  

    predictions = model.predict(img_array)
    print(predictions)
    predicted_class = np.argmax(predictions, axis=1)
    print(predicted_class)
    class_names = ['paper', 'scissors', 'rock'] 
    return class_names[predicted_class[0]]


def generate_random_result():
    return random.choice(['paper', 'scissors', 'rock'])  


def calculate_winner(predicted_class, random_class):
    if predicted_class == random_class:
        return f"It's a tie! Both are {predicted_class}"
    else:
        return f"You: {predicted_class}, Random: {random_class}. {random.choice([f"You win!", f"Random wins!"])}"


def main_function(image):
    predicted_class = predict_image(image)
    random_class = generate_random_result()
    result = calculate_winner(predicted_class, random_class)
    return predicted_class, random_class, result


with gr.Blocks() as app:
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil")  
            predict_button = gr.Button("Play")
        with gr.Column():  
            predicted_output = gr.Textbox(label="Your Prediction")
            random_output = gr.Textbox(label="Random Prediction")
            result_output = gr.Textbox(label="Result")

            predict_button.click(
                fn=main_function,
                inputs=image_input,
                outputs=[predicted_output, random_output, result_output]
            )


app.launch()
