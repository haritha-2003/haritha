commands and modules and parameters

| command | module | parameters |
---------------------------------
| apt update | ansible.builtin.apt | update_cache => true |
| apt upgrade | ansible.builtin.apt | only_upgrade => true |
| apt install openjdk-21 | ansible.builtin.apt | state => present,name => openjdk-21 |
| useradd tomcat | ansible.builtin.user | name => tomcat | 
| 