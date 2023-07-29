import subprocess
import dotbot
from typing import List, Dict, Union


class Snap(dotbot.Plugin):
    _directive = 'snap'

    def can_handle(self, directive: str):
        return self._directive == directive

    def handle(self, directive: str, data: Union[List, Dict]):
        if directive != self._directive:
            raise ValueError('snap cannot handle directive %s' % directive)

        success = True
        defaults = self._context.defaults().get(self._directive, {})

        if isinstance(data, Dict):
            data = [{key: data[key]} if bool(data[key]) else key
                    for key in data]

        for item in data:
            classic = defaults.get("classic", False)
            channel = defaults.get("channel", "latest/stable")
            app = None

            if isinstance(item, Dict):
                app, options = list(item.items())[0]
                if options is not None:
                    classic = options.get("classic", classic)
                    channel = options.get("channel", channel)
            else:
                app = item

            try:
                command = ['snap install']

                if classic:
                    command.append("--classic")
                if channel:
                    command.append("--channel='%s'" % channel)

                command.append(app)
                self._log.debug('Using command: %s' % command)

                subprocess.run([' '.join(command)], shell=True, check=True)
            except subprocess.CalledProcessError:
                success = False

        if success:
            self._log.info('All packages have been installed')
        else:
            self._log.error('Some packages were not successfully installed')
        return success
