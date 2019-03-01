import argparse
from hmcli.utils import load_module, print_raw

modules = ['tcp','covert.dns']

def parse_args():
	p = argparse.ArgumentParser()
	p.add_argument(
		"-m","--module",
		help=("Which module to load. Available: %s" % (', '.join(modules))),
		required=True)

	p.add_argument(
		"-c","--channel",
		help=("Open a two-way channel. Argument: server/client"))
	p.add_argument(
		"-s","--send",
		help=("Send a single message"),
		action="store_true")
	p.add_argument(
		"-r","--recv",
		help=("Recieve a single message"),
		action="store_true")

	p.add_argument(
		"-f","--file",
		help=("[-s/--send] send from file"))
	p.add_argument(
		"-t","--text",
		help=("[-s/--send] send from text(arg)"))

	p.add_argument(
		"-a","--addr",
		help=("[-m/--mode tcp] address to bind/connect to"))

	args = p.parse_args()
	if args.mode == "tcp" and args.addr is None:
		p.error("-a/--addr is required")
	if args.channel not in ['server','client']:
		p.error("-c/--channel must be either server or client")
	if args.channel is None and args.send is None and args.recv is None:
		p.error("-c/--channel or -s/--send or -r/--recv is required")
	if args.send and args.file is None and args.text is None:
		p.error("-f/--file or -t/--text is required to use -s/--send")

	return args

def main(args):
	base = "hackerman.transport" if not args.mode.startswith("covert.") else "hackerman.transport.covert"
	mm = args.mode if not args.mode.startswith("covert.") else args.mode[6:]
	mod = load_module(base, mm)

	if args.channel:
		if args.mode = "covert.dns":
			conn = mod.SpeedyClient(send="listen.com",recv="send.com") if args.channel == "client" else mod.SpeedyClient()
		else:
			conn = mod.Client((args.addr.split(":")[0], int(args.addr.split(":")[1]))) if args.channel == "client" else mod.Server(int(args.addr.split(":")[1]))

		if args.channel == "client":
			while True:
				print_raw(conn.recv())
				conn.send(input("(Send)> ").encode())
		else:
			while True:
				conn.send(input("(Send)> ").encode())
				print_raw(conn.recv())
		deleteme#cont
