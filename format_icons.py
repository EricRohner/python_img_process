#!/usr/bin/env python3
import os, sys
from PIL import Image

source = os.getcwd() + "/images"
destination = os.getcwd() + "/icons"

def get_source_files():
	source_files = os.listdir(source)
	source_files.remove(".DS_Store")
	return source_files

def process_img(file):
	path = source + "/" + file
	print(path)
	im = Image.open(path)
	im = im.rotate(-90)
	im = im.resize((120,120))
	im = im.convert("RGB")
	im.save(destination + "/" + file + ".jpeg")

if __name__ == "__main__":
	source_files = get_source_files()
	for file in source_files:
		process_img(file)
