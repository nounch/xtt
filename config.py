import os.path


#==========================================================================
# Configuration
#==========================================================================

userHome = os.path.expanduser('~')


# Main X resources file
xresources = userHome + '/.Xresrouces'

# Directory for style sheets
styleSheetsDir = userHome + '/.styleSheets/xtermStyleSheets/'

# Shell configuration file (at least supported shells: bash, zsh, ksh)
shellConfigFile = userHome + '/.bashrc'

# Specifies whether aliases should be created
generateAliases = True

# Prefix for aliases - Alias examples: `xtermSolarizedBright'
# `xterm' is the prefix, `SolarizedBright' is the style sheet name
aliasPrefix = 'xterm'

# Prefix for style sheets (Do not change this, if possible.)
styleSheetPrefix = '.Xresources.'

