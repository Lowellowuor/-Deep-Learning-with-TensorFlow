# MNIST Handwritten Digit Classification

## Overview
This project implements a Convolutional Neural Network (CNN) to classify handwritten digits from the MNIST dataset with >99% accuracy. The model uses modern deep learning techniques including BatchNorm and Dropout for robust performance.

## Requirements
- Python 3.7+
- TensorFlow 2.x
- NumPy, Matplotlib, Seaborn
- scikit-learn

## Setup
1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Run the notebook: `jupyter notebook mnist_cnn.ipynb`

## Results
- Test Accuracy: 99.2%
- Training Time: ~5 minutes on GPU
- Model Size: 1.2MB (.h5 format)

## Ethical Note
This model was trained on the standard MNIST dataset which may not represent all handwriting styles equally. For production use, additional testing with diverse samples is recommended.
