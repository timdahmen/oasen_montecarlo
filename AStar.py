import PriorityQueue

class AStar:
	def __init__( self, spieler, spielfeld, wetter ):
		self.spieler = spieler
		self.spielfeld = spielfeld
		self.wetter = wetter
		
	def heuristic( self, a, b ):
		return self.spielfeld.hexDistanz(a,b)

	def extractPath( self, camefrom, start, goal ):
		path = []
		while goal != start:
			path.append( ( "bewege", goal ) )
			if not goal in camefrom.keys():
				return ( [], False )
			goal = camefrom[goal]
		return ( list( reversed(path) ), True )

	def erreichbareNachbarn( self, current ):
		erreichbare = []
		for bis in self.spielfeld.nachbarn( current ):
			if self.spieler.flughoehe >= self.spielfeld.hoehe( current, bis ):
				richtung = self.spielfeld.richtungZuFeld( current, bis )
				if not self.wetter.zugUngueltig( richtung ):
					erreichbare.append( bis )
		return erreichbare
		
	def search( self, start, goal ):
		frontier = PriorityQueue.PriorityQueue()
		frontier.put(start, 0)
		came_from = {}
		cost_so_far = {}
		came_from[start] = None
		cost_so_far[start] = 0
		
		while not frontier.empty():
			current = frontier.get()
			
			if current == goal:
				break
			
			for next in self.erreichbareNachbarn( current ):
				richtung = ( next[0]-current[0], next[1]-current[1] )
				richtung = self.spielfeld.offset_to_cube( richtung )
				new_cost = cost_so_far[current]
				if not self.wetter.zugGratis( richtung ):
					 new_cost += 1
				if next not in cost_so_far or new_cost < cost_so_far[next]:
					cost_so_far[next] = new_cost
					priority = new_cost + self.heuristic(goal, next)
					frontier.put(next, priority)
					came_from[next] = current
		
		( path, erfolg ) = self.extractPath( came_from, start, goal )
		return ( path, cost_so_far, erfolg )