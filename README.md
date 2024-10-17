# ReLU AI Project

## setup Python environment

### first time
0. use WSL (for `tensorflow` GPU support)
0. run `python -m "venv" venv` to create virtual python environment
0. run `source venv/bin/activate` to activate venv
0. run `pip install -r requirements.txt`

### re-running
run `source venv/bin/activate` to activate venv

### `requirements.txt`
- main dependencies: `gradio`, `numpy`, `pillow`, `tensorflow`
- jupyter lab for running notebooks: `jupyterlab`
- for reading `hevc`/`heif` files: `pillow_heif`
- the rest: dependencies' dependencies

## Colab drive folder
[link](https://drive.google.com/drive/folders/1ryLoVFHR7yRBQK4mYo6ijerhv2acAAaR)

### models
name format: model`-`dataset`-kfold-`fold number`.keras`

#### model
- `vgg`: VGG19
- `effnet`: EfficientNetB0
- `custom`: custom architecture

#### dataset
- (none): models trained from existing-dataset
- `added`: models trained from added-dataset (before adding more hand types)
- `added-6types`: models trained from added-dataset (before PublicImageMining)
- `added-6types-pm1.1`: models trained from added-dataset
- `pick`: models trained from pick-dataset
- `pick-c`: models trained from pick-dataset (cropped preprocess version)

### pick-dataset
generated using `notebooks/dataset-picker.ipynb`

made by picking 20 random images of each folder from `added-dataset` 

### dataset preprocessor
- `notebooks/dataset-preprocessor.ipynb`: create folder with resized png images
- `notebooks/dataset-croppreprocessor.ipynb`: create folder with center-cropped resized png images (only used for `pick-c` model)

## PublicImageMining
gradio app to save images and try models

later used as API for game frontend

has authentication with randomly generated passwords (not committed to repo) to prevent random people using app

<sup>requires Secure context: `localhost`, or hosted on `https` except when used as API for Game Frontend
<br>[running as API for Game Frontend in WSL may require using `netsh interface portproxy`](https://stackoverflow.com/a/63781351/3623350)</sup>



### PublicImageMiningFrontend
[link](https://github.com/NutchapolSal/PublicImageMiningFrontend)

local webapp that connects to PublicImageMining, for better image capturing experience and to learn about `@gradio/client`

<sup>requires Secure context: `localhost`, or hosted on `https`</sup>

## Game Frontend
[link](https://github.com/Splazhy/rps-ai-project)

game frontend made with SolidStart

<sup>requires Secure context: `localhost`, or hosted on `https`</sup>

