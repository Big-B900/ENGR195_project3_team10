from fabric import task

# the directory of your project on your VPS
code_dir = '/home/pi/project3/ENGR195_project3_team10/'

#bram/Documents/python/engr195/project3/ENGR195_project3_team10/testFiles/laptopTest'

# here, you can provide a default hostname
# (from your .ssh/config)
default_hosts = ["raspi"]
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
