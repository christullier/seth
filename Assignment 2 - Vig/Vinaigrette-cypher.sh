#!/bin/bash

chr() {
  [ "$1" -lt 256 ] || return 1
  printf "\\$(printf '%03o' "$1")"
}

ord() {
  LC_CTYPE=C printf '%d' "'$1"
}

if [ $# -ne 2 ]
then
	echo Usage: \"vinaigrette-cypher.sh [key] [message]\"
else
	length=$(expr length $2)
	length_key=$(expr $(expr length $1) - 1 )
	message=$2
	key=$1
	
	for ((i=0, key_cnt=0; i<$length; i++, key_cnt++)); do
		char1=${message:$i:1}
		
		if [ $key_cnt -gt $length_key ]; then
			key_cnt=0
		fi
		
		char2=${key:$key_cnt:1}
		
		val1=$(expr $(ord $char1) - 97 )
		val2=$(expr $(ord $char2) - 97 )
		
		val3=$(expr $(expr $val1 + $val2 ) % 26 )
		val3_adj=$(expr $val3 + 97 )
		char3=$(chr $val3_adj)
		
		echo -n $char3
	done
	echo
fi
