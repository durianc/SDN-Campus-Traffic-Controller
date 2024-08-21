import random
from scapy.all import IP, TCP, UDP, send, Raw
from scapy.all import RandIP
import threading
data_set = []
def generate_packets():
    
    global data_set
    
    for i in range(500):#range 500*range 20*thread 5=50000 packets
        Nd = random.randint(1, 7)
        Ne = random.randint(1, 7)
        Nf = 20 - Nd - Ne - 5
        for r in range(5):
            src_ip = '192.168.31.' + str(random.randint(74, 77))
            dst_ip = '192.168.31.' + str(random.randint(74, 77))

            while src_ip == dst_ip:
                dst_ip = '192.168.31.' + str(random.randint(74, 77))
            sender_port = random.randint(990, 1010)
            receiver_port = random.randint(70, 90)
            ip = IP(src=src_ip, dst=dst_ip)
            tcp = TCP(sport=sender_port, dport=receiver_port)
            pkt = ip / tcp
            data_set.append(pkt)
            
        for j in range(Nd):
            src_ip = '192.168.31.' + str(random.randint(74, 77))
            dst_ip = '192.168.31.' + str(random.randint(74, 77))

            while src_ip == dst_ip:
                dst_ip = '192.168.31.' + str(random.randint(74, 77))
            sender_port = random.randint(700, 1300)
            receiver_port = random.randint(70, 90)
            ip = IP(src=src_ip, dst=dst_ip)
            tcp = TCP(sport=sender_port, dport=receiver_port)
            pkt = ip / tcp
            data_set.append(pkt)

        for k in range(Ne):
            src_ip = '192.168.31.' + str(random.randint(74, 77))
            dst_ip = '192.168.31.' + str(random.randint(74, 77))

            while src_ip == dst_ip:
                dst_ip = '192.168.31.' + str(random.randint(74, 77))
            receiver_port = random.randint(70, 90)
            udp = UDP(sport=random.randint(300, 1700), dport=receiver_port)
            pkt = IP(src=src_ip, dst=dst_ip) / udp / Raw(load="Hello FZU")
            data_set.append(pkt)

        for d in range(Nf):
            src_ip = '192.168.31.' + str(random.randint(74, 77))
            dst_ip = '192.168.31.' + str(random.randint(74, 77))

            while src_ip == dst_ip:
                dst_ip = '192.168.31.' + str(random.randint(74, 77))
            receiver_port = random.randint(70, 90)
            udp = UDP(sport=random.randint(980, 1020), dport=receiver_port)
            pkt = IP(src=RandIP(), dst=dst_ip) / udp / Raw(load="Heal the world!")
            data_set.append(pkt)


def send_packets(num_threads):
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=generate_packets)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    send(data_set)

if __name__ == '__main__':
    num_threads = 5  # 设置线程数
    send_packets(num_threads)
