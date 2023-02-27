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

## What is Hypervisor?
- Virtualization Technology
- Processors
  Intel
  - Virtualization feature is called VT-X
  AMD
  - Virtualization feature is called AMD-V
- The OS on which the Virtualization software is installed is called Host OS
- The OS installed within the Virtual Machine is called Guest OS
- There are 2 types 
  1. Type1 - used in Servers/Workstation - this doesn't require a OS - can be installed on bare-metal
     - VMWare vCenter/vSphere
  2. Type2 - used in Laptops/Desktops/Workstation - this requires a Host OS ( Windows, Linux, Mac )
     - VMWare Workstation
     - KVM
     - Parallels
     - Oracle VirtualBox
     - Microsoft Hyper-V
- for each Guest OS, we need to allocate dedicated
  - CPU Cores
  - RAM and
  - Storage
- hence, this type of Virtualization is called Heave-weight Virtualization
- allowed consolidation of many physical servers into few/some physical servers
- Servers will have multiple Processor Socket
- Processors comes in different form factor/packaging
- each Virtual Machine represents one fully function Operating System that has 
   - OS Kernel
   - dedicated Hardware resources ( CPU, RAM, Storage, Network & Graphics Cards, etc.,)
   
  1. SCM (Single Chip Module)
     - One IC will have just one Processor
  2. MCM (Multiple Chip Module)
     - One IC will have many Processors
    
- each Processors might have many CPU Cores
- There are Server motherboard with 8 Sockets 
   - If each Socket supports MCM with let's 4 Processor's, 4 x 8 Sockets = 32 Processors
   - If each Processor supports 128 Cores, then 32 Processors x 128 Cores = 4096 Physical Cores
   - HyperThreading technology supports running 2 or more threads parallely in each Physical core
   - each Physical core is seen by the OS/Virtualization software as 2 virtual cores
   - modern server grade Processors supports upto 4 virtual cores per Physical Processor
   - 4096 Physical cores x 2 = 8192 virtual Cores

## What is Docker?
- is an application virtualization technology
- Docker containers represent one single application
- container is an application process
- it is not an Operating System
- they don't have their own OS Kernel
- they don't have their own dedicated Hardware resources
- containers shares the OS Kernel from the underlying Host OS
- containers shares the hardware resources available on the Host OS
- that is why they are called lightweight virtualization technology
- easily we can create 30~40 containers in a normal laptop/desktop

## What is the technology that enables Containerization?
- containerization is a Linux technology
- Linux Kernels supports
  1. Namespace
     - allows to isolate one container from the other containers
  2. Control Groups (CGroups)
     - allows to apply resource quota restrictions on individual containers
     - example
       - we can restrict how many cpu cores at max a container can utilize
       - we can restrict the max amount of RAM a container can use
       - can restrict the max storage capacity
- Docker is supported in Linux/Unix/Mac/Windows
- When we install Docker for Windows/Mac, it installs a thin linux layer(Linux kernel), which means the linux application containers continues to run on Linux even on Windows/Mac machines.
- Microsoft OS Kernel can't be separated from the OS, it is not modular, OS Kernel and the OS itself is strongly coupled, hence we can't separate out the Microsoft OS Kernel alone
- It is for this reason, Linux doesn't support running a .Net application containers on Unix/Linux/Mac.

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


## Let's create a Custom Ubuntu Ansible Node Docker Image
```
cd ~/ansible-feb-2023
git pull
cd Day1/CustomAnsibleDockerImages/ubuntu
ssh-keygen
cp ~/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/ansible-ubuntu-node:latest .
```

Expected output
<pre>
jegan@tektutor.org $ <b>docker build -t tektutor/ubuntu-ansible-node:latest .</b>

[+] Building 2.2s (13/13) FINISHED                                                                                                      
 => [internal] load .dockerignore                                                                                                  0.0s
 => => transferring context: 2B                                                                                                    0.0s
 => [internal] load build definition from Dockerfile                                                                               0.0s
 => => transferring dockerfile: 669B                                                                                               0.0s
 => [internal] load metadata for docker.io/library/ubuntu:16.04                                                                    0.0s
 => [1/8] FROM docker.io/library/ubuntu:16.04                                                                                      0.0s
 => [internal] load build context                                                                                                  0.0s
 => => transferring context: 675B                                                                                                  0.0s
 => CACHED [2/8] RUN apt-get update && apt-get install -y openssh-server python3                                                   0.0s
 => [3/8] RUN mkdir /var/run/sshd                                                                                                  0.3s
 => [4/8] RUN echo 'root:root' | chpasswd                                                                                          0.4s
 => [5/8] RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config                               0.4s
 => [6/8] RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd                   0.4s
 => [7/8] RUN mkdir -p /root/.ssh                                                                                                  0.4s
 => [8/8] COPY authorized_keys /root/.ssh/authorized_keys                                                                          0.1s
 => exporting to image                                                                                                             0.1s
 => => exporting layers                                                                                                            0.1s
 => => writing image sha256:9631602e39f4d8a3f13bf67c5bbe24095a2a88a3fe61197e00aed6052aaf6430                                       0.0s
 => => naming to docker.io/tektutor/ubuntu-ansible-node:latest                                                                     0.0s
 
jegan@tektutor.org $ <b>docker images</b>
REPOSITORY                                TAG       IMAGE ID       CREATED         SIZE
<b>tektutor/ubuntu-ansible-node              latest    9631602e39f4   5 seconds ago   220MB</b>
ubuntu                                    16.04     b6f507652425   18 months ago   135MB
</pre>
