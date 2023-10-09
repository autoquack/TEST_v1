Here's a short guide for you to connect your local macOS system to the Arista VMs. Of course, you should still configure the IP addresses on the Arista VMs as shown in the Connecting the Local PC to the Devices in Windows video (minutes 1:40 up to 3:25). I am using a macOS High Sierra 10.13.1 for this guide.



1. General Host-Only Network settings

1.1. In VirtualBox, go to the Global Tools menu.


1.2. Go to Host Network Manager.


1.3. Make sure you have the vboxnet0 host-only network created. If it is not created, then you should go ahead and click on the Create button (green plus icon).


1.4. As soon as you hit Create, vboxnet0 will be created.


1.5. Click on Properties, go to the DHCP Server tab and uncheck the Enable Server checkbox, then click Apply.


1.6. On the Adapter tab, click on Configure Adapter Manually and set 10.10.10.1 for the IPv4 Address and 255.255.255.0 for the IPv4 Network Mask, then click Apply.




2. Arista VM network settings

2.1. In VirtualBox, select each Arista VM and click on Settings.


2.2. Go to the Network tab and then go to Adapter 1. Make sure that you check the Enable Network Adapter checkbox. Next, from the Attached to: drop-down menu select Host-only Adapter.


2.3. Then, from the Name: drop-down menu make sure that vboxnet0 is selected. Hit OK and repeat the same steps for all your Arista VMs. Again, don't forget to also configure the IP addresses on the Arista VMs.




Hope that helps and if you have any suggestions or issues regarding these steps please feel free to post in the Q&A area.