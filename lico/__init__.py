# A module to control arduino lights according to the output of your code
#Author: Sanjay Marison
#LICO --- LIGHT CODE
#and yea i know it resembles ligo(gravitational waves detector) in name
#you free to do whatever u want with the code


import pyfirmata
import time


class phycode():
	#change the port for window (currently set for mac)
	#u can change the pin where each colour leds are connected directly
	def __init__(self,red=11,green=12,blue=13,port='/dev/cu.usbmodem14201'):
		self.red = red
		self.green = green
		self.blue = blue
		self.help = """
Keys which are accepted:

1)  error 
2)  sucess
3)  warning
4)  loading
5)  flash
6)  stop
7)  blue_
8)  red_
9)  green_
10) blink

if you get a serial error then the port might be wrong , try changing it.

		"""

		self.board = pyfirmata.Arduino(port)

	def error(self):
		#red colour
		for i in range(10):
			self.board.digital[self.red].write(1)
	def sucess(self):
		#green colour
		for i in range(10):
			self.board.digital[self.green].write(1)
	def warning(self):
		#blue colour
		for i in range(10):
			self.board.digital[self.blue].write(1)
	def loading(self,times=10):#set the times for how many times the cycle must repeat
		#red turned on and off next blue the same then next green the same 
		for i in range(times):
			for x in [self.red,self.blue,self.green]:
				self.board.digital[x].write(1)
				time.sleep(0.5)
				self.board.digital[x].write(0)
	def flash(self):
		#more like a flashlight
		for i in range(10):
			for x in [self.red,self.blue,self.green]:
				self.board.digital[x].write(1)
	def stop(self):
		#turns off all led
		for i in range(10):
			for x in [self.red,self.blue,self.green]:
				self.board.digital[x].write(0)
	def blue_(self):
		for i in range(10):
			self.board.digital[self.blue].write(1)
	def red_(self):
		for i in range(10):
			self.board.digital[self.red].write(1)
	def green_(self):
		for i in range(10):
			self.board.digital[self.green].write(1)
	def blink(self,times=10):#set the times for how many times the cycle must repeat
		#blink red,green and blue turned off and back on continuously
		for i in range(times):
			for x in [self.red,self.blue,self.green]:
				self.board.digital[x].write(1)
			time.sleep(0.5)
			for x in [self.red,self.blue,self.green]:
				self.board.digital[x].write(0)
			time.sleep(0.5)
			
	def console(self):
		#terminal control for all the leds
		while True:
			x = str(input(">"))
			#hasattr checks if a function exists inside a class when given the function name as a string
			if hasattr(self,x):
				result = eval("self."+x+"()")
			else:
				print("Your input is not valid please try again")

if __name__ == '__main__':
	#test the leds and its function directly from the terminal
	s = phycode()
	s.console()
