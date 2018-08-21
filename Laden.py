import Bedarf
from random import choice

class Laden:
	def __init__( self, name, waren, preis, position ):
		self.debug = False
		self.name = name
		self.waren = waren
		self.preis = preis
		self.position = position
		self.auslage = []

	def spezifischeBedarfe( self ):
		bedarfe = []
		for ware in self.waren:
			bedarfe.append( Bedarf.Bedarf( ware, 1, self.preis * 2 + 1     , self.preis ) )
			bedarfe.append( Bedarf.Bedarf( ware, 2, self.preis * 3 * 2 + 1 , self.preis ) )
			# bedarfe.append( Bedarf.Bedarf( ware, 2, self.preis * 2 * 2 + 3 , self.preis ) )
			# bedarfe.append( Bedarf.Bedarf( ware, 3, self.preis * 2 * 2 + 5 , self.preis ) )
		return bedarfe

	def fuelleAuslage( self ):
		while len(self.auslage) < 3:
			self.auslage.append( choice( list( self.waren ) ) )
		if self.debug:
			print (self.name, self.auslage)
		
		
	