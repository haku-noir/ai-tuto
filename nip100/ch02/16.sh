#!/bin/sh

n=`./10.sh popular-names.txt`
split -e -l $(($n / $1)) --numeric-suffixes=1 --additional-suffix=.txt popular-names.txt popular-names-
