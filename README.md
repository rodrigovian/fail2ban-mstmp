# fail2ban-mstmp

#### Using rpm package
Build package  
```
rpmbuild -bb fail2ban-msmtp.spec
```

Install package
```
yum localinstall fail2ban-msmtp-0.1.1-1.el7.noarch
dnf localinstall fail2ban-msmtp-0.1.1-1.el9.noarch
```

#### For install manually
Copy all files inside src directory to /etc/fail2ban/action.d  

#### Config
In your jail.local, use:
```
mta = msmtp
```
