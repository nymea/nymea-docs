#!/usr/bin/env python

# -*- coding: UTF-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                         #
#  Copyright (C) 2020 Simon Stuerz <simon.stuerz@nymea.io>                #
#                                                                         #
#  This file is part of nymea.                                            #
#                                                                         #
#  nymea is free software: you can redistribute it and/or modify          #
#  it under the terms of the GNU General Public License as published by   #
#  the Free Software Foundation, version 2 of the License.                #
#                                                                         #
#  nymea is distributed in the hope that it will be useful,               #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the           #
#  GNU General Public License for more details.                           #
#                                                                         #
#  You should have received a copy of the GNU General Public License      #
#  along with nymea. If not, see <http://www.gnu.org/licenses/>.          #
#                                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import argparse
import traceback
import json
import os
import sys
import subprocess
import shutil

__version__='1.0.0'


#--------------------------------------------------------------------------
def printInfo(info):
    print('[+] ' + info)


#--------------------------------------------------------------------------
def printWarning(warning):
    print('[-] Warning: ' + warning)


#--------------------------------------------------------------------------
def printError(error):
    print('[!] Error: ' + error)


#--------------------------------------------------------------------------
def writeToFile(line):
    outputFile.write('%s\n' % line)

#--------------------------------------------------------------------------
def writeCodeSection(jsonData):
    writeToFile('')
    codeContent = json.dumps(jsonData, sort_keys=True, indent=4)
    codeLines = codeContent.splitlines(True)
    finalCodeContent = ''
    for line in codeLines:
        finalCodeContent = finalCodeContent + '      ' + line

    writeToFile(finalCodeContent)
    writeToFile('')


#--------------------------------------------------------------------------
def loadJsonData(fileName):
    # Open the file
    try:
        jsonFile = open(fileName, 'r')
    except:
        printError('Could not open JSON file \"%s\"' % (fileName))
        exit(-1)

    jsonFileContent = jsonFile.read()
    jsonFile.close()

    # Parse json content
    try:
        data = json.loads(jsonFileContent)
    except ValueError as error:
        printError('Could not load json content from %s' % (fileName))
        printError('     %s' % (error))
        exit(-1)

    return data

#--------------------------------------------------------------------------
def createMarkdownLink(linkName):
    link = '#%s' % linkName.lower().replace(' ', '-')
    return link

#--------------------------------------------------------------------------
def createPluginsMarkdown(directories):
    printInfo('--> Create plugins documentation from %s' % (directories))

    if not os.path.isdir(outputDirectory + '/plugins/'):
        printInfo('--> Create output directory')
        os.mkdir(outputDirectory + '/plugins/')


    for pluginDir in directories:
        # Get json file
        pluginJsonFile = ''
        for file in os.listdir(pluginDir):
            if file.endswith(".json"):
                pluginJsonFile = file
                break

        # Get the readme file
        pluginReadmeFile = pluginDir + '/' + 'README.md'
        if not os.path.isfile(pluginReadmeFile):
            printWarning('The plugin %s has no readme file' % pluginDir)
            continue
        else:
            printInfo('Using readme file %s' % pluginReadmeFile)

        printInfo('Extract plugin information from %s' % pluginJsonFile)
        pluginJsonData = loadJsonData(pluginDir + '/' + pluginJsonFile)
        printInfo('Plugin name: %s' % pluginJsonData['displayName'])

        markdownFileName = pluginJsonData['displayName'].lower().replace(' ', '-')
        

        shutil.copyfile(pluginReadmeFile, outputDirectory + '/plugins/' + markdownFileName + '.md')
        writeToFile('* [%s](plugins/%s.md)' % (pluginJsonData['displayName'], markdownFileName))

    printInfo('nymea-plugins markdown written successfully')


###########################################################################
# Main
###########################################################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This tool generates markdown / html documentation from the plugins repository for the online documentation.')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument('-p', '--plugins', help='The path to the plugins source directory. Default is source/plugins/', metavar='path', default='source/plugins/')
    parser.add_argument('-o', '--output', help='The output directory for the resulting files. Default is output/pluigins', metavar='output', default='output/plugins')
    args = parser.parse_args()

    pluginDirectory = os.path.abspath(args.plugins)
    outputDirectory = os.path.abspath(args.output)
    nymeaPluginsMarkdown = outputDirectory + '/nymea-plugins.md'

    # Print build information for debugging
    printInfo('--> Plugin directory: %s' % pluginDirectory)
    printInfo('--> Output directory: %s' % outputDirectory)

    # Verify path
    if not os.path.isdir(pluginDirectory):
        printError('The given plugins directory path does not exist \"%s\"' % (pluginDirectory))
        exit(-1)

    # collect nymea-plugins paths
    nymeaPluginDirs = []
    nymeaPluginDir = pluginDirectory + '/nymea-plugins'
    excludeDirs = ['.git', 'debian', '.github' ]
    for pluginDir in os.listdir(nymeaPluginDir):
        if os.path.isdir(nymeaPluginDir + '/' + pluginDir) and pluginDir not in excludeDirs:
            nymeaPluginDirs.append(nymeaPluginDir + '/' + pluginDir)

    printInfo('--> Plugin directories %s' % nymeaPluginDirs)
    printInfo('--> Prepare output directory')
    if os.path.isdir(outputDirectory):
        printInfo('--> Clean up output directory')
        shutil.rmtree(outputDirectory)

    printInfo('--> Create output directory')
    os.mkdir(outputDirectory)

    # Generate nymea-plugins markdown
    try:
        outputFile = open(nymeaPluginsMarkdown, 'w')
    except:
        printError('Could not open output file \"%s\"' % (nymeaPluginsMarkdown))
        exit(-1)

    createPluginsMarkdown(nymeaPluginDirs)
    outputFile.close()
