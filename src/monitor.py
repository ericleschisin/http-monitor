import sys
import os.path
import yaml
import requests
import time
from urllib.parse import urlparse
from datetime import timedelta

MAX_LATENCY = timedelta(milliseconds=500)
INTERVAL = 15
history = {}

# Load config
try:
  config_file = str(sys.argv[1])
except NoInputException:
  print("Please provide config file path.")

try:
  print('Using: ' + config_file)
  with open(config_file, 'r') as file:
    config = yaml.safe_load(file)
except NoSuchFileException:
  print(e)


def output_history():
  for url in history:
    uptime_percentage = 100 * (history[url]['num_up'] / history[url]['num_checked'])
    print("{0} has {1} % availability percentage".
      format(url, uptime_percentage))

def update_history(url,response):
  if url in history:
    entry = history[url]
  else:
    entry = { 'num_checked': 0 ,'num_up': 0 }
  entry['num_checked'] += 1
  if 200 <= response.status_code <= 299 and response.elapsed < MAX_LATENCY:
    entry['num_up'] += 1
  history.update({ url : entry })


def check_endpoint(endpoint):
  if 'headers' in endpoint.keys():
    r_headers = endpoint['headers']
  else:
    r_headers = {'user-agent': 'fetch-synthetic-monitor'}
  # Send POST or Get request
  if 'method' in endpoint.keys() and endpoint['method'] == 'POST':
    if 'body' in endpoint.keys():
      r_data = endpoint['body']
    else:
      r_data = {'body': ''}
    r = requests.post(endpoint['url'], data=r_data, headers=r_headers)
  else:
    r = requests.get(endpoint['url'], headers=r_headers)
  update_history(urlparse(endpoint['url']).netloc,r)


if __name__ == "__main__":
  while(True):
    for endpoint in config:
      check_endpoint(endpoint)

    output_history()
    time.sleep(INTERVAL)

