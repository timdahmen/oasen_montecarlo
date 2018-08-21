from multiset import *

class Bedarf:
	def __init__( self, warentyp, anzahl, preis, einkauf ):
		self.waren = Multiset()
		for i in range( 0, anzahl ):
			self.waren.add( warentyp )
		self.preis = preis
		self.einkauf = einkauf * anzahl
		self.stadt = None
		
	def __str__(self):
		result = "Bedarf: "
		for ware in self.waren:
			result = result + ware + " "
		result = result + "zu " + str( self.preis ) + " Geld"
		return result 
		
	def __repr__(self):
		return self.__str__()
		
	def gewinn(self):
		return self.preis - self.einkauf