def http_get(host, page):
	import socket
	sock = socket.create_connection((host, 80))
	sock.sendall(('GET ' + page + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n').encode())
	print(sock.recv(1000).decode())
	sock.close()

http_get('69.89.31.113', '/CScourses/03b2_minimal-meta.html')