# Day 4

## Lab - Writing a custom Ansible module and invoking it from a playbook
```
cd ~/ansible-feb-2023
git pull

cd Day4/custom-ansible-module
ansible-playbook playbook.yml
```

Expected output
<pre>
jegan@tektutor.org:~/ansible-feb-2023/Day4/custom-ansible-module$ <b>tree</b>
.
├── library
│   └── hello.py
└── playbook.yml

1 directory, 2 files
jegan@tektutor.org:~/ansible-feb-2023/Day4/custom-ansible-module$ <b>ansible-playbook playbook.yml</b>
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match
'all'

PLAY [Demonstrates invoking our Custom Ansible module] *******************************************************************

TASK [Gathering Facts] ***************************************************************************************************
ok: [localhost]

TASK [Invoke custom hello module] ****************************************************************************************
changed: [localhost]

TASK [debug] *************************************************************************************************************
ok: [localhost] => {
    "output": {
        "changed": true,
        "failed": false,
        "output": "Hello Custom Ansible Module!"
    }
}

PLAY RECAP ***************************************************************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
</pre>
