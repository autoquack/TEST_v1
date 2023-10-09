Log in to each Arista network device and use the commands below in order to have connectivity set up.



Arista1

enable

configure terminal

username admin secret python

hostname Arista1

interface Management 1

ip address 10.10.10.2 255.255.255.0

no shutdown

copy run start



Arista2

enable

configure terminal

username admin secret python

hostname Arista2

interface Management 1

ip address 10.10.10.3 255.255.255.0

no shutdown

copy run start



Arista3

enable

configure terminal

username admin secret python

hostname Arista3

interface Management 1

ip address 10.10.10.4 255.255.255.0

no shutdown

copy run start





If you need to connect to Cisco IOS devices as well, here's the SSH configuration you need to make on each router.

Modify the username, password, domain-name and hostname according to your needs.



username mihai privilege 15 password python

!

line vty 0 4

privilege level 15

login local

transport input telnet ssh

!

exit

!

enable secret python

!

ip domain-name mihai

!

hostname Cisco-R1

!

!When asked How many bits in the modulus [512]: enter 1024

crypto key generate rsa

1024

!

ip ssh version 2

ip ssh time-out 60

ip ssh authentication-retries 3

!