# Day 1

## What is Configuration Management Tool?
- are used to automate software installation and configuration
- in most cases, software installation automation is done on a already provisioned machine
- Examples
  - Puppet
  - Chef
  - Salt/SaltStack
  - Ansible
- Idempotent

## Puppet/Chef
- follows client/Server architecture
- Puppet/Chef Agent
  - special proprietary softwares that has to installed on the servers where the software installation/configuration automation must be performed
- Chef uses a proprietary tool called knife to push/copy the automation script (recipe) to the Chef Agent
- the language in which the automation code is written that is referred as DSL(Domain Specific Language)
- DSL used is Ruby
- advantages
  - can handle any complex software installation/configuration management 
- disadvantages
  - wrong choice of DSL, hence learning curve for Chef/Puppet is steep
  - installation is also complex
  - follows PULL based architecture

## Ansible
- agentless
  - doesn't require any special proprietary software on the ansible nodes where software installation automation must be done
- doesn't follow client/server architecture
- DSL used in Ansible is YAML (Yet Another Markup Language - Superset of JSON)
- follows simple architecture
  - uses existing tools to achieve the software installation/configuration management
- Ansible Modules
  - Ansible uses ansible modules to perform the automation
  - Ansible modules supported for Unix/Linux/Mac Ansible nodes are Python scripts
  - Ansible modules supported for Windows Ansible nodes are PowerShell scripts
  - Examples
    - copy module helps copying files from local machine to the Ansible node or vice versa
    - shell module helps running shell commands on the Unix/Linux/Mac Ansible nodes
    - service to manage services in Unix/Linux/Mac
    - apt module helps in software installation/uninstallation/ugrade on Debain based ansible nodes
    - yum module helps in software installation/uninstallation/upgrade on Red Hat OS family

# Ansible Commands

## Finding the ansible version
```
ansible --version
```
Expected output
<pre>
 jegan@tektutor.org $ <b>ansible --version</b>
ansible [core 2.14.2]
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/jegan/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3.11/site-packages/ansible
  ansible collection location = /home/jegan/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/bin/ansible
  python version = 3.11.1 (main, Jan  6 2023, 00:00:00) [GCC 12.2.1 20221121 (Red Hat 12.2.1-4)] (/usr/bin/python3)
  jinja version = 3.0.3
  libyaml = False
</pre>

## Verifying docker version and test if docker commands are working without any permission issues
```
docker --version
docker images
```

Expected output
<pre>
jegan@tektutor.org $ <b>docker --version</b>
Docker version 23.0.1, build a5ee5b1

jegan@tektutor.org $ <b>docker images</b>
REPOSITORY                                TAG       IMAGE ID       CREATED         SIZE
tektutor/ansible-centos-node              latest    77826cd90477   2 days ago      220MB
tektutor/ansible-ubuntu-node              latest    77826cd90477   2 days ago      220MB
bitnami/prometheus                        latest    0b5d3ab5c074   3 days ago      312MB
bitnami/grafana                           latest    8ad8324f3626   3 days ago      446MB
bitnami/mysql                             latest    85ae5eff30c3   5 days ago      515MB
csanchez/maven                            latest    6701ab932f19   9 days ago      528MB
docker.bintray.io/jfrog/artifactory-oss   latest    4809cef53f93   2 weeks ago     1.48GB
postgres                                  12        2c278af658a7   2 weeks ago     373MB
redis                                     latest    2f66aad5324a   2 weeks ago     117MB
nginx                                     latest    3f8a00f137a0   2 weeks ago     142MB
sonarqube                                 latest    27d02b3b63c0   3 weeks ago     614MB
hello-world                               latest    feb5d9fea6a5   17 months ago   13.3kB
centos                                    8         5d0da3dc9764   17 months ago   231MB
ubuntu                                    16.04     b6f507652425   18 months ago   135MB
ansible/awx                               17.1.0    599918776cf2   23 months ago   1.41GB
</pre>
