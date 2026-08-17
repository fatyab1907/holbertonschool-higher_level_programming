#!/bin/bash
# Sends a GET request with a header X-School-User-Id: 98 and displays response body
curl -sH "X-School-User-Id: 98" "$1"
