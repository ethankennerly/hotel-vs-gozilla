#!/bin/bash
./kill_python.sh
now=`date +%Y-%m-%d_%H%M_%S`
mv embassy_internetbrothers.log logs/embassy_internetbrothers.$now.log
mv example.log logs/example.$now.log
./embassy.sh
tail -f embassy_internetbrothers.log
