from cement.core import backend, foundation, hook
from cement.utils.misc import init_defaults

from lib import baseController

app = foundation.CementApp('autodb', base_controller=baseController)

hook.define('app_hook')

def test(app):
    print "Application: %s" % app.name

hook.register('app_hook', test, weight=0)

try:
    app.setup()

    #add args
    #app.args.add_argument('-v', '--version', action='store_true', dest='printversion', help='Application Version')

    app.run()
    print "hey"
    #if app.pargs.printversion:
    #    print "Version %s" % defaults['autodb']['version']
finally:
    app.close()
