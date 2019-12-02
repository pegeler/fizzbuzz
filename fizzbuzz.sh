#!/bin/bash
for i in {1..100}; do
  ((i % 3)) || fizz="fizz"
  ((i % 5)) || buzz="buzz"
  
  if [[ -n $fizz || -n $buzz ]]; then 
    echo $fizz$buzz
    unset fizz
    unset buzz
  else
    echo $i
  fi
done
