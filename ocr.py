from googleVisionApi import GoogleVisionApi

def inferExtension(filePath):
	extension = filePath.split(".")[-1].lower()
	if len(extension) > 0:
		return extension
	raise Exception("No format found for: " + filePath)

def filename(filePath):
	extension = inferExtension(filePath)
	name = filePath.split("/")[-1][:-(len(extension)+1)]
	return name

class Ocr:
	def __init__(self):
		self.googleApi = GoogleVisionApi()

	def clearAll(self):
		self.googleApi.clearAll()

	def processFile(self,filePath, dstFolderPath):
		extension = inferExtension(filePath)

		if extension in ["jpg","jpeg","png"]:
			response = self.googleApi.request(filePath)

			with open(dstFolderPath + filename(filePath)+'.json','w') as f:
				f.write(response)

		else:
			print("Invalid Extension:")
			print(extension)
			print("\n")


