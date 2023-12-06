#!/bin/bash

rm `find . -name "*.dot"`

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

dirs=(
    "calculations/ghg/base" 
    "calculations/ghg/scope_1" 
    "calculations/ghg/scope_1/forms" 
    "calculations/ghg/scope_2" 
    "calculations/ghg/scope_2/forms"
    "calculations/ghg/scope_3"
    "calculations/ghg/scope_3/forms"
)

for i in ${!dirs[@]}; do
    cd ${dirs[$i]}
    pyreverse -a 1 -m y --ignore forms .
    sed -i 's/ghg.scope_1.//g' classes.dot
    sed -i 's/ghg.scope_2.//g' classes.dot
    sed -i 's/ghg.scope_3.//g' classes.dot
    sed -i '/Meta/d' classes.dot
    sed -i '/ModelForm/d' classes.dot
    cd $SCRIPT_DIR
done

rm `find . -name "packages.dot"`