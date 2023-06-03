import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      dataPoint = getDataPoint(quote)
      self.assertEqual(dataPoint, (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2.0))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2.0))



  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    quotes_1 = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    quotes_2 = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 120.48, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 119.2, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    price_a1 = (quotes_1[0]['top_ask']['price'] + quotes_1[0]['top_bid']['price']) / 2.0
    price_a2 = (quotes_1[1]['top_ask']['price'] + quotes_1[1]['top_bid']['price']) / 2.0
    self.assertEqual(getRatio(price_a1, price_a2), price_a1 / price_a2)

    price_b1 = (quotes_2[0]['top_ask']['price'] + quotes_2[0]['top_bid']['price']) / 2.0
    price_b2 = (quotes_2[1]['top_ask']['price'] + quotes_2[1]['top_bid']['price']) / 2.0
    self.assertEqual(getRatio(price_b1, price_b2), 1.0)



if __name__ == '__main__':
    unittest.main()
