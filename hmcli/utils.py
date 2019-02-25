import sys

def load_module(mod):
	try:
		exec("from hackerman.crypto import %s as module" % mod)
		return locals()['module']
	except Exception as e:
		print("[!] Error loading hackerman.crypto.%s:" % mod,e)
		exit(1)

print_raw = sys.stdout.buffer.write
