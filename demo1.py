from fabric.api import sudo, run, task
from fabric.context_managers import cd


@task
def install():
    run('echo "holas"')
# from fabric.api import *
# print("Hello")

# def deploy():
#     with settings(host_string="Remote", user = "ubuntu", key_filename="/home/ubuntu/key.pem"):
#         put('/home/localuser/sample.sh', '/home/ubuntu/')
#         run('bash /home/ubuntu/sample.sh')

# if __name__ == '__main__':
#    deploy()
