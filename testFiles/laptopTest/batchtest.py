
import subprocess
#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE,cwd='/home/bram/Documents/python/eng195/project3/ENGR195_project3_team10/testFiles/laptopTest')
#output, error = process.communicate()

#bashCommand = "echo hello world"

#subprocess.check_call(bashCommand.split())


#with subprocess.Popen(["ifconfig"], stdout=PIPE) as proc:
#    log.write(proc.stdout.read())

#subprocess.call(['df','-h'])

#subprocess.call('du -hs', shell=True)


p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)

print(p.communicate())







