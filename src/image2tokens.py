import os
from google.oauth2 import service_account

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credential.json"

class Token():
    def __init__(self,x,y,width,height,text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

def extractTokens(image):
	tokens = []

	for page in image['fullTextAnnotation']['pages']:
	    for block in page["blocks"]:
	        for paragraph in block["paragraphs"]:
	            text = ""
	            firstWord = paragraph["words"][0]

	            i = 1
	            n = len(paragraph["words"])
	            for word in paragraph["words"]:
	                lastWord = word

	                breakType = None
	                if len(word["symbols"]) > 0 and "property" in word["symbols"][-1] and "detectedBreak" in word["symbols"][-1]["property"]:
	                    breakType = word["symbols"][-1]["property"]["detectedBreak"];

	                for symbol in word["symbols"]:
	                    text += symbol["text"]

	                if breakType != None:# and breakType in ["LINE_BREAK",""]:
	                    vertices = firstWord["boundingBox"]["vertices"]
	                    minX = vertices[0]["x"]
	                    minY = vertices[0]["y"]
	                    maxY = vertices[3]["y"]
	                    vertices = lastWord["boundingBox"]["vertices"]
	                    maxX = vertices[1]["x"]

	                    newToken = Token(minX, maxY, maxX - minX, maxY - minY, text)
	                    tokens.append(newToken)

	                    text = ""
	                    if i < n:
	                        firstWord = paragraph["words"][i];

	                i += 1
	return tokens

def createLine(tokens):
	MAX_SPACE_BETWEEN_WORDS = 25

	tokens = sorted(tokens, key=lambda token : token.x)

	last = tokens[0]
	text = ""
	for token in tokens[1:]:
		if token.x - (last.x + last.width) > MAX_SPACE_BETWEEN_WORDS:
			text += last.text + "\t" 
		else:
			text += last.text + " "

		last = token

	text += tokens[-1].text

	return text.split("\t")

def extractLines(tokens):
	tokens = sorted(tokens, key=lambda token : token.y)


	newLine = []
	lines = []

	newLine.append(tokens[0])
	lastY = tokens[0].y
	lastX = tokens[0].x + tokens[0].width

	for token in tokens[1:]:
	    if token.y > lastY + token.height * 0.85:
	        lines.append(createLine(newLine))
	        lastY = token.y
	        newLine = []
	    newLine.append(token)
	    lastX = token.x + token.width

	lines.append(createLine(newLine))

	return lines
