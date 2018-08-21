import random

class Wuerfel:
	def __init__( self, typ ):
		if ( typ=="W4" ):
			self.werte = [1,2,3,4]
		elif ( typ=="W6" ):
			self.werte = [4,4,4,5,5,6]
		elif ( typ == "W8" ):
			self.werte = [1,2,3,4,5,6,7,7]
		elif ( typ == "W12" ):
			self.werte = [4,4,4,5,5,6,7,8,9,10,11,12]
	
	def wuerfele( self ):
		return random.choice( self.werte )