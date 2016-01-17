#!/bin/bash
#
#
# by Chen Siyu
#
# This script is used to do the symbolic link installation process
#
# for those softwares downloaded and unzipped like a folder
#
# must be under scala top level folder


src_dir=`pwd`
src_suffix=".py"
exe_list="ipserver findipserver"
exe_suffix=""

if [ $# -ne 1 ]
	then
	echo this scirpt take precisely one argument
	echo 'link|unlink'
	exit 1
fi

cmd=$1
case $cmd in
	"link")
		echo start linking		
		for sym in $exe_list
		do
			src="$src_dir/${sym}${src_suffix}"
			dst="/usr/local/bin/${sym}${exe_suffix}"
			echo "linking $src to $dst"
			ln -s "$src" "$dst"
		done
		;;
	"unlink")
		echo removing
		for sym in $exe_list
		do
			target="/usr/local/bin/${sym}${exe_suffix}"
			if [ ! -a "$target" ]
				then
				echo "pass:$target"
				continue
			fi
			echo "removing $target"
			rm "$target"
		done
		;;
	*)
		echo "unknown command, support: link|unlink"
		exit 1
		;;
esac
exit 0
