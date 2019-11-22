from fabric import task, Connection
import subprocess

c = Connection('raspi')

method = input("commit message: ")

p = subprocess.Popen(["git", "add","."], stdout=subprocess.PIPE)
q = subprocess.Popen(["git", "commit","-m",'"{}"'.format(method)], stdout=subprocess.PIPE)
r = subprocess.Popen(["git", "push"], stdout=subprocess.PIPE)

print(p.communicate())
print(q.communicate())
print(r.communicate())
#c.local("git pull")
result = c.run("cd {} && git pull".format("/home/pi/project3/ENGR195_project3_team10/"))
print(result)

