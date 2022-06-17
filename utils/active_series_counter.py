import argparse, urllib.request, sys

def prefix_match(line, prefixes):
  # 1. Look for a match
  for prefix in prefixes:
    if line.startswith(prefix):
      return True
  # 2. No match found
  return False

def count_series(metrics, prefixes, allowed):

  active_series = 0
  # 1. Split metrics by new line and iterate over lines
  for line in metrics.split('\\n'):
    # 2. Skip comments
    if not line.startswith("#") and len(line)>0:
      # 3. Count them all use case
      if prefixes is None:
        active_series += 1
      else:
        if allowed and prefix_match(line, prefixes):
          # 3'. Allow list use case
          active_series += 1
        elif (not allowed) and (not prefix_match(line, prefixes)):
          # 3''. Block list use case
          active_series += 1
  # 4. Return the active series number
  return active_series


def get_metrics(metrics_ep):

  payload = ""
  # 1. Try pulling the metrics from the endpoint
  try:
    payload = str(urllib.request.urlopen(metrics_ep).read())
  except Exception as e:
    print(f"ERROR: The '{metrics_ep}' endpoint doesn't seem to right.")
    print("Please, check it manually before using this helper")
    sys.exit(1)
  # 2. Check if it's a Prometheus compatible endpoint
  if (not "HELP" in payload) and (not "TYPE" in payload):
    print(f"ERROR: The '{metrics_ep}' endpoint doesn't seem to be a Prometheus compatible metrics endpoint")
    print("Please, check it manually before using this helper")
    sys.exit(1)
  # 3. Return metrics
  return payload

def get_prefixes(allow_list):

  prefixes = []
  try:
    prefixes = allow_list.split(",")
  except Exception as e:
    print(f"ERROR: The {allow_list} allow list couldn't be split")
    sys.exit(1)
  return prefixes

if __name__ == "__main__":

  # 1. Check input params, parse them and get the configuration
  parser = argparse.ArgumentParser(description=f"Active Series counter script (by Raul Marin) - this software comes with no guarantees")
  parser.add_argument('--metrics_ep', help='Metrics end-point scraped by Prometheus', required=True)
  parser.add_argument('--prefix_list', help='Comma-separated list of metrics prefixes to consider', required=False)
  parser.add_argument('-allowed', help='Prefix list considered as allowed metrics when provided, blocked metrics otherwise', action='store_true')
  # 2. Parse arguments and count metrics according to the criteria applied.
  args = parser.parse_args()
  metrics = None if args.metrics_ep is None else get_metrics(args.metrics_ep)
  prefixes = None if args.prefix_list is None else get_prefixes(args.prefix_list)
  # 3. Time to count series
  active_series = count_series(metrics, prefixes, args.allowed)
  print(f"## Active Series counter script (by Raul Marin, Jun'22) - this software comes with no guarantees")
  print(f"#")
  print(f"There are '{active_series}' active series in the provided metrics end point")
