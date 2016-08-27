#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from caesar import encrypt

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>

"""
edit_header = "<h3>Tricky Sneakies</h3>"

#a form for user input
add_form = """
<form action="/rotate" method="post">
    <label>
        I want to rotate my text by
        <input type="number" name="rotation"/>
        letters.
    </label>
    <br>
    <textarea name="textbox" value=" "
        style="height: 100px; width: 400px;">{0}</textarea>
    <br>
    <input type="submit" value="Go Go Gadget"/>
</form>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""
class Index(webapp2.RequestHandler):

    def get(self):
        add_clear_form= add_form.format("")
        response = page_header + edit_header + add_clear_form + page_footer
        self.response.out.write(response)
class EncryptText(Index):


    def post(self):
        # look inside the request to figure out what the user typed
        user_text = self.request.get("textbox")
        user_rotation=int(self.request.get("rotation"))
        ciphered_text= encrypt(user_text, user_rotation)
        self.response.out.write(edit_header + add_form.format(ciphered_text))




app = webapp2.WSGIApplication([
    ('/', Index),
    ('/rotate', EncryptText)

], debug=True)
