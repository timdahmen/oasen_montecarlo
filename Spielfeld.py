import random
import multiset
import math

import Laden
import Stadt
import Gebirge

class Spielfeld:
	def __init__( self, spiel ):	
		pos = self.leadenPos()
		waren = multiset.Multiset(['honig', 'mandeln', 'orangen'])
		self.oase      = Laden.Laden( "oase", waren, 2, pos[0] )
		waren = multiset.Multiset(['feigen', 'datteln', 'minze'])
		self.garten    = Laden.Laden( "garten", waren, 2, pos[1] )
		waren = multiset.Multiset(['ring', 'halskette', 'ohrringe'])
		self.juwelier  = Laden.Laden( "juwelier", waren, 3, pos[2] )
		waren = multiset.Multiset(['wolle', 'seide', 'leder'])
		self.faerberei = Laden.Laden( "faerberei", waren, 3, pos[3] )		
		self.leaden = [ self.oase, self.garten, self.juwelier, self.faerberei ]
		
		pos = self.stadtPos()
		stadt0 = Stadt.Stadt( pos[0], spiel )
		stadt1 = Stadt.Stadt( pos[1], spiel )
		stadt2 = Stadt.Stadt( pos[2], spiel )
		stadt3 = Stadt.Stadt( pos[3], spiel )
		self.staedte = [ stadt0, stadt1, stadt2, stadt3 ]
		
		self.gebirge = []

		positionenKategorieA = [ (2,0), (7,0), (2,3) ]
		random.shuffle( positionenKategorieA )
		for i in range( 0, 3 ):
			self.gebirge.append( Gebirge.Gebirge( i+1, self.offset_to_cube( positionenKategorieA[i] ) ) )

		positionenKategorieB = [ (1,7), (6,7), (6,4) ]
		random.shuffle( positionenKategorieB )
		for i in range( 0, 3 ):
			self.gebirge.append( Gebirge.Gebirge( i+4, self.offset_to_cube( positionenKategorieB[i] ) ) )
			
		positionenKategorieC = [ (3,0), (4,3), (7,4), (4,5), (2,7) ]
		random.shuffle( positionenKategorieC )
		for i in range( 0, 5 ):
			self.gebirge.append( Gebirge.Gebirge( i+7, self.offset_to_cube( positionenKategorieC[i] ) ) )

		positionenKategorieD = [ (5,1), (3,3), (1,4), (3,5), (5,8) ]
		random.shuffle( positionenKategorieD )
		for i in range( 0, 5 ):
			self.gebirge.append( Gebirge.Gebirge( i+12, self.offset_to_cube( positionenKategorieD[i] ) ) )		
		
	def leadenPos( self ):
		laedenPos = [ (2,0), (6,0), (0,4), (8,4), (2,8), (6,8) ]
		random.shuffle( laedenPos )
		return laedenPos
	
	def ladenAnPosition( self, position ):
		for laden in self.leaden:
			if laden.position == position:
				return laden
		return None
	
	def stadtPos( self ):
		stadtPos = [ (0,0), (0,8), (8,0), (8,8) ]
		return stadtPos
	
	def feldTyp( self, x, y ):
		if not self.isInside( (x,y) ):
			return "rand"

		if  ( x == 0 or x == 8 ) and ( y == 0 or y == 8 ):
			return "stadt"

		for laden in self.leaden:
			if ( x,y ) == laden.position:
				print( laden.name, "at", (x,y) )
				return laden.name
		return "leer"

	def hoehe( self, von, nach ):
		hoeheMaximum = 0
		for gebirge in self.gebirge:
			gebirgsHoehe = gebirge.hoehe( self.offset_to_cube(von), self.offset_to_cube(nach) ) 
			hoeheMaximum = max( hoeheMaximum, gebirgsHoehe )
		return hoeheMaximum
		
	def nachbarn( self, pos ):
		nachbarn = [ (pos[0]-1, pos[1] ), (pos[0]+1, pos[1] ) ]
		if pos[1] % 2 == 0:
			nachbarn.append( (pos[0]-1, pos[1]-1 ) )
			nachbarn.append( (pos[0],   pos[1]-1 ) )
			nachbarn.append( (pos[0]-1, pos[1]+1 ) )
			nachbarn.append( (pos[0],   pos[1]+1 ) )
		else:
			nachbarn.append( (pos[0],   pos[1]-1 ) )
			nachbarn.append( (pos[0]+1, pos[1]-1 ) )
			nachbarn.append( (pos[0],   pos[1]+1 ) )
			nachbarn.append( (pos[0]+1, pos[1]+1 ) )
		return self.filtereRand(nachbarn)
	
	def isInside( self, position ):
		if position[0] < 0 or position[1] < 0:
			return False
		if position[1] > 8:
			return False
		if position[1] % 2 == 0 and position[0] > 8:
			return False
		if position[1] % 2 == 1 and position[0] > 7:
			return False
		return True
		
	def filtereRand( self, felder ):
		result = []
		for feld in felder:
			if self.isInside( feld ):
				result.append( feld )
		return result
	
	def hexDistanz( self, vonPosition, nachPosition ):
		ac = self.offset_to_cube(vonPosition)
		bc = self.offset_to_cube(nachPosition)
		return self.cube_distance(ac, bc)
		
	def offset_to_cube( self, hex ):
		x = hex[0] - (hex[1] - (hex[1] & 1)) / 2
		z = hex[1]
		y = -x-z
		return (x, y, z)
		
	def cube_to_offset( self, cube ):
		col = cube[0] + (cube[2] - (cube[2]&1)) / 2
		row = cube[2]
		return (col, row)
		
	def cube_distance( self, a, b ):
		return (abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])) / 2
