#!/bin/sh

TAB="$(printf '\\\011')" 
sed "s/${TAB}/ /g" popular-names.txt
