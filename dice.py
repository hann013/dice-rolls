import webapp2
import random

rolls = 0

css = "<link href='http://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet' type='text/css'> <link href='http://fonts.googleapis.com/css?family=Maven+Pro' rel='stylesheet' type='text/css'> <style> body { background-image: url('/img/background.jpg'); background-size: cover; font-family: 'Maven Pro', sans-serif; font-size: 15pt; text-align: center; text-shadow: -2px 0 black, 0 2px black, 2px 0 black, 0 -2px black; color: white; } h1.header { font-family: 'Montserrat', sans-serif; font-weight: 700; font-size: 40pt; color: white; } span { font-size: 20pt; font-weight: 700; color: yellow; } </style>"
header = '<title>Dice Roll Generator</title><h1 class="header">Dice Roll Generator</h1>'

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(css)
        self.response.out.write(header + 
            '<img src="http://4.bp.blogspot.com/-xFKg63rUjqY/U3MgB8_2TbI/AAAAAAAABj0/bsONym-FvVA/s1600/Six+faces+of+a+dice.JPG" width=487 height=82>' + 
            '<br><br>' + 
            '<form id="diceForm" onsubmit="checkNumber(event)" action="/check" method="get">' +
                '<div>Number of dice rolls: <input id="numRolls" type="text" name="rolls"></div><br>' + 
                '<div><input type="submit" value="Submit"></div>' + 
            '</form>' + 
            '<div id="errorMessage" style="display: none;">Please enter a valid integer!</div>' +
            '<script>' + 
                'function checkNumber(event) {' +
                    'event.preventDefault();' +
                    'var input = document.getElementById("numRolls").value;' +
                    'if (parseInt(input)) {' +
                        'document.getElementById("diceForm").submit();' + 
                    '} ' + 
                    'else {' +
                        'document.getElementById("errorMessage").style.display = "block";' +
                    '}' +
                '}' +
            '</script>')

class CheckHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(css)
        
        rolls = self.request.get("rolls")
        if len(str(rolls)) == 0:
            rolls = 0
        else:
            rolls = int(rolls)

        roll1 = 0
        roll2 = 0
        rollCount = 1

        self.response.out.write(header)

        if rolls == 0:
            self.response.out.write('<p>No dice rolls!</p>')
        else:
            while rollCount < rolls+1: 
                roll1 = random.randint(1, 6)
                roll2 = random.randint(1, 6)
                self.response.out.write('<span>Roll #' + str(rollCount) + ': <img src="img/' + str(roll1) + '.png" width=50 height=50>' + '<img src="img/' + str(roll2) + '.png" width=50 height=50><br></span>') 
                rollCount += 1

                if roll1 == 6 and roll2 == 6:
                    self.response.out.write('(Double sixes!)<br>')
                if roll1 == 1 and roll2 == 1:
                    self.response.out.write('(Snake eyes!)<br>')

routes = [
    ('/', MainHandler),
    ('/check', CheckHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)