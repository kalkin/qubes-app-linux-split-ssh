if [ -f /var/run/qubes-service/ssh-agent-proxy ]; then
    ssh-agent -k 2>/dev/null
    export SSH_AUTH_SOCK=/tmp/ssh-agent-proxy.socket
fi
