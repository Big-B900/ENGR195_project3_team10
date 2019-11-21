from fabric import task, Connection

# the directory of your project on your VPS
#code_dir = #'/home/pi/project2/ENGR195_project3_team10/'

code_dir = '/home/testuser/gitprojects/ENGR195_project3_team10/'
vision_dir = '/home/testuser/gitprojects/ENGR195_project3_team10/classifier/'
env_dir = "/home/testuser/"
# here, you can provide a default hostname
# (from your .ssh/config)
default_hosts = ["kanga2"]
#hosts.user = 'pi'
#hosts.password = 'engr195'


# to perform the task on your default hosts, you
# have to pass them in each task decorator
@task(hosts=default_hosts)
def update(c):
    # I miss the "with cd(...)" syntax :( it's not yet ported
    c.run("cd {} && git pull".format(code_dir))
    # this command will only make sense if you're using docker-compose
    # to deploy your project
    #c.run("cd {} && docker-compose up -d".format(code_dir))

#@task(hosts=default_hosts)
#def download_db(c):
    #c.get("{}/db.sqlite3".format(code_dir), "db.sqlite3")

#@task(hosts=default_hosts)
#def upload_db(c):
    #c.put("db.sqlite3", "{}/db.sqlite3".format(code_dir))

@task(hosts=default_hosts)
def yolo(c):
    # local will do something on your current host, instead
    # of the SSH host - very handy!
    c.local("git push")
    # you can call other tasks - cool, huh?
    update(c)

@task(hosts=default_hosts)
def hello(c):
    c.run(["echo","hello world"])

@task(hosts=default_hosts)
def virtualenv(c):
    c.run("cd {} && source env/bin/activate".format(env_dir))

@task(hosts=default_hosts)
def vision(c):
    c.run("cd {} && source env/bin/activate && cd {} && python3 runvision.py".format(env_dir,vision_dir))






c = Connection('kanga2')
result = c.run("cd {} && git pull".format(code_dir),hide=True)
#print(result.stdout.strip())




