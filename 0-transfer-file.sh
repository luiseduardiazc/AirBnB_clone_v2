#!/usr/bin/env bash
# Transfer a file to server
path_file="$1"
ip="$2"
username="$3"
ssh_key="$4"
if [ "$#" -lt 3 ]; then
    echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
else
    scp -i "$ssh_key" -o StrictHostKeyChecking=no "$path_file" "$username"@"$ip":~/
fi
