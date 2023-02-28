# Day2

## Installing nginx web server in ubuntu ansible nodes via an Ansible Playbook
```
cd ~/ansible-feb-2023
git pull

cd Day2
ansible-playbook install-nginx-playbook.yml
```

Expected output
<pre>
jegan@tektutor.org $ <b>ansible-playbook install-nginx-playbook.yml</b>

PLAY [This playbook will install,configure nginx web server and will deploy a custom web page into custom web root folder] *************

TASK [Gathering Facts] *****************************************************************************************************************
ok: [ubuntu1]
ok: [ubuntu2]

TASK [Install nginx Web Server in Ubuntu] **********************************************************************************************
changed: [ubuntu1]
changed: [ubuntu2]

PLAY RECAP *****************************************************************************************************************************
ubuntu1                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu2                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
</pre>
