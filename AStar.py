import PriorityQueue

class AStar:
	def __init__( self, spieler, spielfeld ):
		self.spieler = spieler
		self.spielfeld = spielfeld
		
	def heuristic( self, a, b ):
		return self.spielfeld.hexDistanz(a,b)

	def extractPath( self, camefrom, start, goal ):
		path = []
		while goal != start:
			path.append( ( "bewege", goal ) )
			goal = camefrom[goal]
		return list( reversed(path) )

	def erreichbareNachbarn( self, current ):
		erreichbare = []
		for bis in self.spielfeld.nachbarn( current ):
			if self.spieler.flughoehe >= self.spielfeld.hoehe( current, bis ):
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
				new_cost = cost_so_far[current] + 1
				if next not in cost_so_far or new_cost < cost_so_far[next]:
					cost_so_far[next] = new_cost
					priority = new_cost + self.heuristic(goal, next)
					frontier.put(next, priority)
					came_from[next] = current
		
		return self.extractPath( came_from, start, goal ), cost_so_far