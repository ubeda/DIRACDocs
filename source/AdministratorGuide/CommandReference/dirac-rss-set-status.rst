===========================
dirac-rss-set-status
===========================

  ==============================================================================

  DIRAC v6r7

  dirac-rss-set-status

  

    Script that facilitates the modification of a element through the command line.

    However, the usage of this script will set the element token to the command

    issuer with a duration of 1 day.

    

Usage::

      dirac-rss-set-status

        --element=            Element family to be Synchronized ( Site, Resource or Node )

        --name=               Name, name of the element where the change applies

        --statusType=         StatusType, if none applies to all possible statusTypes

        --status=             Status to be changed

        --reason=             Reason to set the Status         

            

    Verbosity:

        -o LogLevel=LEVEL     NOTICE by default, levels available: INFO, DEBUG, VERBOSE..        

  ==============================================================================

 

 

Options::

  -    --element=        : Element family to be Synchronized ( Site, Resource or Node ) 

  -    --name=           : Name, name of the element where the change applies 

  -    --statusType=     : StatusType, if none applies to all possible statusTypes 

  -    --status=         : Status to be changed 

  -    --reason=         : Reason to set the Status 


