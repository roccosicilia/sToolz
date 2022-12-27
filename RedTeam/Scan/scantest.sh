
# set var
args=("$@")
target = ${args[1]}

# out
echo "Setup scan for $target"
sleep 1

# scan
echo "########################################"
nmap -sn -PR -T5 -oA alive $target
