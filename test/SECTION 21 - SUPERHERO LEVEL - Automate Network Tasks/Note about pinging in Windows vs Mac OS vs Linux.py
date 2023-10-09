When pinging from a Mac OS / Linux (in your Python script) you should always use this syntax in between the parentheses of the call() method:

ping_reply = subprocess.call("ping %s -c 2" % ip)

or, the extended version:

ping_reply = subprocess.call('ping %s -c 2' % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

The -c option is the one to use for specifying the number of echo requests, as per the Linux documentation on ping: https://linux.die.net/man/8/ping



On the other hand, in Windows that would translate to -n to get the same result, as per the Windows documentation on ping: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ping

ping_reply = subprocess.call("ping %s -n 2" % ip)