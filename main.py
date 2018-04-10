import webapp2
import matplotlib.pyplot as plt
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Try again!')
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

