#!/bin/bash
ps -A | grep ' python' | gawk '{print $1}'
