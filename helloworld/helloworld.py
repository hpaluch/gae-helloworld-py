from datetime import datetime
print 'Content-Type: text/plain'
print ''
print 'Hello, world!'
print 'Now is: '+datetime.now().strftime("%d.%m.%Y %H:%M:%S")
print
