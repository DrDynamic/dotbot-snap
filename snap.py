import subprocess
import dotbot
from typing import List, Dict


class Snap(dotbot.Plugin):
    _directive = 'snap'

    def can_handle(self, directive: str):
        return self._directive == directive

    def handle(self, directive: str, data: List):
        if directive != self._directive:
            raise ValueError('snap cannot handle directive %s' % directive)

        success = True
        defaults = self._context.defaults().get(self._directive, {})

        for item in data:
            classic = defaults.get("classic", False)
            app = None

            if isinstance(item, Dict):
                app, options = list(item.items())[0]
                if options is not None:
                    classic = options[0].get("classic", classic)
            else:
                app = item

            try:
                command = ['snap install']
                if classic:
                    command.append("--classic")
                command.append(app)
                subprocess.run([' '.join(command)], shell=True, check=True)

            except subprocess.CalledProcessError:
                success = False

        if success:
            self._log.info('All packages have been installed')
        else:
            self._log.error('Some packages were not successfully installed')
        return success
