#!/usr/bin/python3

# class imports (below is all pyfos classes necessary for pyfos work)
import pyfos.pyfos_auth as pyfos_auth
import pyfos.pyfos_brocade_fibrechannel_switch as pyfos_switch
import pyfos.pyfos_util as pyfos_util
import pyfos.utils.brcd_util as brcd_util

# standard package imports to work with the pyfos information pulled... this could include csv, json, sys, os, etc....
import sys


def main():
    ip_address = '10.0.0.1'  # ip address of switch - edit for IP of switch
    username = 'admin'  # username of switch - edit for username of switch
    password = 'admin'  # password of switch - edit for password of switch

    # logs into the switch and creates an active session with the switch
    session = pyfos_auth.login(username=username,
                               password=password,
                               ip_addr=ip_address,
                               isHttps=True)
    if pyfos_auth.is_failed_login(session):  # if there is a login fail.... please print why...
        '''
            this is where you can put your logging and error handling
        '''
        print("login failed because",
              session.get(pyfos_auth.CREDENTIAL_KEY)
              [pyfos_auth.LOGIN_ERROR_KEY])

        sys.exit()

    switch = pyfos_switch.fibrechannel_switch.get(session)  # creates the switch variable (and its info)
    '''
    pyfos_util.response_print(switch) # Prints out the switch json..... same as the below:
    
    # alternative: I use the below... as I'm trying to change it out to dump into an actual dictionary to play with it.
    print('Switch info:')
    print(switch)
    '''

    #  pyfos_util.response_print(switch)  #  command not used, but could be used to print out switch variable

    pyfos_auth.logout(session)  # logs out of the session to prevent maxing out Rest Sessions....

    print('Switch info:')  # prints switch info.... drop out point to dump into a json dump then dictionary
    print(switch)

    # used as a script pause point (for PyCharm or python editor.... comment this out if running as a script from CLI
    print('script pause')
    print('')

# python script functionality telling python to run whatever is in this script... in this case, run 'main()' above
if __name__ == '__main__':
    main()



