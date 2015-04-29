__author__ = 'wthongthai'

import cgi
import webapp2

form="""
<form method='post'>
  Enter Message
  <br>
  <textarea name='area' rows='4' cols='50'>%(message)s</textarea>
  <br>
  <input type='submit'>
</form>
"""

class MainPage(webapp2.RequestHandler):
  def write_form(self, message=""):
    self.response.out.write(form % {'message': esc(message)})

  def get(self):
    self.write_form()

  def post(self):
    message = self.request.get('area')
    coded_message = rot13(message)
    self.write_form(coded_message)

class MessageHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("ROT13!")

application = webapp2.WSGIApplication(
  [('/', MainPage), 
  ('/message', MessageHandler)],
  debug = True)


def esc(s):
    return cgi.escape(s, quote=True)

def rot13(s):
    # rot13("helloy") --> "h"
    letters = {"a" : "n",
               "b" : "o",
               "c" : "p",
               "d" : "q",
               "e" : "r",
               "f" : "s",
               "g" : "t",
               "h" : "u",
               "i" : "v",
               "j" : "w",
               "k" : "x",
               "l" : "y",
               "m" : "z",
               "n" : "a",
               "o" : "b",
               "p" : "c",
               "q" : "d",
               "r" : "e",
               "s" : "f",
               "t" : "g",
               "u" : "h",
               "v" : "i",
               "w" : "j",
               "x" : "k",
               "y" : "l",
               "z" : "m",}

    output = ""
    for i in range(len(s)):
        if s[i] not in letters:
            if s[i] == s[i].upper() and s[i].isalpha():
                output = output + letters[s[i].lower()].upper()
            else:
                output = output + s[i]
        else:
            output = output + letters[s[i]]
    return output






