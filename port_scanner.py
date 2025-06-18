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

import nmap
import csv
import os


# دالة لمسح المنافذ
def scan_ports(target_ip, port_range='22-1024'):
    # إنشاء كائن من Nmap
    nm = nmap.PortScanner()

    # مسح المنافذ المحددة
    print(f"Scanning {target_ip} for open ports between {port_range}...")
    nm.scan(target_ip, port_range)

    # طباعة جميع الأجهزة التي تم اكتشافها
    for host in nm.all_hosts():
        print(f"\nHost: {host}")
        print(f"State: {nm[host].state()}")

        # فحص المنافذ المفتوحة
        for protocol in nm[host].all_protocols():
            print(f"Protocol: {protocol}")
            open_ports = nm[host][protocol].keys()
            for port in open_ports:
                port_state = nm[host][protocol][port]['state']
                service = nm[host][protocol][port].get('name', 'Unknown')
                print(f"Port {port}: {port_state} (Service: {service})")

                # تخزين النتائج في ملف CSV
                save_to_csv(host, port, port_state, service, protocol)


# دالة لحفظ النتائج في ملف CSV
def save_to_csv(host, port, state, service, protocol):
    file_exists = os.path.isfile('scan_results.csv')

    # فتح أو إنشاء ملف CSV
    with open('scan_results.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        # إذا كان الملف جديدًا، إضافة رأس الجدول
        if not file_exists:
            writer.writerow(['Host', 'Port', 'State', 'Service', 'Protocol'])

        # كتابة البيانات في الملف
        writer.writerow([host, port, state, service, protocol])


# تنفيذ السكربت
if __name__ == "__main__":
    # طلب عنوان IP من المستخدم
    target_ip = input("Enter the target IP address: ")

    # تحديد نطاق المنافذ (افتراضي من 22 إلى 1024)
    port_range = input("Enter the port range (e.g., 22-1024 or 1025-65535): ") or '22-1024'

    # مسح المنافذ على العنوان المحدد
    scan_ports(target_ip, port_range)
