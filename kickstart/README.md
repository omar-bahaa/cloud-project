# Content
  1. Front.txt
  2. ks - node.cfg 
  3. ks.cfg
  4. node.txt


## ks and ks - node
1. delete the loggin and make it auto login as root using: <br>
``` bash
  rm -rf /etc/systemd/system/getty.target.wants/getty\@tty1.service
  cp /lib/systemd/system/getty\@.service /etc/systemd/system/getty\@tty1.service
  sed -i "s/ExecStart.*$/ExecStart=-\/sbin\/agetty --autologin root --noclear %I/g" /etc/systemd/system/getty\@tty1.service
  echo ";Alias=getty@tty1.service" >> /etc/systemd/system/getty\@tty1.service
  ln -s /etc/systemd/system/getty\@tty1.service /etc/systemd/system/getty.target.wants/getty\@tty1.service
```

2. make a file to work with the startup because there is no system yet and the script works in the kernel mode
 that is why there are servers and tools not initiated using init.d
 
3. Putting the opennebula automation script in the srwr.sh service on the init.d 
4. The script <code> srwr.sh </code> is called from the network to be edited (Front.txt and node.txt) and integrated with the gui
