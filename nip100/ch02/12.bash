#!/bin/bash

N=2
for ((i=1;i<$N+1;i++)) do cut -f $i popular-names.txt > col$i.txt; done
