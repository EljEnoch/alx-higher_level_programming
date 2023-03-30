#!/bin/bash
#display allowed methods http
curl -sI "$1" | grep "Allow:" | cut -b 8-
