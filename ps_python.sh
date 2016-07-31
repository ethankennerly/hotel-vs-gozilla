#!/bin/bash
ps -a | grep ' python' | gawk '{print $1}'
