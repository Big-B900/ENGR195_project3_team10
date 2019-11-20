from fabric2 import task# env, run
#from fabric.api import Connection #local


@task
def hello(ctx):
	print("hello world")

@task
def test(ctx):
	local('echo hello world')
