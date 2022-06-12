import unittest
from pubsub import (
	PubSub,
	Callback,
	Channel
)

class SubscriberA:

	def subscribe_handler(self, payload: dict, callback: Callback = None):
		print("called from subscribe_handler", payload)
		callback(payload)
		return None

class TestPubSub(unittest.TestCase):

	def test_can_register_a_subscriber(self):
		ch = Channel.with_name("abcd")
		def callback(payload: dict):
			print("called from callback", payload)
			self.assertEqual(payload["test"], "this is a test")

		pubsub = PubSub()
		pubsub.create_channel(ch)
		pubsub.subscribe(ch, SubscriberA())
		pubsub.publish(ch, {"test": "this is a test"}, callback)


if __name__ == "__main__":
    unittest.main()