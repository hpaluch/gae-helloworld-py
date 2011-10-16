#
# Hello World example. Warning! It does not work on GAE SDK 1.5.5 or lower
#
# system imports
from datetime import datetime
import platform
import threading
# GAE imports
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
	content = 'Hello, world! (for Python2.7/threads)\n'
        content += 'Now is: %s\n\n' % (datetime.now().strftime("%d.%m.%Y %H:%M:%S"),)
        content += 'Python version: %s\n' % (platform.python_version(),)
        content += 'Thread count: %d\n' % (threading.active_count(),)
        content += 'This thread ident: %d\n' % (threading.current_thread().ident,)
       
        self.response.out.write(content)

app = webapp2.WSGIApplication(
               [('/', MainPage)],
               debug=True)

