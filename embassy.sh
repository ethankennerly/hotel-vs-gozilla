#!/bin/bash
echo '' >> embassy_internetbrothers.log
echo '' >> embassy_internetbrothers.log
echo '' >> embassy_internetbrothers.log
nohup python embassy.py --verbose info >> embassy_internetbrothers.log &
