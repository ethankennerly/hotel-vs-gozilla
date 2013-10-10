#!/bin/bash
kill -9 `ps -A | grep ' python' | gawk '{print $1}'`

