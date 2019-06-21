#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                         #
#  Copyright (C) 2019 Simon Stuerz <simon.stuerz@nymea.io>                #
#                                                                         #
#  This file is part of nymea-docs.                                       #
#                                                                         #
#  This program is free software; you can redistribute it and/or          #
#  modify it under the terms of the GNU General Public License            #
#  as published by the Free Software Foundation; either version 2         #
#  of the License, or (at your option) any later version.                 #
#                                                                         #
#  This program is distributed in the hope that it will be useful,        #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#  GNU General Public License for more details.                           #
#                                                                         #
#  You should have received a copy of the GNU General Public License      #
#  along with guh. If not, see <http://www.gnu.org/licenses/>.            #
#                                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import re
import sys
import argparse
import traceback
import subprocess
from bs4 import BeautifulSoup
from bs4 import Comment

__version__='1.0.0'

#--------------------------------------------------------------------------
def printInfo(info):
    print('\033[1;32m%s\033[0m' % info)


#--------------------------------------------------------------------------
def printWarning(warning):
    print('\033[1;33m%s\033[0m' % warning)


#--------------------------------------------------------------------------
def printError(error):
    print('\033[1;31m%s\033[0m' % error)


#--------------------------------------------------------------------------
def loadFileToSoap(inputFileName):
    inputFile = open(inputFileName, 'r')
    inputSoup = BeautifulSoup(inputFile.read(), 'html.parser')
    inputFile.close()
    return inputSoup
    
#--------------------------------------------------------------------------
def saveXmlToFile(page, outputFileName):
    printInfo('Write xml document to %s' % outputFileName)
    outputFile = open(outputFileName, 'w')
    outputFile.write(page.prettify(formatter="html5"))
    outputFile.close()    

#--------------------------------------------------------------------------
def extractHtmlBody(inputFileName):
    printInfo('Extract body from %s' % inputFileName)
    inputSoup = loadFileToSoap(inputFileName)
    return inputSoup.body

#--------------------------------------------------------------------------
def createHtmlReferenceFromString(reference):
    validCharacters = "abcdefghijklmnopqrstuvwxyz-"
    result = ''
    titleReference = reference.lower().replace(' ', '-')
    for character in titleReference:
        if character in validCharacters:
            result += character
    
    return result

#--------------------------------------------------------------------------
def generatePage(body):
    # Load default html parts
    head = loadFileToSoap(os.path.dirname(os.path.realpath(sys.argv[0])) + '/html-templates/head')
    header = loadFileToSoap(os.path.dirname(os.path.realpath(sys.argv[0])) + '/html-templates/header')
    footer = loadFileToSoap(os.path.dirname(os.path.realpath(sys.argv[0])) + '/html-templates/footer')

    # Create the new page
    page = BeautifulSoup('<!DOCTYPE html><html lang="en-US"></html>', 'html.parser')
    page.insert(1, Comment("Automatically created using nymea-doc tools. See https://nymea.io for more information."))
    page.html.append(head)
    
    # Create body tag
    bodyTag = page.new_tag('body')
    bodyTag.append(header)
    
    for bodyChild in body.contents:
        if (bodyChild.name == None):
            continue
        
        # Note: the body tag does not allow the li tag as child
        if bodyChild.name == 'li':
            continue
            
        bodyTag.append(bodyChild)
    
    # Append the footer at the end of the body
    bodyTag.append(footer)
    
    # Finalls insert the new body into the page and save the file
    page.html.append(bodyTag)
    return page
    

#--------------------------------------------------------------------------
def buildNymeaPluginsDocumentation():
    pluginDirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + '/source/nymea-plugins/'
    printInfo('Build nymea plugins documentations %s' % pluginDirectory)
    
    pluginDirs = []
    excludeDirs = ['.git', 'debian' ]
    
    for pluginDir in os.listdir(pluginDirectory):
        if os.path.isdir(pluginDirectory + pluginDir) and pluginDir not in excludeDirs:
            pluginDirs.append(pluginDir)
        
    # Iterate plugin directories and generate html from markdown
    for pluginDir in pluginDirs:
        if 'README.md' in os.listdir(pluginDirectory + pluginDir):
            pluginReadmeFile = pluginDirectory + pluginDir + "/README.md"
            print('Process %s' % pluginReadmeFile)
            htmlResult = subprocess.run(['markdown', pluginReadmeFile], stdout=subprocess.PIPE)
            pluginSoup = BeautifulSoup(htmlResult.stdout, 'html.parser')
                        
            # Generate contents and place the reference into the header of h2
            contentsString = ''
            headers = pluginSoup.find_all('h2')
            for header in headers:
                headerReference = createHtmlReferenceFromString(header.text)
                print(header, headerReference)
                header['id'] = headerReference
                contentsString += '<li class="level1"><a href="#%s">%s</a></li>' % (headerReference, header.text)
                
            # Build main content div
            tocDiv = BeautifulSoup('<div class="toc"><h3><a name="toc">Contents</a></h3><ul>%s</ul> </div>' % contentsString, 'html.parser')
            sidebarDiv = BeautifulSoup('<div class="sidebar">%s</div>' % tocDiv.prettify(), 'html.parser')
            contextDiv = BeautifulSoup('<div class="context">%s</div>' % pluginSoup.prettify(), 'html.parser')
            mainContentDiv = BeautifulSoup('<div class="content mainContent">%s%s</div>' % (sidebarDiv.prettify(), contextDiv.prettify()), 'html.parser')
            
            print(mainContentDiv.prettify())

            page = generatePage(mainContentDiv)
            saveXmlToFile(page, os.path.dirname(os.path.realpath(sys.argv[0])) + '/output/nymea-plugins/plugin-' + pluginDir + '.html')


    
#--------------------------------------------------------------------------
def buildHtmlFromQdocBody(inputFileName, outputFileName):
    printInfo('Building html from qdoc body')

    page = generatePage(extractHtmlBody(inputFileName))
    saveXmlToFile(page, outputFileName)
    

        
###########################################################################
# Main
###########################################################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This tool provides different help methods for building docs and handling content.')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument('-i', '--input-file', help='The name of the input file to process rellative to this tool path.', metavar='file')
    parser.add_argument('-o', '--output-file', help='The name of the output file', metavar='file', default='')
    parser.add_argument('-q', '--build-qdoc-html', help='Build a html site using the body from the give qdoc generated input file and save it to the output file.', action='store_true')
    parser.add_argument('-p', '--build-plugins-documentation', help='Build the plugins documentation located in /source/nymea-plugins.', action='store_true')

    args = parser.parse_args()

    inputFileName = args.input_file
    outputFileName = args.output_file
   
    # Build html using qdoc input file body and save to output file
    if args.build_qdoc_html:
        if not args.output_file:
            printError('No output file specified. Please specify the output file name using "-o", "--output-file"')
            exit(1)
            
        buildHtmlFromQdocBody(inputFileName, outputFileName)
    
    # Build nymea plugins documentation
    if args.build_plugins_documentation:
        buildNymeaPluginsDocumentation()
    
            
    
