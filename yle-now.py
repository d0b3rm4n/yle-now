#!/usr/bin/python3
#
# MIT License
#
# Copyright (C), Reto Zingg <g.d0b3rm4n@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import argparse
import logging
import requests
from http.client import HTTPConnection

def get_current_played_song(station, appid, apikey):
	logging.debug("Fetch current played song from: %s"%(station))
	logging.debug("APP ID: %s"%(appid))
	logging.debug("API Key: %s"%(apikey))

	base_url = 'https://external.api.yle.fi/v1/programs/'
	api_parameters = "&app_id=%s&app_key=%s"%(appid, apikey)

	session = requests.Session()

	# curl -v "https://external.api.yle.fi/v1/programs/services/{id}.json?app_id=YOUR_APP_ID&app_key=YOUR_APP_KEY"
	call_url = base_url + "nowplaying/" + station + ".json?" + api_parameters 

	logging.info("About to call: %s"%call_url)
	
	response = session.get(call_url)

	if response.status_code != 200:
		logging.debug("Could not fetch: '%s'"%call_url)
		return 'Error in API call...'
	else:
		logging.debug("Response:\n%s"%(response.text))
		data = response.json().get('data')
		for song in data:
			logging.debug("startTime: %s"%song['startTime'])
			logging.debug("endTime: %s"%song['endTime'])
			logging.debug("Delta: %s"%song['delta'])
			if song['delta'] == "1":
				# "content":{
				#   "id":"12-1022-2-36267",
				#   "type":"MusicRecording",
				#   "title":{
				#     "unknown":"Wolframin laulu iltatähdelle oopp. Tannhäuser"
				#   },
				#   "performer":[{"type":"agent","name":"Radion sinfoniaorkesteri"}
				current_playing = ' - '.join(song['content']['title'].values())
				logging.info("This is the current playing song: %s"%current_playing)
				return current_playing

	return 'Huch... so embarrassing, but something went wrong...'


def parse_args():
	'''Parses commandline arguments provided by the user'''

	parser = argparse.ArgumentParser()
	parser.add_argument(
		'-a', '--appid',
		help='Yle API application ID',
		metavar='YLE-APP-ID', type=str, required=True)

	parser.add_argument(
		'-k', '--apikey',
		help='Yle API key',
		metavar='YLE-APP-KEY', type=str, required=True)

	stations=['yle-radio-1', 'yle-puhe', 'yle-mondo', 'ylex']
	parser.add_argument(
		'-s', '--station', choices=stations,
		help='Yle Radio Station, choices: ' + ', '.join(stations),
		metavar='YLE-RADIO-STATION', type=str, default='yle-radio-1')

	parser.add_argument(
		'-V', '--verbose',
		action='count', required=False, default=0,
		help='increase output verbosity (use up to 2 times)')

	return parser.parse_args()

# -----------------------------------------------------------------------------
# Main function related code

def main():
	args = parse_args()

	# setup logging for lower level libraries
	HTTPConnection.debuglevel = args.verbose

	debug_level = 0
	if args.verbose == 0:
		debug_level = logging.CRITICAL
	elif args.verbose == 1:
		debug_level = logging.INFO
	elif args.verbose > 1:
		debug_level = logging.DEBUG

	logging.basicConfig()
	logging.getLogger().setLevel(debug_level)

	requests_log = logging.getLogger("urllib3")
	requests_log.setLevel(debug_level)
	requests_log.propagate = True

	current_played = get_current_played_song(args.station,
						args.appid,
						args.apikey)

	print("On %s is currently playing: %s"%(args.station,current_played))


if __name__ == '__main__':
	main()
