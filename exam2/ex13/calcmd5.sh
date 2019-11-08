#!/bin/bash
echo $1 | md5sum | awk '{print $1}'
