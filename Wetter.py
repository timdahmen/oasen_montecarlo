import random

c  = (  0, 0, 0 )
w  = ( -1, 1, 0 )
o  = (  1,-1, 0 )
nw = (  0, 1,-1 )
so = (  0,-1, 1 )
no = (  1, 0,-1 )
sw = ( -1, 0, 1 )

class Wetter:
	def __init__( self, spiel ):
		self.wettersack = []
		for i in range(0,3):
			self.wettersack += [("wind_o", "wind_no"),( "wind_o", "wind_so") ]
			self.wettersack += [("wind_w", "wind_sw"),( "wind_w", "wind_nw") ]
		self.wettersack += [("regen", "sturm_w"),("regen", "sturm_n")]
		self.wettersack += [("regen", "sturm_o"),("regen", "sturm_s")]
		random.shuffle( self.wettersack )
		
	def richtungToString( self, richtung ):
		if richtung == no:
			return "no"
		if richtung == o:
			return "o"
		if richtung == so:
			return "so"
		if richtung == sw:
			return "sw"
		if richtung == w:
			return "w"
		if richtung == nw:
			return "nw"
		return "ungültige richtung:" + str(richtung)
		
	def zieheWetter( self ):
		chip = self.wettersack.pop()
		seite = random.randint(0,1)
		self.aktuellesWetter = chip[seite]
		
	def zugGratis( self, richtung ):
		if self.aktuellesWetter is "windstill":
			return False
			
		if self.aktuellesWetter is "wind_no":
			return richtung == sw
		if self.aktuellesWetter is "wind_o":
			return richtung == w
		if self.aktuellesWetter is "wind_so":
			return richtung == nw
		if self.aktuellesWetter is "wind_sw":
			return richtung == no
		if self.aktuellesWetter is "wind_w":
			return richtung == o
		if self.aktuellesWetter is "wind_nw":
			return richtung == so

		if self.aktuellesWetter is "sturm_n":
			return (richtung == so) or (richtung == sw)
		if self.aktuellesWetter is "sturm_s":
			return (richtung == no) or (richtung == nw)
		if self.aktuellesWetter is "sturm_w":
			return richtung == o
		if self.aktuellesWetter is "sturm_o":
			return richtung == w
			
		return False

	def zugUngueltig( self, richtung ):
		if self.aktuellesWetter is "windstill":
			return False
			
		if self.aktuellesWetter is "wind_no":
			return richtung == no
		if self.aktuellesWetter is "wind_o":
			return richtung == o
		if self.aktuellesWetter is "wind_so":
			return richtung == so
		if self.aktuellesWetter is "wind_sw":
			return richtung == sw
		if self.aktuellesWetter is "wind_w":
			return richtung == w
		if self.aktuellesWetter is "wind_nw":
			return richtung == nw

		if self.aktuellesWetter is "sturm_n":
			return (richtung == nw) or (richtung == no)
		if self.aktuellesWetter is "sturm_s":
			return (richtung == so) or (richtung == sw)
		if self.aktuellesWetter is "sturm_w":
			return (richtung == nw) or (richtung == w) or (richtung == sw)
		if self.aktuellesWetter is "sturm_o":
			return (richtung == no) or (richtung == o) or (richtung == so)
			
		return False
		