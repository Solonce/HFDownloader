import torch
import argparse
import os
import transformers
import hfloader as hfl
'''
Saves the model that has been loaded to cache to the disk
'''
def save_model(path_name, tokenizer, model):
	if os.path.exists(path_name) == False:                                                                        #  Ensures the path exists
		os.mkdir(path_name)                                                                                       #  If not, creates the path
		print(f"Created path /{path_name}")                                                                       #  Output for user

	tokenizer.save_pretrained(path_name)                                                                          #  Saves the tokenizer within the path
	model.save_pretrained(path_name)                                                                              #  Saves the model within the path
	print(f"Saved Model under /{path_name}")                                                                      #  Output for user


'''
Main code block ran when the script is called
'''
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Arguments for loading and saving a model from huggingfaces")    #  Loads the argument parser
	parser.add_argument('model', type=str, help="For example: HuggingFaceH4/zephyr-7b-beta")                      #  Argument for the model to download from HuggingFace Model Hub
	parser.add_argument('os_path_name', type=str, help="The path you wish for the model to save to.")             #  Argument for the path the model will be saved to
	args = parser.parse_args()                                                                                    #  Loads the arguments

	tokenizer, model = hfl.load_model(args.model)                                                                 #  Loads the model and stores the tokenizer and model variables 
	save_model(args.os_path_name, tokenizer, model)                                                               #  Saves the tokenizer and model to the path designated