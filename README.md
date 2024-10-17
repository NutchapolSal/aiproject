# ReLU AI Project

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

<sup>requires Secure context: `localhost`, or hosted on `https`</sup>

### PublicImageMiningFrontend
[link](https://github.com/NutchapolSal/PublicImageMiningFrontend)

local webapp that connects to PublicImageMining, for better image capturing experience and to learn about `@gradio/client`

<sup>requires Secure context: `localhost`, or hosted on `https`</sup>

## Game Frontend
[link](https://github.com/Splazhy/rps-ai-project)

game frontend made with SolidStart

<sup>requires Secure context: `localhost`, or hosted on `https`</sup>

