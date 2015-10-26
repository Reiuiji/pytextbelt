#TextBelt python Wrapper
import urllib      # URL functions
import urllib2     # URL functions

url = "http://textbelt.com/text"

class textbelt(object):

    def send(self, number=None, message=None):
        val = { 'number'     : number,
                'message'    : message }
        postdata = urllib.urlencode(val)
        req = urllib2.Request(url, postdata)
        try:
            response = urllib2.urlopen(req)
            message = response.read()
            return message
        except URLError as e:
            print e.reason
