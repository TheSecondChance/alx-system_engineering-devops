#!/bin/bash

if [ "$#" -eq 2 ]; then
	if [ "$2" == 'c' ]; then
		chmod u+x "$1"
		echo "chmod is done"
		git add "$1"
		git commit -m "Add $1"
		git push
		echo "Your '$1' file is now Executable \git add, git commit, and git push - All Done!"
	elif [ "$2" == 'f' ]; then
		chmod u+x "$1"
		echo "chmod is done"
		git add "$1"
		git commit -m "Fix $1"
		git push
		echo "Fix Done"
	else
		echo "Wrong Key!"
	fi
elif [ "$#" -eq 1 ]; then
	chmod u+x "$1"
	git add "$1"
	git commit -m "Add $1"
	git push
	echo "All Done!"
else
	echo "Something Error. Try Again!"
fi
