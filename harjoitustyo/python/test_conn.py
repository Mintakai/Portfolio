import platform     # For getting the operating systems name
import subprocess   # For executing a shell command

def ping(host):

    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of