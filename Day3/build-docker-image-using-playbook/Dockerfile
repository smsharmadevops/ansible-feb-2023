FROM centos/systemd
MAINTAINER Jeganathan Swaminathan <jegan@tektutor.org> 

RUN yum install -y which openssh-clients openssh-server python3 sudo epel-release openssl certmonger; systemctl enable sshd.service

RUN mkdir -p /var/run/sshd; chmod -rx /var/run/sshd

RUN echo 'root:root' | chpasswd && usermod -aG wheel root

RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key

RUN sed -ri 's/#PermitRootLogin yes/PermitRootLogin yes/g' /etc/ssh/sshd_config

RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/#UsePAM no/UsePAM yes/g' /etc/ssh/sshd_config

RUN echo 'root:root' | chpasswd
RUN usermod -aG wheel root 

RUN mkdir -p /root/.ssh
COPY authorized_keys /root/.ssh/authorized_keys

EXPOSE 22
EXPOSE 80 

ENTRYPOINT ["/usr/sbin/sshd", "-D"]
