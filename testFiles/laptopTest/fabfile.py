from fabric import task
from fabric.api import local

@task
def hello(ctx):
	print("hello world")

@task
def test(ctx):
	local('echo hello world')
