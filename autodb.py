from cement.core import backend, foundation, hook, handler
from cement.utils.misc import init_defaults

from lib import baseController, parser

import sys

try:
    app = foundation.CementApp('autodb')

    handler.register(baseController.baseController)
    handler.register(parser.parser)

    app.setup()

    #add args
    #app.args.add_argument('-v', '--version', action='store_true', dest='printversion', help='Application Version')

    app.run()

finally:
    app.close()
