import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(u'Hello, 147!蛋黄叫你回家吃饭')
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

