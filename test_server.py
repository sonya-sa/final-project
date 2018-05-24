class MyTest(unittest.TestCase):
  def test_home(self):
      client = server.app.test_client()
      server.app.config['TESTING'] = True

      result = client.get('/')
      self.assertEqual(result.status_code, 200)
