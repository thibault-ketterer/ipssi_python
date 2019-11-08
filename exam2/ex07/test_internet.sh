#!/bin/bash

dat=$(date +%Y-%m-%d:%T)
if curl -s www.google.com > /dev/null;then
	echo "$dat internet ok" >> internet.log
else
	echo "$dat internet FAIL" >> internet.log
fi
