#!/bin/bash

if ls $1 >> /tmp/log 2>>/tmp/ls_err.log
then
	echo ls ok
else
	echo ls FAIL
fi

