import paramiko
import time
def connect_linux_system(ip_adress,user_name,password):
    try:
        ssh_pre = paramiko.SSHClient()
        ssh_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_pre.connect(ip_adress, username=user_name, password=password)
        time.sleep(10)
        (stdin, stdout, stderr) = ssh_pre.exec_command('free -m')
        return stdout.read()
    except Exception as e:
            print ('entered details wrong or check network connection')
    except Exception as e:
            print ('Error'+str(e))
connect_linux_system('192.168.0.12','krishna','@123')
