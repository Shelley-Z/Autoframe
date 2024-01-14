import requests
import unittest



class ApiTests(unittest.TestCase):

    def test_positive_api(self):
        response = requests.get("https://gorest.co.in/public-api/users")
        self.assertEqual(response.status_code, 200)

        print(response.text)

    def test_negative_api(self):
        response = requests.get("https://gorest.co.in/public-api/nonexistent-endpoint")
        self.assertEqual(response.status_code, 404)

        print(response.text)

if __name__ == "__main__":
    unittest.main()
