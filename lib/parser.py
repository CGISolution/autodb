from cement.core import controller
from pprint import pprint
import json

class parser(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'parser'
        description = 'Parses Database JSON schemas'

    def default(self):
        #intialize parser
        pass

    def loadJson(self):
        
        with open('db.json', 'r') as jraw:
            data = json.load(jraw)
        jraw.close()

        print data['name']
        return True

    @controller.expose(help='Builds Database from JSON script')
    def build(self):
        print "Building Database"

        self.loadJson()
