import server
import unittest
from unittest import TestCase
#from model import db, connect_to_db, EIS_data, State, Project_State
from server import app

class TestFlaskRoutes(unittest.TestCase):

  def test_index(self):

      client = app.test_client(self)
      server.app.config['TESTING'] = True

      result = client.get('/')
      self.assertEqual(result.status_code, 200)

if __name__ == '__main__':  #pragma: no cover
    
    #runs all cases
    unittest.main() 
