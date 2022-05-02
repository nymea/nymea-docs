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
    echo "    --branch=<value>          - Use given branch to check out sources (Default: master)"
}

variables() {
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    LIGHT_RED='\033[1;31m'
    LIGHT_GREEN='\033[1;32m'
    NC='\033[0m'
    ERROR_COLOR=$LIGHT_RED
    POSITIVE_COLOR=$GREEN

    USERNAME=`id --user --name`
    GROUPNAME=$USERNAME
    USERID=150000
    GROUPID=150000

    PACKAGE=`basename "$PWD"`
    LXD_IMAGE_NAME=jammy
    LXD_IMAGE=ubuntu:$LXD_IMAGE_NAME
#    LXD_IMAGE=$LXD_IMAGE_NAME
    LXD_CONTAINER=builder-$CONTAINER_PREFIX$LXD_IMAGE_NAME
    DEPENDENCIES="npm python3-git"

    USERDIR=/home/$USERNAME
    MOUNTED_DIRECTORY=$PWD
    MOUNT_POINT=$USERDIR/$PACKAGE
    SOURCE_PATH_CONTAINER=$MOUNT_POINT

}

new_container() {
    if lxc info $LXD_CONTAINER > /dev/null 2>&1 ; then
        echo "${POSITIVE_COLOR}LXD container $LXD_CONTAINER already exists.${NC}"
        # FIXME: check if the container is already started
        lxc start $LXD_CONTAINER || true
    else
        echo "${POSITIVE_COLOR}Creating LXD container $LXD_CONTAINER using $LXD_IMAGE.${NC}"
        lxc remote --public=true --accept-certificate=true add nymea https://jenkins.nymea.io || true
        lxc init $LXD_IMAGE $LXD_CONTAINER

        # Note: check the lxc version for lxc.id_map vs lxc.idmap
        LXCVERSION=$(lxc --version)
        LXCMAJORVERSION=$(echo ${LXCVERSION} | cut -d. -f1)
        if [ "${LXCMAJORVERSION}" -lt "3" ]; then
            echo "${POSITIVE_COLOR}Using lxc version 2 compatibility$LXD_IMAGE.${NC}"
            printf "lxc.id_map = g $GROUPID `id --group` 1\nlxc.id_map = u $USERID `id --user` 1" | lxc config set $LXD_CONTAINER raw.lxc -
        else
            printf "uid `id --user` 150000\ngid `id --group` 150000" | lxc config set $LXD_CONTAINER raw.idmap -

#            echo "Mapping uids: lxc.idmap = g $GROUPID `id --group` 1\nlxc.idmap = u $USERID `id --user` 1"
#            printf "lxc.idmap = g `id --group` 1\nlxc.idmap = u $USERID `id --user` 1" | lxc config set $LXD_CONTAINER raw.lxc -
        fi


        lxc start $LXD_CONTAINER
        lxc exec --env GROUPID=$GROUPID --env GROUPNAME=$GROUPNAME $LXD_CONTAINER -- deluser $USERNAME || true
        lxc exec --env GROUPID=$GROUPID --env GROUPNAME=$GROUPNAME $LXD_CONTAINER -- delgroup $GROUPNAME || true
        lxc exec $LXD_CONTAINER -- rm -rf /home/ubuntu
        lxc exec --env GROUPID=$GROUPID --env GROUPNAME=$GROUPNAME $LXD_CONTAINER -- addgroup --gid $GROUPID $GROUPNAME
        lxc exec --env GROUPID=$GROUPID --env USERNAME=$USERNAME --env USERID=$USERID $LXD_CONTAINER -- adduser --disabled-password --gecos "" --uid $USERID --gid $GROUPID $USERNAME
        lxc exec --env USERNAME=$USERNAME $LXD_CONTAINER -- usermod -aG sudo $USERNAME
        exec_container_root passwd --delete $USERNAME

    fi

    if ! lxc config device get $LXD_CONTAINER current_dir_mount disk 2> /dev/null ; then
        echo "${POSITIVE_COLOR}Mounting $MOUNTED_DIRECTORY in container $MOUNT_POINT.${NC}"
        lxc config device add $LXD_CONTAINER current_dir_mount disk source=$MOUNTED_DIRECTORY path=$MOUNT_POINT
    else
        lxc config device set $LXD_CONTAINER current_dir_mount source $MOUNTED_DIRECTORY
    fi

    if ! lxc config device get $LXD_CONTAINER gradle_cache_dir_mount disk 2> /dev/null ; then
        echo "${POSITIVE_COLOR}Mounting gradle cache dir ($HOME/.gradle) in container.${NC}"
        if [ ! -d $HOME/.gradle ]; then mkdir $HOME/.gradle; fi
        lxc config device add $LXD_CONTAINER gradle_cache_dir_mount disk source=$HOME/.gradle/ path=$HOME/.gradle
    fi

    exec_container_root chgrp -R 150000 /opt/ || true

}

delete_container () {
    echo "${POSITIVE_COLOR}Deleting LXD container $LXD_CONTAINER.${NC}"
    lxc delete -f $LXD_CONTAINER
}

install_dependencies() {
    exec_container_root apt update
    exec_container_root apt install --yes $DEPENDENCIES
}

shell_container () {
    echo "${POSITIVE_COLOR}Entering shell in LXD container $LXD_CONTAINER.${NC}"
    lxc exec $LXD_CONTAINER -- su --login $USERNAME
}


check_command_parameter_count () {
    MIN_PARAMETERS=$1
    MAX_PARAMETERS=$2
    COUNT=$(echo $PARAMETERS | wc -w)
    if  [ -n $MIN_PARAMETERS ] && [ $COUNT -lt $MIN_PARAMETERS ] ; then
        display_help
        echo ""
        echo "${ERROR_COLOR}Command '$COMMAND' requires a minimum of $MIN_PARAMETERS parameters. $$
        exit 1
    fi
    if [ -n $MAX_PARAMETERS ] && [ $COUNT -gt $MAX_PARAMETERS ] ; then
        display_help
        echo ""
        echo "${ERROR_COLOR}Command '$COMMAND' accepts at most $MAX_PARAMETERS parameters. $COUNT $
        exit 1
    fi
}

exec_container_root () {
    command="$@"
    #echo lxc exec $LXD_CONTAINER "$@"
    lxc exec $LXD_CONTAINER -- sh -c "cd $SOURCE_PATH_CONTAINER; $command"
}

exec_container () {
    command="$@"
    #echo lxc exec $LXD_CONTAINER "$@"
    lxc exec $LXD_CONTAINER -- su -l -c "cd $SOURCE_PATH_CONTAINER; $command" $USERNAME
}

build () {
    exec_container ./build.sh --branch=$BRANCH
}

clean () {
    exec_container "rm builddir -rf"
}

BRANCH="master"

while [ "$1" != "" ]; do
    OPTION=`echo $1 | awk -F= '{print $1}'`
    VALUE=`echo $1 | awk -F= '{print $2}'`
    VALUEVALUE=`echo $1 | awk -F= '{print $3}'`
    case $1 in
        -*)
            case $OPTION in
            --container-prefix)
                CONTAINER_PREFIX=$VALUE
            ;;
            --branch)
                echo "Setting branch to $VALUE"
                BRANCH=$VALUE
            ;;
            --help | -h | help )
                display_help
                exit 0
            ;;
            *)
                display_help
                echo ""
                echo "error: unknown option: $OPTION"
                exit 1
            ;;
            esac
            shift
        ;;
        *)
            break
        ;;
    esac
done

variables

COMMAND=$1
if [ -n "$COMMAND" ] ; then
    shift
fi

if [ "$COMMAND" = "help" ] ; then
    display_help
    exit 0
fi
if [ -z "$COMMAND" ] ; then
    new_container
    install_dependencies
    build
else
    PARAMETERS=$@
    case "$COMMAND" in
        delete) 
            check_command_parameter_count 0 1
            delete_container
        ;;
        shell)
            check_command_parameter_count 0 1
            new_container
            shell_container
        ;;
        build)
            new_container
            build
        ;;
        clean)
            new_container
            clean $@
        ;;
        *)
            display_help
            echo ""
            echo "${ERROR_COLOR}error: unknown command: $COMMAND${NC}"
            exit 1
        ;;
    esac
fi

