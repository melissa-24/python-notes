import random
import time

class Server:
    # url -> response
    cache = {}

    def processGETRequest(self, url):
        if url in self.cache:
            print(url + ' is already in the cache')
            return self.cache[url]
        print(url + ' is not cached yet. Computing...')
        self.cache[url] = self.doExpensiveComputation(url)
        print('caching ' + url + ' with value ' + str(self.cache[url]))
        return self.cache[url]

    def processPUTRequest(self, url):
        # update DB with new values
        # evict url from the cache

    def doExpensiveComputation(self, url):
        time.sleep(5)
        return random.randint(0, 101)


server = Server()
server.processGETRequest("google.com")
server.processGETRequest("google.com")
server.processGETRequest("facebook.com")