#!/usr/bin/env python



import sys
import re
import os
import os.path
import glob
import shutil
import errno

import config


# Main .Xresource template
xresourcesTemplate = './templates/.Xresources.template'
# Header + non-theme resource definitions
xresourcesMixin = './templates/.Xresources.mixin.template'
# .Xresrources.styleSheetsList template
styleSheetsListTemplate = './templates/.Xresources.styleSheetsList.template'
# .Xresrources.styleSheetsList header
styleSheetsListHeader = './templates/.Xresources.styleSheetsListHeader.template'
# Shell configuration file template
shellFile = './aliases/shellFile.template'
# Header for the shell configuration file
shellFileHeader ='./aliases/shellFileHeader.template'
# Template file extension (has to be stripped before writing to the user's
# directories)
TEMPLATE_EXTENSION = 'template'
# Suffix to use for style sheets
STYLE_SHEET_SUFFIX = 'XTerm'


# Make sure the style sheets directory exists
try:
    os.makedirs(config.styleSheetsDir)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise


# Helpers
def upperFirstAlpha(string):
    regex = re.compile("[A-Za-z]")
    string = regex.search(string).group()
    return string.replace(string, string.upper(), 1)


# Add include statements to the .Xresources  template
styleSheetPathes = glob.glob(os.path.dirname(os.path.realpath(__file__)) + '/styleSheets/.*')
includeLine = '! Include %s\n#include "%s"\n\n'
aliasLine = 'alias %s = "xterm -name %s"'
styleSheetNames = []


#==========================================================================
# Template generation
#==========================================================================

def generateTemplates():

    # Append includes to style sheets list template
    with open(styleSheetsListTemplate , 'w') as resourcesTemplate:
        # Add header
        with open(styleSheetsListHeader , 'r') as headerFile:
            for line in headerFile:
                resourcesTemplate.write(line)
        # Add include statements
        for styleSheetTemplatePath in  styleSheetPathes:
            styleSheetName = os.path.basename(styleSheetTemplatePath)
            resourcesTemplate.write(
                includeLine % (styleSheetName + ' theme',
                               config.styleSheetsDir + styleSheetTemplatePath))
            # Generate list of style sheets - doing this here save another loop
            styleSheetNames.append(styleSheetName)

    # Append style sheets list include template to xresources template.
    # (This is required to be able to regenerate the list of style sheets
    # without altering the user's .Xresources file.)
    with open(xresourcesTemplate, 'w') as resourcesFileTemplate:
        with open(xresourcesMixin, 'r') as mixin:
            # Add mixin
            for line in mixin:
                resourcesFileTemplate.write(line)
        # Add include statement
        resourcesFileTemplate.write(includeLine % (
                ' all XTerm style sheets',
                config.styleSheetsDir + os.path.basename(
                    styleSheetsListTemplate.rstrip(
                        '.' + TEMPLATE_EXTENSION))))


    # Write alias definitions to shell configuration file template
    if config.generateAliases:
        with open(shellFile, 'w') as shFile:
            for name in styleSheetNames:
                # name = name.lstrip(config.styleSheetPrefix).rstrip(XTerm)
                name = re.sub(config.styleSheetPrefix,  '', name)
                name = re.sub('XTerm',  '', name)
                aliasName = ''.join([s.title() for s in  re.split('[A-Z]', name)])
                shFile.write(aliasLine % (config.aliasPrefix + aliasName, name) + '\n')

    # Merge shell configuration file header in shell configuration file
    with open(shellFileHeader, 'r') as header:
        with open(shellFile, 'a+') as shFile:
            for line in header:
                shFile.write(line)
            shFile.write('\n')


#==========================================================================
# Write to user files/dirs
#==========================================================================

def install():

    # Append style sheets list include file to user's style sheet directory.
    # This is required to be able to regenerate the list of style sheets
    # without altering the user's .Xresources file.
    with open(styleSheetsListTemplate, 'r') as listTemplate:
        with open(config.styleSheetsDir + os.path.basename(
                styleSheetsListTemplate).rstrip(TEMPLATE_EXTENSION).rstrip(
                '.'), 'w') as xres:
            for line in listTemplate:
                xres.write(line)
            xres.write('\n')

    # Copy style sheet templates to user's style sheets directory.
    for file in styleSheetPathes:
        shutil.copyfile(file, config.styleSheetsDir + os.path.basename(
                file))

    # Append configuration to the user's .Xresources file
    with open(xresourcesTemplate, 'r') as template:
        with open(config.xresources, 'a+') as userFile:
            for line in template:
                userFile.write(line)
            userFile.write('\n')

    # Write alias definitions to user's shell config file.
    with open(config.shellConfigFile, 'a+') as shFile:
        shFile.write('\n\n')
        with open(shellFile, 'r') as template:
            for line in template:
                shFile.write(line)


#==========================================================================
# Clear template files
#==========================================================================

def clear():
    cleanableFiles = [xresourcesTemplate,
                      styleSheetsListTemplate,
                      shellFile]

    for file in cleanableFiles:
        with open(file, 'w') as f:
            f.write('')

#==========================================================================
# CLI
#==========================================================================

usage = ''' Usage:

  ./install.py generate  -  Generate template files
  ./install.py install   -  Install themes
  ./install.py clear     -  Clear template files'''

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print(len(sys.argv))  # DEBUG
    print(usage)
else:
    if sys.argv[1] == 'generate':
        generateTemplates()
    elif sys.argv[1] == 'install':
        generateTemplates()
        install()
    elif sys.argv[1] == 'clear':
        clear()
    else:
        print(usage)

