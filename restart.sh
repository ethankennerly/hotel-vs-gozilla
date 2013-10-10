#!/bin/bash
./kill_python.sh
now=`date +%Y-%m-%d_%H%M_%S`
mv embassy_internetbrothers.log embassy_internetbrothers.$now.log
mv example.log example.$now.log
./embassy.sh
tail -F embassy_internetbrothers.log
