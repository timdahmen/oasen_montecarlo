from multiset import *

class Stadt:
	def __init__( self, position, spiel ):
		self.debug = False
		self.bedarfe = []
		self.position = position
		self.spiel = spiel

	def zieheBedarfe( self ):
		while len( self.bedarfe ) < 3:
			bedarf = self.spiel.bedarfe.pop(0)
			bedarf.stadt = self
			self.bedarfe.append( bedarf ) 
		if self.debug:
			print("Bedarfe:",self.bedarfe)