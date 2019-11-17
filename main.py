'''
Created on 2019/11/17

@author: Ken
'''
import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):

        templates = {}
        self.display('メインページ','index.html',templates,1)

app = webapp2.WSGIApplication([('/',MainPage)],
                              debug=True)