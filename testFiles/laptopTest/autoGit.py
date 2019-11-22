from fabric import task, Connection
import subprocess

c = Connection('raspi')

p = subprocess.Popen(["git", "add","."], stdout=subprocess.PIPE)
q = subprocess.Popen(["git", "commit","-m",'"automated git push"'], stdout=subprocess.PIPE)
r = subprocess.Popen(["git", "push"], stdout=subprocess.PIPE)
#c.local('git config --global user.email "big-b+git@wayfarer.org"')
#c.local('git config --global user.name "Bram"')

#c.local("git add .")
#c.local("git commit -m 'automated git push'")
#c.local("git push")
print(p.communicate())
print(q.communicate())
print(r.communicate())
#c.local("git pull")
c.run("cd {} && git pull".format("/home/pi/project3/ENGR195_project3_team10/"))




#def autoGit(c):
#	vision_dir = '/home/testuser/gitprojects/ENGR195_project3_team10/classifier/'
#	env_dir = "/home/testuser/"
#	result =  c.run("cd {} && source env/bin/activate && cd {} && python3 runvision.py".format(env_dir,vision_dir),hide=True)
#	return result.stdout.strip()


