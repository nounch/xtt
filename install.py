#!/usr/bin/env python



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
xresourcesMixin = './templates/.Xresouces.mixin.template'
# .Xresrources.styleSheetsList template
styleSheetsListTemplate ='./templates/.Xresources.styleSheetsList.template'
# .Xresrources.styleSheetsList header
styleSheetsListHeader ='./templates/.Xresources.styleSheetsListHeader.template'
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
    string = regex.search(s).group()
    return s.replace(string, string.upper(), 1)


# Add include statements to the .Xresources  template
styleSheetPathes = glob.glob(os.path.dirname(os.path.realpath(__file__)) + '/styleSheets/.*')
includeLine = '! Include %s\n#include "%s"\n\n'
aliasLine = 'alias ' + config.aliasPrefix  + '%s = "xterm -name %s"'
styleSheetNames = []


#==========================================================================
# Template generation
#==========================================================================

# Append includes to style sheets list template
with open(styleSheetsListTemplate , 'w') as resourcesTemplate:
    # Add header
    with open(styleSheetsListHeader , 'r') as headerFile:
        for line in headerFile:
            resourcesTemplate.write(line);
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
                    '.' + TEMPLATE_EXTENSION))));


#==========================================================================
# Write to user files/dirs
#==========================================================================

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
            userFile.write(line);
        userFile.write('\n')

# TODO: Write alias definitions to user's shell config file.

