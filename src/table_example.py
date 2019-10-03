from image2tokens import extractTokens, extractLines
from ocr import Ocr
import json
import sys

def changeFileExtension(path,newExtension):
	res = ''.join(path.split(".")[:-1])+'.'+newExtension
	print(res)
	return res

def main(imagePath):
	# Create OCR
	ocr = Ocr()

	# Run OCR over image. It generates a JSON with the text and the coordinates of each word
	ocr.processFile(imagePath,'./')

	# Read JSON and delete it
	jsonFile = changeFileExtension(imagePath.split("/")[-1],"json")
	with open(jsonFile,'r') as f:
	    image = json.load(f)

	# Extract tokens (Each word, its width, height and its coordinates)
	tokens = extractTokens(image)

	# Sort the tokens into lines
	lines = extractLines(tokens)

	txt = ""
	for line in lines:
		print(line)
		line = list(filter(lambda x : x != "–",line))
		try:
			txt += "{:>40}{:>40}{:>40}{:>40}\n".format(line[0],line[1],line[2],line[3])
		except:
			try:
				txt += "{:>40}{:>40}\n".format(line[0],line[1])
			except:
				pass

	with open(changeFileExtension(imagePath.split("/")[-1],"txt"),'w') as f:
		f.write(txt)

imagePath = sys.argv[1]
print('RUNNING ON ' + imagePath)
main(imagePath)