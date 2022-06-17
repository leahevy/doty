#!/bin/bash

# Usable variables
###########
OS="`uname`"
case $OS in
    'Darwin')
        OS="osx"
        ON_MAC=1
        ON_LINUX=0
        ;;
    'Linux')
        OS="linux"
        ON_MAC=0
        ON_LINUX=1
        ;;
    *)
        echo "Fatal: invalid operating system found (error 42)" >&2
        exit 1
        ;;
esac


# Internal run methods
#####################################################
_do_check() {
    enable-strict-mode
    check
}

_do_prepare() {
    enable-strict-mode
    prepare
}

_do_pre-populate() {
    pre-populate
}

_do_post-populate() {
    post-populate
}

_do_configure() {
    configure
}

_do_install() {
    install
}

_do_uninstall() {
    uninstall
}


# Empty function to be overloaded by the configure script
#########################################3###############
check() {
    :
}

prepare() {
    :
}

pre-populate() {
    :
}

post-populate() {
    :
}

configure() {
    :
}

install() {
    :
}

uninstall() {
    :
}


# Internal functions
###################
_write_response() {
    echo "++ DOTY ++ [[[" "$@" "]]]"
}


# Utility functions
###################
enable-strict-mode() {
    set -eu
}

require-pkg() {
    _write_response "pkg" "require" "$1"
}
