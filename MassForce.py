import adns, time, os, sys

if len(sys.argv) == 2:
	host_file = sys.argv[1]
else:
	print "Usage:",sys.argv[0],"[Hosts_File]"
	exit()

with open(host_file, 'r') as f:
	hosts = [line.strip() for line in f]

intensity = 500
resolved_hosts = {}
active_queries = {}
host_queue = hosts[:]
success = 0
mainsub = adns.init()

def collect_results():
	global success
	for query in mainsub.completed():
		answer = query.check()
		host = active_queries[query]
		del active_queries[query]
		if answer[0] == 0:
			ip = answer[3][0]
			success += 1
			resolved_hosts[host] = ip
		elif answer[0] == 101: # CNAME
			query = mainsub.submit(answer[1], adns.rr.A)
			active_queries[query] = host
		else:
			resolved_hosts[host] = None

def finished_resolving():
	os.system('clear')
	print "Total Hosts: ", len(hosts)
	print "Remaining Hosts: ", len(host_queue)
	print "Resolved Hosts: ", len(resolved_hosts)
	print "Active Queries: ", len(active_queries)
	print "Successed Resolved Hosts: ", success
	time.sleep(0.05)

	if len(host_queue) == 0 and len(active_queries) == 0:
		time.sleep(10)
		return True
	else:
		return False

def main():
	while not finished_resolving():
		while host_queue and len(active_queries) < intensity:
			host = host_queue.pop()
			query = mainsub.submit(host, adns.rr.A)
			active_queries[query] = host
		collect_results()

	print "#######################################################"
	for host in resolved_hosts:
		if resolved_hosts[host] != None:
			print host, resolved_hosts[host]
	print "#######################################################"

main()
