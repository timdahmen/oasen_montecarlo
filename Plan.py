from multiset import *
import Spielfeld
import Bedarf

class Plan:
	def __init__( self, spielfeld, route ):
		self.spielfeld = spielfeld
		self.route = route
		self.heuristischerWert = None

	def routenKosten( self, route ):
		kosten = 0
		for i in range(1, len(route) ):
			von = route[i-1][0]
			bis = route[i][0]
			kosten += self.spielfeld.hexDistanz(von,bis)
		return kosten

	def aktion( self, poi ):
		if poi == None:
			return "Start"
		if isinstance( poi, Bedarf.Bedarf ):
			return "Verkauf"
		return str(poi)
	
	def routenStopBeschreibung( self, position, poi ):
		return str( position[0] ) + "/" + str( position[1]) + " (" + self.aktion( poi ) + ")"
	
	def routenBeschreibung( self ):
		s = ""
		for ( position, poi ) in self.route[:-1]:
			s += self.routenStopBeschreibung(position,poi) + " -> "
		( position, poi ) = self.route[-1]
		s += self.routenStopBeschreibung(position,poi)
		return s
		
	def __str__( self ):
		s  = self.routenBeschreibung()
		s += " distanz: " + str( self.routenKosten( self.route) ) 
		s += " gewinn: " + str( self.gewinn() )
		s += " bewertung: " + str( self.heuristischeBewertung() )
		return s
		
	def gewinn( self ):
		return self.route[ len( self.route )-1 ][1].gewinn()
		
	def heuristischeBewertung( self ):
		kosten = self.routenKosten( self.route )
		gewinn = self.gewinn()
		quotient = gewinn / (kosten + 0.1)
		self.heuristischerWert = quotient
		return quotient