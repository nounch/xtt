#!/usr/bin/env python



import re
import os
import os.path
import glob
import shutil
import errno

import config


xresourcesTemplate = './templates/.Xresources.template'
styleSheetsListTemplate ='./templates/styleSheets/.Xresources.styleSheetsList.template'
TEMPLATE_EXTENSION = 'template'
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
styleSheetTemplatePathes = glob.glob('./templates/styleSheets/*')
includeLine = 'Include %s\n#include "%s"'
aliasLine = 'alias ' + config.aliasPrefix  + '%s = "xterm -name %s"'
styleSheetNames = []


#==========================================================================
# Template generation
#==========================================================================

# Append includes to style sheets list template
with open(styleSheetsListTemplate , 'a+') as resourcesTemplate:
    for styleSheetTemplatePath in  styleSheetTemplatePathes:
        styleSheetName = os.path.basename(styleSheetTemplatePath)
        resourcesTemplate.write(
            includeLine % (styleSheetName + ' theme',
                           config.styleSheetsDir + styleSheetTemplatePath))
        # Doing this here save another loop
        styleSheetNames.append(styleSheetName)

# Append style sheets list include template to xresources template.
# (This is required to be able to regenerate the list of style sheets
# without altering the user's .Xresources file.)
with open(xresourcesTemplate, 'r') as resourcesFileTemplate:
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
    with open(conf.styleSheetsDir + os.path.basename(
            styleSheetsListTemplate).rstrip(
            '.' + TEMPLATE_EXTENSION), 'a+') as list:
        for line in list:
            xres.write(line)
        xres.write('\n')

# Copy style sheet templates to user's style sheets directory.
for file in styleSheetTemplatePathes:
    shutil.copyfile(file, config.styleSheetsDir + os.path.basename(
            file).rstrip(TEMPLATE_EXTENSION))

# Copy style sheets list template to user's style sheets directory.
shutil.copyfile(
    styleSheetsListTemplate,
    config.styleSheetsDir + os.path.basename(styleSheetsListTemplate))

# Append configuration to the user's .Xresources file
with open(xresourcesTemplate, 'r') as template:
    with open(config.xresources, 'a+') as userFile:
        for line in template:
            userFile.write(line);
        userFile.write('\n')

