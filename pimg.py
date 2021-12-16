import cv2
import urllib.request
import sys
from colr import Colr as C

class imagePrinter():
	def __init__(self, img_path, width):
		if img_path.startswith('https://'):
			self.url = img_path
			urllib.request.urlretrieve(self.url, "%temp%temp.jpg")
			self.img_path = "%temp%temp.jpg"
		else:
			self.img_path = img_path
		self.img = cv2.imread(str(self.img_path), cv2.IMREAD_COLOR)

		self.height, self.width, self.channels = self.img.shape
		self.resizing_width = int(width)

		## 세로 / 가로 = x, 가로*x=세로
		self.img_size = (int(self.resizing_width),int((self.height/self.width)*self.resizing_width))

		self.convert()

	def convert(self):
		self.img_resized = cv2.resize(self.img, self.img_size, interpolation = cv2.INTER_CUBIC)

	def print(self):
		self.line = ''
		for i in self.img_resized:
			for j in i:
				self.line += self.colored(j, '██')
			print(self.line)
			self.line = ''
				
	def colored(self, color, text):
    	return "\033[38;2;{};{};{}m{}\033[0m".format(color[2], color[1], color[0], text)

if __name__ == '__main__':
	temp = imagePrinter(sys.argv[1], sys.argv[2])
	temp.print()