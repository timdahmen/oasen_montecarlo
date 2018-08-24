import multiset
import itertools

import Spielfeld
import Bedarf
import Plan
import AStar

class Ki:
	def __init__( self, spieler, spiel ):
		self.debug = False
		self.spiel = spiel
		self.spieler = spieler
		spieler.ki = self
		self.spielfeld = spiel.spielfeld
		self.searchalgorithm = AStar.AStar( self.spieler, self.spielfeld, spiel.wetter )
		
	def bedarfMachbar( self, bedarf ):
		gesamteAuslage = multiset.Multiset()
		for laden in self.spielfeld.leaden:
			for ware in laden.auslage:
				gesamteAuslage.add( ware )
		for ware in self.spieler.inventory:			
			gesamteAuslage.add( ware )
		
		for ware in bedarf.waren:
			if not self.wareMachbar( ware, gesamteAuslage ):
				# print("nicht machbar:",bedarf,"es fehlt:",ware)
				return False
				
		return True
		
	def wareMachbar( self, ware, gesamteAuslage ):
		if not ware in gesamteAuslage:
			return False
		gesamteAuslage.discard( ware, 1 )
		return True
		
	def ladenMitAngebot( self, ware ):
		for laden in self.spielfeld.leaden:
			if ware in laden.auslage:
				return laden				
		return None
		
	def moeglicheRouten( self, bedarf ):
		moeglicheRouten = []
		bedarfPermutationen = list( itertools.permutations( bedarf.waren ) )
		for permutation in bedarfPermutationen:
			warenListe = list( permutation )
			planInventory = self.spieler.inventory.copy()			
			route = []
			route.append( ( self.spieler.position, None ) ) 
			for ware in warenListe:
				if ware in planInventory:
					planInventory.discard(ware,1)
					continue
				ladenPosition = self.ladenMitAngebot( ware ).position
				route.append( ( ladenPosition, ware ) ) 
			route.append( ( bedarf.stadt.position, bedarf ) )
			moeglicheRouten.append( route )
		return moeglicheRouten
				
	def macheMakroPlan( self ):
		machbareBedarfe = []
		for stadt in self.spielfeld.staedte:
			for bedarf in stadt.bedarfe:
				if self.bedarfMachbar( bedarf ):
					machbareBedarfe.append( bedarf )

		plaene = []
					
		for bedarf in machbareBedarfe:
			# print(bedarf, "(machbar)")
			for route in self.moeglicheRouten( bedarf ):
				plan = Plan.Plan( self.spielfeld, route )
				plaene.append( plan )
				
		plaene.sort( key=lambda plan: plan.heuristischeBewertung(), reverse=True )
		
		if len( plaene ) > 0:
			if self.debug:
				print("Makroplan für Spieler", self.spieler.name, ":", plaene[0] )
			return plaene[0]
		return None

	def macheMikroPlan( self, makroplan ):
		mikroplan = []
		for i in range(1,len(makroplan.route)):
			start = makroplan.route[i-1][0]
			ziel = makroplan.route[i][0]
			(bewegung,cost,erfolg) = self.searchalgorithm.search( start, ziel )
			if not erfolg:
				return None

			mikroplan += bewegung
			aktion = makroplan.route[i][1]
			
			if ( type(aktion) is str ):
				mikroplan.append( ( "kaufe", aktion ) )
			if isinstance( aktion, Bedarf.Bedarf ):
				mikroplan.append( ( "verkaufe", aktion ) )
		if self.debug:		
			print("Mikroplan",mikroplan)
		return mikroplan
