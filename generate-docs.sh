#!/bin/bash

CURRENT_DIR=$(pwd)
SOURCE_DIR=${CURRENT_DIR}/source
OUTPUT_DIR=${CURRENT_DIR}/output
CONFIG_DIR=${CURRENT_DIR}/qdoc-configs
TEMPLATE_DIR=${CURRENT_DIR}/html-templates

function printGreen() {
    echo -e "\e[1;32m[+] $1\e[0m"
}

function printRed() {
    echo -e "\e[1;31m[!] $1\e[0m"
}

function create-nymea-docs() {
    printGreen "Clean nymea"
    if [ -d ${SOURCE_DIR}/nymea ]; then rm -rf ${SOURCE_DIR}/nymea; fi
    if [ -d ${OUTPUT_DIR}/nymea ]; then rm -rf ${OUTPUT_DIR}/nymea; fi
    if [ -d ${OUTPUT_DIR}/nymea-raw ]; then rm -rf ${OUTPUT_DIR}/nymea-raw; fi
    mkdir -p ${OUTPUT_DIR}/nymea
    mkdir -p ${SOURCE_DIR} || true

    cd ${SOURCE_DIR}
    git clone --depth 1 https://github.com/guh/nymea.git

    printGreen "Prepare nymea docs"
    cd ${SOURCE_DIR}/nymea/doc
    python generate-interfaces-qdoc.py
    python generate-api-qdoc.py

    printGreen "Create nymea docs"
    cd ${CONFIG_DIR}/nymea
    qdoc config.qdocconf

    printGreen "Migrate html files"
    for htmlFile in "${OUTPUT_DIR}/nymea-raw/"*.html; do
        printGreen "--> $htmlFile"
        htmlFileName=`basename $htmlFile`
        ${CURRENT_DIR}/doc-tools.py -i ${htmlFile} -o ${OUTPUT_DIR}/nymea/${htmlFileName} -q
    done

    printGreen "Copy common data"
    cp -rv ${TEMPLATE_DIR}/favicons/ ${OUTPUT_DIR}/nymea/
    cp -rv ${TEMPLATE_DIR}/images/ ${OUTPUT_DIR}/nymea/
    cp -rv ${TEMPLATE_DIR}/scripts ${OUTPUT_DIR}/nymea/
    cp -rv ${TEMPLATE_DIR}/styles ${OUTPUT_DIR}/nymea/

    printGreen "Copy nymea images"
    cp -r ${SOURCE_DIR}/nymea/doc/images/* ${CURRENT_DIR}/output/nymea/images/
}


function create-nymea-plugins-docs() {
    printGreen "Clean nymea-plugins"
    if [ -d ${SOURCE_DIR}/nymea-plugins ]; then rm -rf ${SOURCE_DIR}/nymea-plugins; fi
    if [ -d ${OUTPUT_DIR}/nymea-plugins ]; then rm -rf ${OUTPUT_DIR}/nymea-plugins; fi
    if [ -d ${OUTPUT_DIR}/nymea-plugins-raw ]; then rm -rf ${OUTPUT_DIR}/nymea-plugins-raw; fi

    mkdir -p ${SOURCE_DIR} || true

    cd ${SOURCE_DIR}
    git clone --depth 1 -b update-docs-mechanism https://github.com/guh/nymea-plugins.git

    printGreen "Prepare nymea-plugins docs"
    mkdir -p ${OUTPUT_DIR}/nymea-plugins

    printGreen "Create nymea-plugins docs"
    ${CURRENT_DIR}/doc-tools.py -p

    printGreen "Copy common data"
    cp -rv ${TEMPLATE_DIR}/favicons/ ${OUTPUT_DIR}/nymea-plugins/
    cp -rv ${TEMPLATE_DIR}/images/ ${OUTPUT_DIR}/nymea-plugins/
    cp -rv ${TEMPLATE_DIR}/scripts ${OUTPUT_DIR}/nymea-plugins/
    cp -rv ${TEMPLATE_DIR}/styles ${OUTPUT_DIR}/nymea-plugins/
}

function create-qtcoap-docs() {
    printGreen "Clean qtcoap source"
    if [ -d ${SOURCE_DIR}/qtcoap ]; then rm -rf ${SOURCE_DIR}/qtcoap; fi
    if [ -d ${OUTPUT_DIR}/qtcoap ]; then rm -rf ${OUTPUT_DIR}/qtcoap; fi
    if [ -d ${OUTPUT_DIR}/qtcoap-raw ]; then rm -rf ${OUTPUT_DIR}/qtcoap-raw; fi

    mkdir -p ${SOURCE_DIR}
    mkdir -p ${OUTPUT_DIR}/qtcoap

    cd ${SOURCE_DIR}
    git clone --depth 1 https://github.com/t-mon/qtcoap.git

    printGreen "Create qtcoap docs"
    cd ${CONFIG_DIR}/qtcoap
    qdoc config.qdocconf

    printGreen "Migrate html files"
    for htmlFile in "${OUTPUT_DIR}/qtcoap-raw/"*.html; do
        printGreen "--> $htmlFile"
        htmlFileName=`basename $htmlFile`
        ${CURRENT_DIR}/doc-tools.py -i ${htmlFile} -o ${OUTPUT_DIR}/qtcoap/${htmlFileName} -q
    done

    printGreen "Copy common data"
    cp -rv ${TEMPLATE_DIR}/favicons/ ${OUTPUT_DIR}/qtcoap/
    cp -rv ${TEMPLATE_DIR}/images/ ${OUTPUT_DIR}/qtcoap/
    cp -rv ${TEMPLATE_DIR}/scripts ${OUTPUT_DIR}/qtcoap/
    cp -rv ${TEMPLATE_DIR}/styles ${OUTPUT_DIR}/qtcoap/

    printGreen "Copy qtcoap images"
}

function create-nymea-mqtt-docs() {
    printGreen "Clean nymea-mqtt source"
    if [ -d ${SOURCE_DIR}/nymea-mqtt ]; then rm -rf ${SOURCE_DIR}/nymea-mqtt; fi
    if [ -d ${OUTPUT_DIR}/nymea-mqtt ]; then rm -rf ${OUTPUT_DIR}/nymea-mqtt; fi
    if [ -d ${OUTPUT_DIR}/nymea-mqtt-raw ]; then rm -rf ${OUTPUT_DIR}/nymea-mqtt-raw; fi
    mkdir -p ${SOURCE_DIR}
    mkdir -p ${OUTPUT_DIR}/nymea-mqtt

    cd ${SOURCE_DIR}
    git clone --depth 1 -b qdoc https://github.com/guh/nymea-mqtt.git

    printGreen "Create nymea-mqtt docs"
    cd ${CONFIG_DIR}/nymea-mqtt
    qdoc config.qdocconf

    printGreen "Migrate html files"
    for htmlFile in "${OUTPUT_DIR}/nymea-mqtt-raw/"*.html; do
        printGreen "--> $htmlFile"
        htmlFileName=`basename $htmlFile`
        ${CURRENT_DIR}/doc-tools.py -i ${htmlFile} -o ${OUTPUT_DIR}/nymea-mqtt/${htmlFileName} -q
    done

    printGreen "Copy common data"
    cp -rv ${TEMPLATE_DIR}/favicons/ ${OUTPUT_DIR}/nymea-mqtt/
    cp -rv ${TEMPLATE_DIR}/images/ ${OUTPUT_DIR}/nymea-mqtt/
    cp -rv ${TEMPLATE_DIR}/scripts ${OUTPUT_DIR}/nymea-mqtt/
    cp -rv ${TEMPLATE_DIR}/styles ${OUTPUT_DIR}/nymea-mqtt/

    printGreen "Copy nymea-mqtt images"
}



create-nymea-docs
create-nymea-plugins-docs
create-qtcoap-docs
create-nymea-mqtt-docs
