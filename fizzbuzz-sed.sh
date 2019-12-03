#!/bin/bash
sed -e '0~5s/[0-9]*/buzz/' \
    -e '0~3s/[0-9]*/fizz/' \
    <(for i in {1..100}; do echo $i; done)
