#!/bin/sh

cut -f 1 popular-names.txt | sort | uniq -c | sort -n -r
