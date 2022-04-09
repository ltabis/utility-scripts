#!/bin/bash

prompt="$1"
command="$2"

echo "$prompt"

result=$(echo -e "Yes\nNo" | dmenu)

if [ "$result" == "Yes"  ]
then
    ${command}
fi
