#!/bin/bash -e

BRANCH="master"

while [ "$1" != "" ]; do
    OPTION=`echo $1 | awk -F= '{print $1}'`
    VALUE=`echo $1 | awk -F= '{print $2}'`
    case $1 in
        -*)
            case $OPTION in
                --branch | -b)
                    BRANCH=$VALUE
                ;;
                --help | -h)
                    echo "Usage: build.sh [--branch=<branch>]"
                    exit 0
                ;;
            esac
            shift
        ;;
        *)
            break
        ;;
    esac
done

make generate html BRANCH="$BRANCH"
