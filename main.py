import webapp2
import networkx as nx
G = nx.fast_gnp_random_graph(100,10)
n = G.number_of_nodes()
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(str(n))
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

