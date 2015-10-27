#!/bin/bash

cmd="$1"
shift
. venv/Scripts/activate
export PYTHONPATH=$PWD/Lib:$PYTHONPATH
exec "$cmd" "$@"
