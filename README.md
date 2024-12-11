## Introduction

<p align="justify">
Ollama has really made it easy for us to run large language models locally on our personal computer. These local models are capable of answering
complex questions, analyzing and summarizing documents, generating and interpreting images, and more. Ollama provides developers a range of powerful
machine learning models to work with.
</p>

## About
<p align="justify">
Ollama Adventures is a GitHub repository that contains a collection of Jupyter Notebooks demonstrating the features and capabilities of Ollama's models.
Ollama Adventures explores different avenues on how Ollama's Llama models are capable of answering questions, analyzing and summarizing PDF documents, analyzing
YouTube video transcripts, interpreting images, and analyzing complex datasets. 
</p>

## Setup for Local Environments
<p align="justify">
These notebooks were developed using Google Colab's Jupyter environment. If you plan on playing around with these notebooks in your local environment modifications to these notebooks' setup or code will be needed whether that's to run commands, code syntax, package installation, etc. If you want to pursue running these notebooks locally ensure you meet the following requirements:
</p>

  * RAM Requirements
    * 8 GB of RAM available to run 7B models.
    * 16 GB of RAM available to run 13B models.
    * 32 GB of RAM available to run 33B models.
    * More on this available here https://github.com/ollama/ollama?tab=readme-ov-file#model-library
  * GPU Selection
    * Ollama supports Nvidia GPUs with compute capability 5.0+.
      * NVIDIA GPUs supported https://github.com/ollama/ollama/blob/main/docs/gpu.md#nvidia
    * Ollama supports certain AMD Radeon GPUs
      * AMD Radeon GPUs supported https://github.com/ollama/ollama/blob/main/docs/gpu.md#amd-radeon
  * Disk Space
    * Ensure you have enough disk space to store Ollama's large language mode files.
  * Python 3.3 or greater.
  * Jupyter (preferably recommend using the Anaconda distribution to install Python and Jupyter)
  * Python packages these notebooks used (refer to requirements.txt)
  * Notebook Modifications:
    * Update notebook code command syntax.
    * Update notebook paths and commands to point to local directories and resources instead of Colab-specific paths.
    

  
    
