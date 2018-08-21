import unittest

import Spielfeld
import Oasen

class SpielfeldTest( unittest.TestCase ):

	def test_upper(self):
		spiel = Oasen.Oasen()
		feld = Spielfeld.Spielfeld( spiel )

		self.assertEqual( feld.normaleDistanz( (2,2), (2,2) ), 0 )
		self.assertEqual( feld.normaleDistanz( (0,0), (3,0) ), 3 )
		self.assertEqual( feld.normaleDistanz( (3,0), (0,0) ), 3 )
		self.assertEqual( feld.normaleDistanz( (0,0), (1,2) ), 2 )
		self.assertEqual( feld.normaleDistanz( (0,0), (1,1) ), 2 )
		self.assertEqual( feld.normaleDistanz( (0,0), (2,1) ), 3 )
		self.assertEqual( feld.normaleDistanz( (1,2), (0,0) ), 2 )
		self.assertEqual( feld.normaleDistanz( (1,1), (0,0) ), 2 )
		self.assertEqual( feld.normaleDistanz( (2,1), (0,0) ), 3 )		
if __name__ == '__main__':
	unittest.main()
