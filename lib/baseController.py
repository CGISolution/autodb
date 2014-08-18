from cement.core import handler,hook, controller
class baseController(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'base'
        description = 'Database Automation'

        config_defaults = {}
        arguments = []

    @controller.expose(hide=True, aliases=['run'])
    def default(self):
        print "default function"
        #for res in hook.run('autodb_default_command_hook', self.app):
        #    pass
