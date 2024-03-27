import threading,time,socket,os

main_ip='209.222.115.'
hypixel_ips=['102','108','71','69','89']

def ping(ip):
    try:
        port=25565
        ip=main_ip+ip
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip,port))
        s.send('-'.encode())
        a,c=s.recv(4096)
        print(f"CONNECTION! {ip}:{str(port)}")
        os.system(f"echo {ip}:{str(port)}| clip")
        print(a)
        print(c)
    except Exception as e:
        if(not isinstance(e,socket.timeout)):
            print(e)

def loop():
    for ip in hypixel_ips:
        f=threading.Thread(target=ping, args=(ip,))
        f.start()
        time.sleep(5/len(hypixel_ips))

while True:
    loop()