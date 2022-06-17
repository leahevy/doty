#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

SCRIPT=$(readlink -f $0)
SCRIPTDIR=`dirname $SCRIPT`
SCRIPTDIR=`realpath $SCRIPTDIR`

if [ "${1+-}" = "" ]; then
    echo "Fatal: $(basename $0) called with invalid arguments. (error 1)" >&2
    exit 1
else
    RUN_SCRIPT="$1"
fi
shift 1

if [[ ! -e "$RUN_SCRIPT" ]]; then
    echo "Fatal: script '$RUN_SCRIPT' does not exist (error 3)" >&2
    exit 1
fi

RUN_SCRIPT="$(realpath "$RUN_SCRIPT")"

TMPDIR="$(mktemp -d)"
cd "$TMPDIR"
trap 'rm -rf -- "$TMPDIR"' EXIT

source "$SCRIPTDIR/configure-functions.sh"

source "$RUN_SCRIPT"

for arg in "$@"; do
    set -o pipefail
    IFS=$'\n\t'

    set +eu
    "$arg"
    set -eu
done