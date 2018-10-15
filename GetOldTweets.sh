#!/bin/bash
#Copyright 2016 Almudena Garcia Jurado-Centurion

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


option=8
salir='n'
echo " "
echo "----------------------------------------"
echo "------> Welcome to GetOldTweets <------"
echo "----------------------------------------"
file_GetOldTweets=`find $HOME -name GetOldTweets.sh 2>/dev/null`
echo ${file_GetOldTweets}
path_GetOldTweets=${file_GetOldTweets%/*}
cd $path_GetOldTweets
cd  ..
root=`pwd`
cd $root
git fetch origin master  > /dev/null  2>&1
status=`git status`

if git status | grep "git pull" > /dev/null;
then
   echo "There are updates from GetOldTweets, do you want to install them (y/n)?"
   echo "Note that if the scripts have been modified, the update will fail"
   read response
   if [ "$response" = "y" ];
   then
      echo "Upgrading changes"
      git pull
      echo "GetOldTweets is up to date"
      echo " Please, enter <ctrl> c to exit and start again"
   fi
else
  echo "GetOldTweets is up to date"
fi
python ${root}/GetOldTweets_menu.py ${root} --linux
