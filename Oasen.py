from random import shuffle

import Laden
import Spielfeld
import Bedarf
import Spieler
import Ki

import SVGOutput

print("Oasen!")

class Oasen:
	def __init__( self ):
		self.bedarfe = []
		self.spielfeld = Spielfeld.Spielfeld( self ) 
		self.bedarfe = self.erstelleBedarfe()
		self.maxInventory = 6
		self.erstelleSpieler()
		self.nachziehPhase( )
		return
		
	def erstelleBedarfe( self ):
		bedarfe = []
		for laden in self.spielfeld.leaden:
			bedarfe = bedarfe + laden.spezifischeBedarfe()
		shuffle( bedarfe )	
		return bedarfe

	def erstelleSpieler( self ):
		self.spieler = []
		for i in range(0, 4):
			self.spieler.append( Spieler.Spieler( "spieler" + str(i), self.spielfeld.staedte[i].position, self ) )

	def wechseleStartSpieler( self ):
		tmp = self.spieler[0]
		del self.spieler[0]
		self.spieler.append( tmp )
			
	def runde( self ):
		self.wechseleStartSpieler()
		for aktuellerSpieler in self.spieler:
			aktuellerSpieler.zug()
		self.nachziehPhase()
	
	def nachziehPhase( self ):
		for laden in self.spielfeld.leaden:
			laden.fuelleAuslage()
		for stadt in self.spielfeld.staedte:
			stadt.zieheBedarfe()	
	
	def zugGueltig( self, spieler, position ):
		if not position in self.spielfeld.nachbarn( spieler.position ):
			print("ungültiger zugversuch von ",spieler.position, "nach", position )
			return False
		if spieler.bewegungspunkte <= 0:
			print("ungültiger zugversuch (keine Bewegungspunkte)" )
			return False
		bergHoehe = self.spielfeld.hoehe( spieler.position, position )
		if spieler.flughoehe < bergHoehe:
			print( "ungültiger zugversuch (hoehe: ", spieler.flughoehe, "erforderlich:",bergHoehe,")" )
			return False		
		return True
	
	def aktionBewege( self, spieler, position ):
		if self.zugGueltig( spieler, position ):
			spieler.position = position
			spieler.bewegungspunkte -= 1
			print( spieler.name, "bewegt nach", spieler.position )
		else:
			quit()
	
	def kaufGueltig( self, spieler, ware ):
		laden = self.spielfeld.ladenAnPosition( spieler.position )
		if laden == None:
			return False
		if not ware in laden.auslage:
			return False
		if spieler.geld < laden.preis:
			return False
		if len( spieler.inventory ) > self.maxInventory:
			return False
		return True
			
	def aktionKaufe( self, spieler, ware ):
		if self.kaufGueltig( spieler, ware ):
			laden = self.spielfeld.ladenAnPosition( spieler.position )
			laden.auslage.remove( ware ) 
			spieler.inventory.add( ware )
			spieler.geld -= laden.preis
			print( spieler.name, "kauft", ware, "für", laden.preis, "Geld" )
		else:
			print("ungültiger kaufversuch: ", spieler.name, ware )
			quit()
			
	def verkaufGueltig( self, spieler, bedarf ):
		stadt = bedarf.stadt
		if not stadt.position is spieler.position:
			print("ungültiger verkaufversuch: ", spieler.name, "position", spieler.position, "nicht in Stadt position", stadt.position )
			return False
		if not bedarf in stadt.bedarfe:
			print("ungültiger verkaufversuch: Bedarf nicht in Stadt" )
			return False
		checkInventory = spieler.inventory.copy()
		for ware in bedarf.waren:
			if not ware in checkInventory:
				print("ungültiger verkaufversuch: ", ware, "nicht auf Teppich" )
				return False
			else:
				checkInventory.discard(ware,1)
		return True			
			
	def aktionVerkaufe( self, spieler, bedarf ):
		if self.verkaufGueltig( spieler, bedarf ):
			stadt = bedarf.stadt
			stadt.bedarfe.remove( bedarf )
			self.bedarfe.append( bedarf )
			for ware in bedarf.waren:
				spieler.inventory.discard( ware, 1 )

			spieler.geld += bedarf.preis
			print( spieler.name, "verkauft", bedarf.waren, "für", bedarf.preis, "Geld Besitz:", spieler.geld )
		else:
			quit()
			
spiel = Oasen()

for i in range(0,16):
	print("==========")
	print("Runde", i)
	print("==========")
	spiel.runde()
	# SVGOutput.zeichneSpielfeld( spiel, spiel.spielfeld, "runde"+str(i)+".svg" )