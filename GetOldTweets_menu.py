#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (C) 2015 Mariluz Congosto
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
import os
import sys
#import os.path
import codecs
import argparse

def get_dir (query,path):
  while True:
    dir  = raw_input (query)
    if os.path.isdir('%s%s' % (path,dir)):
      break
    else:
      print '>>>>%s/%s file does not exist' % (path,dir)
  return dir

def main():
  reload(sys)
  sys.setdefaultencoding('utf-8')
  sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
  #defino argumentos de script
  parser = argparse.ArgumentParser(description='menu for t-hoarder_kit')
  parser.add_argument('root', type=str, help='path where t_hoarder_kit was installed')
  action = parser.add_mutually_exclusive_group(required=True)
  action.add_argument('--windows', action='store_true',help='windows OS')
  action.add_argument('--linux', action='store_true',help='linux OS')
  action.add_argument('--mac', action='store_true',help='mac OS')
  args = parser.parse_args()
  root= args.root
  if args.windows:
    path_store='%s\\store\\' % root
  if args.linux or args.mac:
    path_store='%s/store/' % root
  enviroment=False
  option=5
  exit='n'
  if not enviroment: 
    print  'working in', root
    print  ' '
    print '----------------------------------------'
    print '------>    Environment  data     <------'
    print '----------------------------------------'

    experiment=get_dir ('Enter experiment name: ', path_store)
    enviroment =True
  if args.windows:
    path_experiment = '%s%s\\' % (path_store,experiment)
  elif args.linux or args.mac:
    path_experiment='%s%s/' % (path_store,experiment)

  while exit != 'y':
    try:
      print '--------------------------------'
      print ' Working in:'
      print '   experiment:', path_experiment
      print '--------------------------------'
      print 'What function do you want to run?'
      print '--------------------------------'
      print '1. Get tweets by username'
      print '2. Get tweets by username and bound dates'
      print '3. Get tweets by query search'
      print '4. Get tweets by query search and bound dates'
      print '5. Exit'
      print ' '
      while True:
        try:
          option = int(raw_input('--> Enter option: '))
          break
        except:
          pass
      if option ==1:
        os.chdir(path_experiment)
        print path_experiment
        user= raw_input ('Enter a screen name user: ')
        max_tweets= raw_input ('Enter max number of tweets: ')
        outputfile= raw_input ( 'Enter output file name: ')
        if args.windows:
          command="python2.7 %s/Exporter.py --username %s --maxtweets %s --output %s" % (root,user,max_tweets,outputfile) 
        else:
          command="python2.7 %s/Exporter.py --username '%s' --maxtweets '%s' --output '%s'" % (root,user,max_tweets,outputfile)
        os.system(command)
      elif option ==2:
        os.chdir(path_experiment)
        user= raw_input ('Enter a screen name user: ')
        since= raw_input ('Since (yyyy-mm-dd) : ')
        until= raw_input ('Until (yyyy-mm-dd) : ')
        max_tweets= raw_input ('Enter max number of tweets: ')
        outputfile= raw_input ( 'Enter output file name: ')
        if args.windows:
          command="python2.7 %s/Exporter.py --username %s --since %s --until %s --maxtweets %s --output %s" % (root,user,since,until,max_tweets,outputfile) 
        else:
          command="python2.7 %s/Exporter.py --username '%s' --since '%s' --until '%s' --maxtweets '%s' --output '%s'" % (root,user,since,until,max_tweets,outputfile)
        os.system(command)
      if option ==3:
        os.chdir(path_experiment)
        print path_experiment
        user= raw_input ('Enter a query search: ')
        max_tweets= raw_input ('Enter max number of tweets: ')
        outputfile= raw_input ( 'Enter output file name: ')
        if args.windows:
          command="python2.7 %s/Exporter.py --querysearch %s --maxtweets %s --output %s" % (root,user,max_tweets,outputfile) 
        else:
          command="python2.7 %s/Exporter.py --querysearch '%s' --maxtweets '%s' --output '%s'" % (root,user,max_tweets,outputfile)
        os.system(command)
      elif option ==4:
        os.chdir(path_experiment)
        user= raw_input ('Enter a query search: ')
        since= raw_input ('Since (yyyy-mm-dd) : ')
        until= raw_input ('Until (yyyy-mm-dd) : ')
        max_tweets= raw_input ('Enter max number of tweets: ')
        outputfile= raw_input ( 'Enter output file name: ')
        if args.windows:
          command="python2.7 %s/Exporter.py --querysearch %s --since %s --until %s --maxtweets %s --output %s" % (root,user,since,until,max_tweets,outputfile) 
        else:
          command="python2.7 %s/Exporter.py --querysearch '%s' --since '%s' --until '%s' --maxtweets '%s' --output '%s'" % (root,user,since,until,max_tweets,outputfile)
        os.system(command)
      elif option == 5:
         exit='y'
    except KeyboardInterrupt:
      pass
    finally:
      pass

if __name__ == '__main__':
   try:
     main()
   except KeyboardInterrupt:
     print '\nGoodbye!'
     exit(0)

