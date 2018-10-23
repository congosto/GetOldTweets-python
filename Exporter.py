#!/usr/bin/python
# -*- coding: utf-8 -*-
#The MIT License (MIT)
#Copyright (c) 2016 Jefferson Henrique
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import sys,getopt,datetime,codecs
import csv
import unicodecsv as csv

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main(argv):

	if len(argv) == 0:
		print('You must pass some parameters. Use \"-h\" to help.')
		return

	if len(argv) == 1 and argv[0] == '-h':
		f = open('exporter_help_text.txt', 'r')
		print f.read()
		f.close()

		return
	format='txt'

	try:
		opts, args = getopt.getopt(argv, "", ("username=", "near=", "within=", "since=", "until=", "querysearch=", "toptweets", "maxtweets=", "output=", "csv"))

		tweetCriteria = got.manager.TweetCriteria()
		outputFileName = "output_got.csv"

		for opt,arg in opts:
			if opt == '--username':
				tweetCriteria.username = arg

			elif opt == '--since':
				tweetCriteria.since = arg

			elif opt == '--until':
				tweetCriteria.until = arg

			elif opt == '--querysearch':
				tweetCriteria.querySearch = arg

			elif opt == '--toptweets':
				tweetCriteria.topTweets = True

			elif opt == '--maxtweets':
				tweetCriteria.maxTweets = int(arg)
			
			elif opt == '--near':
				tweetCriteria.near = '"' + arg + '"'
			
			elif opt == '--within':
				tweetCriteria.within = '"' + arg + '"'

			elif opt == '--within':
				tweetCriteria.within = '"' + arg + '"'

			elif opt == '--output':
				outputFileName = arg
			elif opt == '--csv':
				format = 'csv'
				
		outputFile = codecs.open(outputFileName, "w", "utf-8")
		if format == 'txt':
			print 'generate file txt'
			outputFile.write('id tweet\tdate\tauthor\ttext\tgeolocation\tretweets\tfavorites\tmentions\thashtags\tpermalink')
		else:
			print 'generate file csv'
			writer = csv.writer(f,delimiter=';')
			title= ['id tweet','date','author','text','geolocation','retweets','favorites','mentions','hashtags','permalink']
			writer.writerow(title)
		print('Searching...\n')

		def receiveBuffer(tweets):
			for t in tweets:
				if format == 'txt':
					outputFile.write(('\n%s\t%s\t@%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % ( t.id,t.date.strftime("%Y-%m-%d %H:%M:%S"),t.username, t.text,  t.geo,t.retweets, t.favorites, t.mentions, t.hashtags, t.permalink)))
				if format == 'csv':
					row=[]
					row.append(t.id)
					row.append (t.date.strftime("%Y-%m-%d %H:%M:%S"))
					row.append('@'+t.username)
					row.append(t.geo)
					row.append(t.retweets)
					row.append(t.favorites)
					row.append(t.mentions)
					row.append(t.hashtags)
					row.append(t.permalink)
					writer.writerow(row)
			outputFile.flush()
			print('More %d saved on file...\n' % len(tweets))

		got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)

	except arg:
		print('Arguments parser error, try -h' + arg)
	finally:
		outputFile.close()
		print('Done. Output file generated "%s".' % outputFileName)

if __name__ == '__main__':
	main(sys.argv[1:])
