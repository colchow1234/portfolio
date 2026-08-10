#!/bin/bash
# Double-click this file to preview the site locally.
# It starts a local server in this folder and opens the homepage in your browser.
# Uses dev-server.py so /home and /credits work the same way they do live.
cd "$(dirname "$0")"
PORT=8000
python3 dev-server.py &
SERVER_PID=$!
trap "kill $SERVER_PID" EXIT
sleep 1
echo "Local preview running at http://localhost:$PORT/"
echo "(Press Ctrl+C in this window, or just close it, to stop the server.)"
open "http://localhost:$PORT/"
wait $SERVER_PID
