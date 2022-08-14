import subprocess, dotbot

class Snap(dotbot.Plugin):
    _directive = 'snap'


    def can_handle(self, directive):
        return self._directive == directive

    def handle(self, directive, data):
        if directive != self._directive:
            raise ValueError('snap cannot handle directive %s' %
                directive)
        
        success = True
        classic = False

        for app, options in data.items():
            if isinstance(options, dict):
                classic = options.get("classic", classic)
            
            try:
                command = ['snap install']
                if classic:
                    command.append("--classic")
                command.append(app)

                subprocess.run(
                        [' '.join(command)], 
                        shell=True, 
                        check=True)
            except subprocess.CalledProcessError:
                success = False

        if success:
            self._log.info('All packages have been installed')
        else:
            self._log.error('Some packages were not successfully installed')
        return success
