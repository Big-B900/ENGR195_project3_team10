from fabric import task
from __future__ import with_statement
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm


@task
def hello(ctx):
	print("hello world")

@task
def deploy(ctx):
    code_dir = '~/project3/ENGR195_project3_team10/testFiles'
    with lcd(code_dir):
        run("git pull")
        run("touch app.wsgi")

