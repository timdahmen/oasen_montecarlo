import random

c  = (  0, 0, 0 )
w  = ( -1, 1, 0 )
o  = (  1,-1, 0 )
nw = (  0, 1,-1 )
so = (  0,-1, 1 )
no = (  1, 0,-1 )
sw = ( -1, 0, 1 )

def feld( weg ):
	(x,y,z) = (0,0,0)
	for schritt in weg:
		x += schritt[0]
		y += schritt[1]
		z += schritt[2]
	return (x,y,z)

class Gebirge:
	def __init__( self, typ, position ):
		self.grenzen = {}
		
		if ( typ is 1 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp1(), position )
		if ( typ is 2 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp2(), position )
		if ( typ is 3 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp3(), position )
		if ( typ is 4 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp4(), position )
		if ( typ is 5 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp5(), position )
		if ( typ is 6 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp6(), position )
		if ( typ is 7 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp7(), position )
		if ( typ is 8 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp8(), position )
		if ( typ is 9 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp9(), position )
		if ( typ is 10 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp10(), position )
		if ( typ is 11 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp11(), position )
		if ( typ is 12 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp12(), position )
		if ( typ is 13 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp13(), position )
		if ( typ is 14 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp14(), position )
		if ( typ is 15 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp15(), position )
		if ( typ is 16 ):
			self.grenzen = self.invertiereUndSchiebe( self.erstelleTyp16(), position )			
			
	def hoehe( self, positionVon, positionBis ):
		if not positionVon in self.grenzen.keys():
			return 0
		rand = self.grenzen[positionVon]
		if not positionBis in rand.keys():
			return 0
		return rand[positionBis]
	
	def verschiebe( self, offset, grenzen ):
		offset = psiel
	
	def invertiereUndSchiebe( self, grenzen, position ):
		alleGrenzen = {}
		for vonLokal in grenzen.keys():
			for nachLokal in grenzen[vonLokal]:
				hoehe = grenzen[vonLokal][nachLokal]
				von  = ( vonLokal[0] + position[0], vonLokal[1] + position[1], vonLokal[2] + position[2])
				nach = ( vonLokal[0] + nachLokal[0] + position[0], vonLokal[1] + nachLokal[1] + position[1], vonLokal[2] + nachLokal[2] + position[2] )
				if not von in alleGrenzen:
					alleGrenzen[von] = {}
				alleGrenzen[von][nach] = hoehe
				if not nach in alleGrenzen:
					alleGrenzen[nach] = {}
				alleGrenzen[nach][von] = hoehe
		return alleGrenzen

	def erstelleTyp1( self ):
		grenzen = {}
		grenzen[ c ]                = { nw: 0, w: 0, sw: 0 }
		grenzen[ sw ]               = { o: 0, so: 3, sw: 3 }
		grenzen[ feld( [ sw,sw ]) ] = { o: 3 }
		return grenzen
		
	def erstelleTyp2( self ):
		grenzen = {}
		grenzen[ c ]                = { nw: 4, w: 4, sw: 4 }
		grenzen[ sw ]               = { o: 3, so: 4, sw: 4 }
		grenzen[ feld( [ sw,sw ]) ] = { o: 4 }
		return grenzen
		
	def erstelleTyp3( self ):
		grenzen = {}
		grenzen[ c ]                = { nw: 0, w: 0, sw: 0 }
		grenzen[ sw ]               = { o: 3, so: 3, sw: 3 }
		grenzen[ feld( [ sw,sw ]) ] = { o: 3 }
		return grenzen

	def erstelleTyp4( self ):
		grenzen = {}
		grenzen[ c ]  = { no: 3, nw: 3, w: 0, sw: 0 }
		grenzen[ nw ] = { o: 3 }
		grenzen[ sw ] = { o: 3, so: 3 }
		return grenzen
		
	def erstelleTyp5( self ):
		grenzen = {}
		grenzen[ c ]  = { no: 4, nw: 4, w: 4, sw: 3 }
		grenzen[ nw ] = { o: 4 }
		grenzen[ sw ] = { o: 4, so: 4 }
		return grenzen

	def erstelleTyp6( self ):
		grenzen = {}
		grenzen[ c ]  = { no: 0, nw: 3, w: 3, sw: 3 }
		grenzen[ nw ] = { o: 0 }
		grenzen[ sw ] = { o: 3, so: 0 }
		return grenzen
		
	def erstelleTyp7( self ):
		grenzen = {}
		grenzen[ c ]  = { sw: 3, so: 3, o: 3 }
		grenzen[ w ]  = { so: 3 }
		grenzen[ so ] = { no: 3 }
		return grenzen		
	
	def erstelleTyp8( self ):
		grenzen = {}
		grenzen[ c ]          = { sw: 4, so: 4, o: 3 }
		grenzen[ sw ] = { nw: 4 }
		grenzen[ so ] = { no: 4 }
		return grenzen	
	
	def erstelleTyp9( self ):
		grenzen = {}
		grenzen[ c ]          = { sw: 0, so: 0, o: 0 }
		grenzen[ sw ] = { nw: 0 }
		grenzen[ so ] = { no: 0	 }
		return grenzen	
		
	def erstelleTyp10( self ):
		grenzen = {}
		grenzen[ c ]  = { sw: 0, so: 0, o: 3 }
		grenzen[ w ]  = { so: 0 }
		grenzen[ so ] = { no: 3 }
		return grenzen	
	
	def erstelleTyp11( self ):
		grenzen = {}
		grenzen[ c ] = { so: 3, o: 4, sw: 0 }
		grenzen[ sw ] = { nw: 3 }
		grenzen[ so ] = { no: 4 }
		return grenzen	
		
	def erstelleTyp12( self ):
		grenzen = {}
		grenzen[ c ] = { w:  3, nw: 3, no: 3 }
		grenzen[ w ] = { no: 3 }
		grenzen[ o ] = { nw: 3 }
		return grenzen		
		
	def erstelleTyp13( self ):
		grenzen = {}
		grenzen[ c ] = { w:  3, nw: 4, no: 4 }
		grenzen[ w ] = { no: 4 }
		grenzen[ o ] = { nw: 4 }
		return grenzen	
		
	def erstelleTyp14( self ):
		grenzen = {}
		grenzen[ c ] = { w:  0, nw: 0, no: 0 }
		grenzen[ w ] = { no: 0 }
		grenzen[ o ] = { nw: 0 }
		return grenzen		
		
	def erstelleTyp15( self ):
		grenzen = {}
		grenzen[ c ] = { w:  0, nw: 3, no: 3 }
		grenzen[ w ] = { no: 0 }
		grenzen[ o ] = { nw: 3 }
		return grenzen	
		
	def erstelleTyp16( self ):
		grenzen = {}
		grenzen[ c ] = { w:  4, no: 4, nw: 0 }
		grenzen[ w ] = { no: 4 }
		grenzen[ o ] = { nw: 4 }
		return grenzen	