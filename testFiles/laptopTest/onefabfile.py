#from fabric import task
from fabric.api import local
import fabric

#@task
def hello():
	print("hello world")

#@task
def test():
	local('echo hello world')
