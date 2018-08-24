from svgutils import *
import math

def drawPosition( x, y ):
	x = x + 1
	y = y - 8
	size = 22.0
	w = math.sqrt(3.0) * size
	h = size * 2.0
	if y%2 is 0:
		drawx = (x+0.5) * w
	else:
		drawx = (x+1) * w
	drawy = y * 3/4 * h
	return (drawx,drawy)
		
def setzeIconAufFeld( figure, pos, filename ):
	icon = transform.fromfile(filename).getroot()
	(xdraw,ydraw) = drawPosition( pos[0],pos[1] )
	icon.moveto( xdraw, ydraw )
	figure.append( icon )
	return

def haengeIconAnFeld( figure, pos, filename, belegung ):
	icon = transform.fromfile(filename).getroot()
	(xdraw,ydraw) = drawPosition( pos[0],pos[1] )
	
	if pos in belegung.keys():
		belegung[pos] = belegung[pos] + 1
	else:
		belegung[pos] = 0

	ydraw -= 12
	ydraw += ( belegung[pos] % 4 ) * 6.0
	xdraw += math.floor( belegung[pos] / 4 ) * 6.0
	
	icon.moveto( xdraw, ydraw )
	figure.append( icon )
	return
	
def setzeIconZwischenFeld( figure, posA, posB, filename ):
	icon = transform.fromfile(filename).getroot()
	(xdrawA,ydrawA) = drawPosition( posA[0],posA[1] )
	(xdrawB,ydrawB) = drawPosition( posB[0],posB[1] )
	icon.moveto( (xdrawA+xdrawB)/2.0, (ydrawA+ydrawB)/2.0 )
	figure.append( icon )
	return

def zeichneSpielfeld( spiel, spielfeld, filename ):
	figure = transform.SVGFigure("10cm", "10cm")
	# background = transform.fromfile('img/spielfeld_leer.svg').getroot()
	# background.moveto( 0, 0 )
	# figure.append( background )

	for x in range( 0, 9 ):
		for y in range ( 0, 9 ):
			typ = spielfeld.feldTyp( x, y )
			if ( typ == "rand" ):
				continue
			setzeIconAufFeld( figure, (x,y), "img/leer.svg" )
			if ( typ != "leer"):
				setzeIconAufFeld( figure, (x,y), "img/"+typ+".svg" )
			
	for gebirge in spielfeld.gebirge:
		for von in gebirge.grenzen.keys():
			for nach in gebirge.grenzen[von]:
				hoehe = gebirge.grenzen[von][nach]
				vonOffset  = spielfeld.cube_to_offset( von )
				nachOffset = spielfeld.cube_to_offset( nach )
				# if hoehe is 0:
					# setzeIconZwischenFeld( figure, vonOffset, nachOffset, "img/gebirge_0.svg" )				
				if hoehe is 3:
					setzeIconZwischenFeld( figure, vonOffset, nachOffset, "img/gebirge_3.svg" )
				if hoehe is 4:
					setzeIconZwischenFeld( figure, vonOffset, nachOffset, "img/gebirge_4.svg" )

	belegung = {}
	for spieler in spiel.spieler:
		for aktion in spieler.letzterZug:
			if aktion[0] is "start":
				haengeIconAnFeld( figure, aktion[1], "img/" + spieler.name + "_start.svg", belegung)
				position = aktion[1]	
			if aktion[0] is "bewege":
				haengeIconAnFeld( figure, aktion[1], "img/" + spieler.name + "_bewegung.svg", belegung)
				position = aktion[1]	
			if aktion[0] is "kaufe":
				haengeIconAnFeld( figure, position, "img/" + aktion[1] + ".svg", belegung)
			if aktion[0] is "verkaufe":
				for ware in aktion[1].waren:
					haengeIconAnFeld( figure, position, "img/" + ware + ".svg", belegung)
				

	setzeIconAufFeld( figure, (-1,4), "img/" + spiel.wetter.aktuellesWetter + ".svg" )
				
	figure.save( filename )
	return
	