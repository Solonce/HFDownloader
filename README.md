# HFDownloader - Hugging Face Model Downloader

### This package provides the user with one method that downloads a tokenizer and model from [HuggingFace Model Hub](https://huggingface.co/models) to a local path. 

This package utilizes the `transformers` library to download a tokenizer and model using just one method. When a model is downloaded, it will save a state from a loaded tokenizer and model to a local path. If the path does not exist, the method will create one with the title passed.

This Github repo also allows you to run '`hf_downloader.py`' like a script if you don't want to open a python terminal. It has two positional arguments, the model and the pathname you wish the model to save to. Example usage may look something like this in the command line.

    python hf_downloader.py cardiffnlp/twitter-roberta-base-sentiment sentiment_model_path


# Installation
The package can be installed with the following command:

    pip install hfdownloader

# How to Use
Here is a bit of code you can reference to see how to use the package. I will be using another package I released called [HFLoader](https://github.com/Solonce/HFLoader), that simply loads the tokenizer and model. You can do this in any way, this package is not required.

    import hlfloader as hfl
    import hfdownload as hfd
    
    huggingface_model = "cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer, model = hfl.load_model(huggingface_model)
    hfd.save_model("HuggingFaceModelPath", tokenizer, model)
    
    
The code above is the easiest way I have found to save models from the HuggingFace Model Hub locally.

## Requirements
> pip install transformers

**Not required but helpful**
> pip install hfloader

## Notes
I don't have plans to upkeep this project unless it necessitates it. I was able to achieve the goal I had set out when developing the package.