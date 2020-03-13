#!/usr/bin/env python

# -*- coding: UTF-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                         #
#  Copyright (C) 2019-2020 Simon Stuerz <simon.stuerz@nymea.io>           #
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
import subprocess

__version__='1.0.0'


#--------------------------------------------------------------------------
def printInfo(info):
    print(info)


#--------------------------------------------------------------------------
def printWarning(warning):
    print('Warning: ' + warning)


#--------------------------------------------------------------------------
def printError(error):
    print('Error: ' + error)


#--------------------------------------------------------------------------
def writeToFile(line):
    outputFile.write('%s\n' % line)


#--------------------------------------------------------------------------
def createMarkdownLink(linkName):
    link = '#%s' % linkName.lower().replace(' ', '-').replace('.', '')
    return link

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
def getJsonString(object, key):
    for objectKey, value in object.items():
        if objectKey is key:
            return value

    return None


#--------------------------------------------------------------------------
def extractReferences(element):
    referenceList = []

    if isinstance(element, list):
        for item in element:
            itemString = ('%s' % item)
            if itemString.startswith('$ref:'):
                referenceList.append(itemString)

            elif isinstance(item, dict):
                referenceList.extend(extractReferences(item))

    elif isinstance(element, dict):
        for key, value in element.iteritems():
            keyString = ('%s' % key)
            if keyString.startswith('$ref:'):
                referenceList.append(keyString)

            valueString = ('%s' % value)
            if valueString.startswith('$ref:'):
                referenceList.append(valueString)

            elif isinstance(value, dict):
                referenceList.extend(extractReferences(value))

            elif isinstance(value, list):
                for item in value:
                    itemString = ('%s' % item)
                    if itemString.startswith('$ref:'):
                        referenceList.append(itemString)

                    elif isinstance(item, dict):
                        referenceList.extend(extractReferences(item))

    return referenceList


#--------------------------------------------------------------------------
def createReferenceLine(item):
    # Get list of all references
    referenceList = []
    fullReferenceList = extractReferences(item)
    for reference in fullReferenceList:
       if reference not in referenceList:
           referenceList.append(reference.replace('$ref:', ''))

    if not referenceList:
        return ""

    # Write references from content
    referencesString = "See also: "
    referenceCount = len(referenceList)
    for i in range(len(referenceList)):
        if i is referenceCount - 1:
            referencesString += '[%s](%s)' % (referenceList[i], createMarkdownLink(referenceList[i]))
        else:
            referencesString += '[%s](%s), ' % (referenceList[i], createMarkdownLink(referenceList[i]))

    return referencesString

#--------------------------------------------------------------------------
def extractDeprecates(element):
    deprecatedList = []
    if isinstance(element, list):
        for item in element:
            itemString = ('%s' % item)
            if itemString.startswith('d:'):
                deprecatedList.append(itemString)

            elif isinstance(item, dict):
                deprecatedList.extend(extractDeprecates(item))

    elif isinstance(element, dict):
        for key, value in element.iteritems():
            keyString = ('%s' % key)
            if keyString.startswith('d:'):
                deprecatedList.append(keyString)

            valueString = ('%s' % value)
            if valueString.startswith('d:'):
                deprecatedList.append(valueString)

            elif isinstance(value, dict):
                deprecatedList.extend(extractDeprecates(value))

            elif isinstance(value, list):
                for item in value:
                    itemString = ('%s' % item)
                    if itemString.startswith('d:'):
                        deprecatedList.append(itemString)

                    elif isinstance(item, dict):
                        deprecatedList.extend(extractDeprecates(item))

    return deprecatedList


#--------------------------------------------------------------------------
def createDeprecatedWarning(item):
    # Get list of all references
    deprecatedList = []
    fullDeprecatedList = extractDeprecates(item)
    for deprecated in fullDeprecatedList:
       if deprecated not in deprecatedList:
           deprecatedList.append(deprecated.replace('d:', ''))

    if not deprecatedList:
        return ""

    # Write references from content
    deprecatedString = "> **Warning**: following values are deprecated and will be removed with the next major API version: "
    deprecatedCount = len(deprecatedList)
    for i in range(len(deprecatedList)):
        if i is deprecatedCount - 1:
            deprecatedString += '`%s`' % deprecatedList[i]
        else:
            deprecatedString += '`%s`, ' % deprecatedList[i]

    return deprecatedString


#--------------------------------------------------------------------------
def extractEnums(enums):
    enumList = []
    for enum in enums:
        enumList.append(enum)

    enumSorted = sorted(enumList)
    for enum in enumSorted:
        writeToFile(' * [%s](%s)' % (enum, createMarkdownLink(enum)))

    for enum in enumSorted:
        writeToFile('------------------------------')
        writeToFile('#### %s' % enum)
        writeCodeSection(enums[enum])
        writeToFile(createReferenceLine(enums[enum]))
        writeToFile('')


#--------------------------------------------------------------------------
def extractTypes(types):
    typesList = []
    for type in types:
        typesList.append(type)

    typesSorted = sorted(typesList)
    for type in typesSorted:
        writeToFile(' * [%s](%s)' % (type, createMarkdownLink(type)))

    for type in typesSorted:
        writeToFile('------------------------------')
        writeToFile('##### %s' % type)
        writeCodeSection(types[type])
        deprecatedWarning = createDeprecatedWarning(types[type])
        if deprecatedWarning:
            writeToFile(deprecatedWarning)
            writeToFile('')

        writeToFile(createReferenceLine(types[type]))
        writeToFile('')



#--------------------------------------------------------------------------
def extractFlags(flags):
    flagList = []
    for flag in flags:
        flagList.append(flag)


    flagSorted = sorted(flagList)
    for flag in flagSorted:
        writeToFile(' * [%s](%s)' % (flag, createMarkdownLink(flag)))

    for flag in flagSorted:
        writeToFile('------------------------------')
        writeToFile('##### %s' % flag)
        writeToFile('')
        writeCodeSection(flags[flag])
        writeToFile('')
        writeToFile(createReferenceLine(flags[flag]))
        writeToFile('')


#--------------------------------------------------------------------------
def extractMethods(methods):
    methodsList = []
    for method in methods:
        methodsList.append(method)

    methodsSorted = sorted(methodsList)
    for method in methodsSorted:
        writeToFile(' * [%s](%s)' % (method, createMarkdownLink(method)))

    for method in methodsSorted:
        writeToFile('------------------------------')
        writeToFile('##### **%s**' % method)
        writeToFile('')
        description = methods[method]['description']
        descriptionTokens = description.split('\n')
        for token in descriptionTokens:
            writeToFile('%s' % token)
            writeToFile('')
            writeToFile('')

        writeToFile('')
        if 'deprecated' in methods[method]:
            writeToFile("> **Warning**: this method is deprecated. %s" % methods[method]['deprecated'])

        writeToFile('')
        writeToFile('*Params*')
        writeToFile('')
        writeCodeSection(methods[method]['params'])
        writeToFile('')
        writeToFile('*Returns*')
        writeToFile('')
        writeCodeSection(methods[method]['returns'])
        writeToFile('')
        deprecatedWarning = createDeprecatedWarning(methods[method])
        if deprecatedWarning:
            writeToFile(deprecatedWarning)
            writeToFile('')

        writeToFile(createReferenceLine(methods[method]))
        writeToFile('')


#--------------------------------------------------------------------------
def extractNotifications(notifications):
    notificationsList = []
    for notification in notifications:
        notificationsList.append(notification)

    notificationsSorted = sorted(notificationsList)
    for notification in notificationsSorted:
        writeToFile(' * [%s](%s)' % (notification, createMarkdownLink(notification)))

    for notification in notificationsSorted:
        writeToFile('------------------------------')
        writeToFile('##### %s' % notification)
        writeToFile('')
        writeToFile('%s' % notifications[notification]['description'])
        writeToFile('')
        if 'deprecated' in notifications[notification]:
            writeToFile("> **Warning**: this notification is deprecated. %s" % notifications[notification]['deprecated'])

        writeToFile('')
        writeToFile('*Params*')
        writeToFile('')
        writeCodeSection(notifications[notification]['params'])
        deprecatedWarning = createDeprecatedWarning(notifications[notification])
        if deprecatedWarning:
            writeToFile(deprecatedWarning)
            writeToFile('')

        writeToFile(createReferenceLine(notifications[notification]))
        writeToFile('')


#--------------------------------------------------------------------------
def writeDocumentationContent(apiVersion, apiJson):
    printInfo('--> Write API documentation content')
    printInfo('--> API version: \"%s\"' % (version))

    writeToFile('')
    writeToFile('In the following section you can find a detailed description of the current API version **%s**.' % apiVersion)
    writeToFile('')
    writeToFile(' * [Enums](#enums)')
    writeToFile(' * [Flags](#flags)')
    writeToFile(' * [Types](#types)')
    writeToFile(' * [Methods](#methods)')
    writeToFile(' * [Notifications](#notifications)')
    writeToFile('')
    writeToFile('')

    if 'enums' in apiJson:
        writeToFile('------------------------------')
        writeToFile('### Enums')
        writeToFile('')
        extractEnums(apiJson['enums'])

    if 'flags' in apiJson:
        writeToFile('------------------------------')
        writeToFile('### Flags')
        writeToFile('')
        extractFlags(apiJson['flags'])

    if 'types' in apiJson:
        writeToFile('------------------------------')
        writeToFile('### Types')
        writeToFile('')
        extractTypes(apiJson['types'])

    if 'methods' in apiJson:
        writeToFile('------------------------------')
        writeToFile('### Methods')
        writeToFile('')
        extractMethods(apiJson['methods'])

    if 'notifications' in apiJson:
        writeToFile('------------------------------')
        writeToFile("### Notifications")
        extractNotifications(apiJson['notifications'])

    writeToFile('')
    writeToFile("## Full introspect")
    writeToFile('')
    writeCodeSection(apiJson)
    writeToFile('')


###########################################################################
# Main
###########################################################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This tool generates a qdoc file out of the api.json file for the online documentation.')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument('-j', '--jsonfile', help='The API JSON input file name with the JSON RPC api definition', metavar='jsonfile', default='../tests/auto/api.json')
    parser.add_argument('-o', '--output', help='The qdoc outputFile with the generated documentation script', metavar='output', default='./jsonrpc-api.qdoc')
    args = parser.parse_args()

    # Print build information for debugging
    printInfo('Json file: %s' % (args.jsonfile))
    printInfo('Output: %s' % (args.output))

    # Open API file for reading
    try:
        inputFile = open(args.jsonfile, 'r')
    except:
        printError('Could not open input file \"%s\"' % (args.jsonfile))
        exit -1

    # Open qdoc file for writing
    try:
        outputFile = open(args.output, 'w')
    except:
        printError('Could not open output file \"%s\"' % (args.output))
        exit -1

    # Read version line and create json content of the rest
    inputFileContent = inputFile.read().splitlines(True)
    inputFile.close()

    # Parse verion and json data
    version = inputFileContent[0].strip()
    jsonRawContent = ''
    for line in inputFileContent[1:]:
        jsonRawContent += line

    # Parse json content
    try:
        apiJson = json.loads(jsonRawContent)
    except ValueError as error:
        printError(' --> Could not load json content')
        printError('     %s' % (error))
        exit -1

    # Sort alphabetically
    apiJsonSortedRaw = json.dumps(apiJson, sort_keys=True, indent=4)
    apiJsonSorted = json.loads(apiJsonSortedRaw)
    writeDocumentationContent(version, apiJsonSorted)
