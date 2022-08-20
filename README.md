[dotbot_repo]: https://github.com/anishathalye/dotbot

## Dotbot ```snap``` Plugin

Plugin for [Dotbot][dotbot_repo], that adds ```snap``` directive, which allows you to install snap packages 

## Installation

1. Simply add this repo as a submodule of your dotfiles repository:
```
git submodule add https://github.com/DrDynamic/dotbot-snap.git
```

2. Pass this folder (or directly snap.py file) path with corresponding flag to your [Dotbot][dotbot_repo] script:
  - ```-p /path/to/file/snap.py```

  or

 - ```--plugin-dir /pato/to/plugin/folder```

## Supported task variants
```yaml
...
- snap: 
    - app 1
    - app 2
    - app 3:
        classic: true
    ...
```

| Parameter | Explanation |
| --- | --- |
| `classic` | Installs snap in classic mode, with `--classic` flag. Required for some snaps published using classic confinement, which would otherwise throw an error. (default: false) |

## Usage

### Example config
```yaml
- defaults:
    snap:
      classic: false # default
...
- snap:
    - bpytop
    - chromium
    - mailspring
    - node:
        classic: true
    ...
...
```

### Execution
```bash
"~/.dotfiles/bin/dotbot" -d "~/.dotfiles" -c "~/.dotfiles/packages.yaml" -p "~/.dotfiles/plugins/dotbot-snap/snap.py"
```
