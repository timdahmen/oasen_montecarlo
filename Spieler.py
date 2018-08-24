import multiset
import Wuerfel
import Ki

class Spieler:
	def __init__( self, name, position, spiel ):
		self.name = name
		self.bedarfe = []
		self.position = position
		self.spiel = spiel
		self.weitenWuerfel = Wuerfel.Wuerfel("W6")
		self.hoehenWuerfel = Wuerfel.Wuerfel("W4")
		self.bewegungspunkte = 0
		self.flughoehe = 0
		self.inventory = multiset.Multiset()
		self.geld = 15
		self.letzterZug = []
		ki = Ki.Ki( self, spiel )
		print("erstelle Spieler: ", self.name, "in", self.position )
	
	def wuerfele( self ):
		self.bewegungspunkte = self.weitenWuerfel.wuerfele()
		self.flughoehe       = self.hoehenWuerfel.wuerfele()
	
	def zug( self ):
		print(self.name )
		self.letzterZug = [ ("start", self.position ) ]
		self.wuerfele()
		print("Weite",self.bewegungspunkte,"Höhe",self.flughoehe)
		while True:
			makroPlan = self.ki.macheMakroPlan( )
			if makroPlan == None:
				print("Spieler: ", self.name, "setzt aus" )
				return
			mikroPlan = self.ki.macheMikroPlan( makroPlan )
			if mikroPlan == None:
				print("Spieler: ", self.name, "setzt aus" )
				return
			for aktion in mikroPlan:
				if ( aktion[0] == "bewege" ):
					if self.bewegungspunkte == 0:
						return
					self.spiel.aktionBewege( self, aktion[1] )
				if ( aktion[0] == "kaufe" ):
					self.spiel.aktionKaufe( self, aktion[1] )
				if ( aktion[0] == "verkaufe" ):
					self.spiel.aktionVerkaufe( self, aktion[1] )
				self.letzterZug.append( aktion )
