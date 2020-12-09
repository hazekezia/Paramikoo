import paramiko

ip_list = ["192.168.43.234","192.168.43.153","192.168.43.247","192.168.43.249"]
username = "root"
password = "haze"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def allcall():
    #Menu Apps
    print("1. Hitung Luas dan Keliling Segitiga")
    print("2. Hitung Luas dan Keliling Lingkaran")
    print("3. Hitung Luas dan Keliling Persegi")

    x = str(input("\nPilihan : "))
    print()
    #1. Segitiga 2. Lingkaran 3. Persegi
    if (x=="1"):
        a = float(input("Masukkan nilai alas : "))
        t = float(input("Masukkan nilai tinggi : "))
        s = float(input("Masukkan nilai sisi : "))
        print()
        x=1
        for ipaddr in ip_list:
            ssh_client.connect(hostname=ipaddr,username=username,password=password)
            print ("Sukses login ke {0} (Mesin {1})".format(ipaddr, x))
            x=x+1
            conn = ssh_client.get_transport().open_session()
            conn.invoke_shell()
            
            conn.send("cd UAS\n")
            conn.send("python3 klsegi.py\n")
            conn.send(str(a) + "\n")
            conn.send(str(t) + "\n")
            conn.send(str(s) + "\n")
            
            output = conn.recv(65535).decode('ascii')
            print(output)
            
    elif (x=="2"):
        r = float(input("Masukkan nilai jari-jari : "))
        print()
        x=1
        for ipaddr in ip_list:
            ssh_client.connect(hostname=ipaddr,username=username,password=password)
            print ("Sukses login ke {0} (Mesin {1})".format(ipaddr, x))
            x=x+1
            conn = ssh_client.get_transport().open_session()
            conn.invoke_shell()
            
            conn.send("cd UAS\n")
            conn.send("python3 klling.py\n")
            conn.send(str(r) + "\n")
            
            output = conn.recv(65535).decode('ascii')
            print(output)
            
    elif (x=="3"):
        s = float(input("Masukkan nilai sisi : "))
        print()
        x=1
        for ipaddr in ip_list:
            ssh_client.connect(hostname=ipaddr,username=username,password=password)
            print ("Sukses login ke {0} (Mesin {1})".format(ipaddr, x))
            x=x+1
            conn = ssh_client.get_transport().open_session()
            conn.invoke_shell()
            
            conn.send("cd UAS\n")
            conn.send("python3 klpers.py\n")
            conn.send(str(s) + "\n")
            
            output = conn.recv(65535).decode('ascii')
            print(output)
    
    else:
        print("Tidak tersedia. Silahkan ulangi kembali.")