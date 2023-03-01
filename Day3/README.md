# Day 3

## ⛹️ Lab - Using List variables in Ansible playbooks
```
cd ~/ansible-feb-2023
git pull

cd Day3/loops/list
ansible-playbook playbook.yml
```

Expected output
<pre>
jegan@tektutor.org $ <b>ansible-playbook playbook.yml</b>

PLAY [This playbook will demonstrate use of list variables] ****************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************
ok: [ubuntu1]
ok: [ubuntu2]

TASK [Install software tools] **********************************************************************************************************
ok: [ubuntu1] => (item=vim)
ok: [ubuntu2] => (item=vim)
ok: [ubuntu2] => (item=net-tools)
ok: [ubuntu1] => (item=net-tools)
ok: [ubuntu2] => (item=iputils-ping)
ok: [ubuntu1] => (item=iputils-ping)

PLAY RECAP *****************************************************************************************************************************
ubuntu1                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu2                    : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
</pre>

## ⛹️ Lab - Using Dictionary variables in Ansible playbooks
```
cd ~/ansible-feb-2023
git pull

cd Day3/loops/dictionary
ansible-playbook playbook.yml
```

Expected output
<pre>
jegan@tektutor.org $ <b>ansible-playbook playbook.yml</b>

PLAY [This playbook demonstrates the use of dictionary varibles in Ansible playbook] ***************************

TASK [Gathering Facts] *****************************************************************************************
ok: [localhost]

TASK [debug] ***************************************************************************************************
ok: [localhost] => (item={'key': 'JAVA_HOME', 'value': '/var/lib/jdk8'}) => {
    "msg": "JAVA_HOME ==> /var/lib/jdk8"
}
ok: [localhost] => (item={'key': 'M2_HOME', 'value': '/usr/share/maven'}) => {
    "msg": "M2_HOME ==> /usr/share/maven"
}
ok: [localhost] => (item={'key': 'LOG_PATH', 'value': '/tmp/ansible/ansible.log'}) => {
    "msg": "LOG_PATH ==> /tmp/ansible/ansible.log"
}

PLAY RECAP *****************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
</pre>
