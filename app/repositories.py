
class Counter:
    def __init__(self):
        self.id = 0

    def next(self):
        self.id += 1
        return self.id


class TweetRepository:
    def __init__(self):
        self.clear()

    def add(self, tweet):
        tweet.id = self.id.next()
        self.tweets[tweet.id] = tweet

    def get(self, id):
        if id not in self.tweets:
            return None
        return self.tweets[id]

    def clear(self):
      self.tweets = {}
      self.id = Counter()
