## Introduction

<p align="justify">
Ollama has made it easy for us to run large language models locally on our personal computers. These local models are capable of answering
complex questions, analyzing and summarizing documents, generating and interpreting images, and more. Ollama provides developers a range of powerful
machine learning models to work with.
</p>

## About
<p align="justify"> Ollama Adventures is a GitHub repository that contains a collection of Jupyter Notebooks demonstrating the features and capabilities of Ollama's models. Ollama Adventures explores different avenues on how Ollama's Llama models are capable of answering questions, analyzing and summarizing PDF documents, interpreting images (Ollama's Llava model), and analyzing datasets. </p>

## Features

**Llama Models**
- **Question Answering:** Using Ollama's language models to answer various types of questions.
- **Document Summarization:** Analyzing and summarizing PDF files.
- **Dataset Analysis:** Using dataset input to answer queries and generate insights from data.

**Llava Models**
- **Image Interpretation:** Using Ollama's Llava model to interpret and generate responses from images.

## Setup for Local Environments

These notebooks were developed in Google Colab's Jupyter environment, but you can modify and run them locally with the following setup steps. Make sure your local environment meets the requirements below:

### Requirements

#### Hardware Requirements

- **RAM**:
    - 8 GB of RAM available to run 7B models.
    - 16 GB of RAM available to run 13B models.
    - 32 GB of RAM available to run 33B models.
    - More on this [here](https://github.com/ollama/ollama?tab=readme-ov-file#model-library).

- **GPU**:
    - **NVIDIA GPUs**: Supports GPUs with compute capability 5.0+ (More details [here](https://github.com/ollama/ollama/blob/main/docs/gpu.md#nvidia)).
    - **AMD Radeon GPUs**: Certain models are supported (Details [here](https://github.com/ollama/ollama/blob/main/docs/gpu.md#amd-radeon)).

- **Disk Space**: Ensure you have enough disk space to store Ollama's large language model files.

#### Software Requirements

- **Python**: Version 3.3 or greater.
- **Ollama**: Install Ollama from [here](https://ollama.com/download).
- **Jupyter**: Preferably installed using the Anaconda distribution.
- **Required Python Packages**: Install the necessary packages listed in `requirements.txt`.

### Setup Instructions

1. **Install Dependencies**:
    - Clone the repository:
      
      ```bash
      git clone https://github.com/dug22/Ollama-Adventures.git
      ```
    - Install required packages:
      
      ```bash
      pip install -r requirements.txt
      ```

2. **Set Up Ollama**:
    - Install Ollama on your machine [Ollama's Installation Link](https://ollama.com/download).

3. **Running the Notebooks**:
    - Once the dependencies are installed and Ollama is set up, navigate to the folder containing the Jupyter notebooks and run them in Jupyter or JupyterLab:
      
      ```bash
      jupyter notebook
      ```

4. **Modify Notebooks for Local Use**:
    - Adjust notebook paths and commands to point to local directories instead of Colab-specific paths.
    - Adjust code syntax oh how you install Ollama's models, and Python packages.
    - Modify any environment-specific settings to match your local setup.

## Usage

Once the environment is set up, you can open and run the provided notebooks. Each notebook demonstrates specific features, such as:

- **Question Answering**: Answering questions based on input text or data.
- **PDF Summarization**: Analyzing and summarizing the contents of PDF files.
- **Image Interpretation**: Using Ollama's Llava model to generate responses based on images.
- **Dataset Analysis**: Analyzing and interpreting datasets to answer queries.

For each notebook, there are detailed instructions and examples to help you understand how to use the models and the code provided.

## Contributing

If you'd like to contribute to this repository, feel free to open a pull request with your suggestions, bug fixes, or enhancements. Contributions are always welcome!

   

  
    
