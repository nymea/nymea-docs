#!/bin/bash -e

PROGRAM_NAME=`basename $0`

display_help () {
    echo "Usage: $PROGRAM_NAME [options] [command]"
    echo ""
    echo "Available commands:"
    echo "    help                      - Display this help."
    echo "    delete                    - Delete a container."
    echo "    shell                     - Enter a container."
    echo "    clean                     - Clean the snap build dir."
    echo "Options:"
    echo "    --help, -h                - Display this help."
    echo "    --branch=<value>          - Use given branch to check out sources (Default: master)."
}

echo "******************* $@"

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
        *)
        ;;
      esac
      shift
    ;;
    *)
      break;
    ;;
  esac
done

cd tools
export QT_SELECT=qt5
./generate-docs $BRANCH
cd ..


npm i
npm run build
cd dist
