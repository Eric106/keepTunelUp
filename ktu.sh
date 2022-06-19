#!/bin/bash
tmux new-session -d -s ktu
tmux send-keys -t ktu.0 "cd /home/systemacs/Documents/keepTunelUp/ " ENTER
tmux send-keys -t ktu.0 "python3 ktu.py -host \"10.0.0.5\" -sleep 5 -command \"sudo /etc/firewall/firewall\" " ENTER
