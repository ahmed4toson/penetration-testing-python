import nmap


# دالة لمسح المنافذ
def scan_ports(target_ip):
    # إنشاء كائن من Nmap
    nm = nmap.PortScanner()

    # مسح المنافذ من 22 إلى 1024
    print(f"Scanning {target_ip} for open ports between 22 and 1024...")
    nm.scan(target_ip, '22-1024')

    # طباعة جميع الأجهزة التي تم اكتشافها
    for host in nm.all_hosts():
        print(f"Host: {host}")
        print(f"State: {nm[host].state()}")

        # طباعة المنافذ المفتوحة لكل جهاز
        for protocol in nm[host].all_protocols():
            print(f"Protocol: {protocol}")
            open_ports = nm[host][protocol].keys()
            for port in open_ports:
                print(f"Port {port}: {nm[host][protocol][port]['state']}")


# تنفيذ السكربت
if __name__ == "__main__":
    # طلب عنوان IP من المستخدم
    target_ip = input("Enter the target IP address: ")

    # مسح المنافذ على العنوان المحدد
    scan_ports(target_ip)
