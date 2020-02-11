import struct, socket, adns, sys, time, os

if len(sys.argv) == 3:
	start = sys.argv[1]
	end = sys.argv[2]
else:
	print "Usage:",sys.argv[0],"[Start_IP] [End_IP]"
	exit()

start = struct.unpack('>I', socket.inet_aton(start))[0]
end = struct.unpack('>I', socket.inet_aton(end))[0]

intensity = 500
resolved_IPs = {}
active_queries = {}
IP_queue = []
IPs = end - start + 1
success = 0
mainsub = adns.init()


for i in range(start,end+1):
	ip = socket.inet_ntoa(struct.pack('>I', i))
	IP_queue.append(ip)

def collect_results():
	global success
	for query in mainsub.completed():
		answer = query.wait()
		IP = active_queries[query]
		del active_queries[query]
		if answer[0] == 0:
			ptr = answer[3][0]
			success += 1
			resolved_IPs[IP] = ptr
		else:
			resolved_IPs[IP] = None

def finished_resolving():
	os.system('clear')
	print "Total IPs: ", IPs
	print "Remaining IPs: ", len(IP_queue)
	print "Resolved IPs: ", len(resolved_IPs)
	print "Active Queries: ", len(active_queries)
	print "Successed Resolved IPs: ", success
	time.sleep(0.05)

	if len(IP_queue) == 0 and len(active_queries) == 0:
		time.sleep(10)
		return True
	else:
		return False

def main():
	while not finished_resolving():
		while IP_queue and len(active_queries) < intensity:
			IP = IP_queue.pop()
			query = mainsub.submit_reverse(IP, adns.rr.PTR)
			active_queries[query] = IP
		collect_results()

	print "#######################################################"
	for IP in resolved_IPs:
		if resolved_IPs[IP] != None:
			print IP, resolved_IPs[IP]
	print "#######################################################"

main()
