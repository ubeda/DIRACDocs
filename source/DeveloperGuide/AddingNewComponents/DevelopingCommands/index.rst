======================================
Developing Commands
======================================

Commands are one of the main interface tools for the users. Commands are also called *scripts* in DIRAC lingo. 

Where to place scripts
------------------------

All scripts should live in the *scripts* directory of their parent system. For instance, the command:: 

  dirac-wms-job-submit

will live in::

  DIRAC/WorkloadManagementSystem/scripts/dirac-wms-job-submit.py

The command script name is the same as the command name itself with the *.py* suffix appended. When DIRAC client software
is installed, all scripts will be placed in the installation scripts directory and stripped of the *.py* extension. 
This way users can see all the scripts in a single place and it makes easy to include all the scripts in the 
system PATH variable.

Coding commands
------------------

All the commands should be coded following a common recipe and having several mandatory parts. The instructions
below must be applied as close as possible although some variation are allowed according to developer's habits. 

**1.** All scripts must start with a Shebang line like the following::

    #!/usr/bin/env python

which will set the interpreter directive to the python on the environment.
  
**2.** The next is the documentation line which is describing the command. This same documentation line
will be used also the command help information available with the *-h* command switch.   

**3.** Users need to specify parameters to scripts to define what they want to do. To do so, 
they pass arguments when calling the script. The first thing any script has to do is define what 
options and arguments the script accepts. Once the valid arguments are defined, the script can parse 
the command line. An example follows which is a typical command description part::

    #!/usr/bin/env python
    
    """  Ping a list of services and show the result
    """

    __RCSID__ = "$Id$
    
    import sys
    from DIRAC import S_OK, S_ERROR, gLogger, exit
    from DIRAC.Core.Base import Script
    
    # Define a simple class to hold the script parameters
    class Params:
    
      def __init__( self ):
        self.raw = False
        self.pingsToDo = 1
      
      def setRawResult( self, value ):
        self.raw = True
        return S_OK()
    
      def setNumOfPingsToDo( self, value ):
        try:
          self.pingsToDo = max( 1, int( value ) )
        except ValueError:
          return S_ERROR( "Number of pings to do has to be a number" )
        return S_OK()
    
    # Instantiate the params class
    cliParams = Params()
    
    # Register accepted switches and their callbacks
    Script.registerSwitch( "r", "showRaw", "show raw result from the query", cliParams.setRawResult )
    Script.registerSwitch( "p:", "numPings=", "Number of pings to do (by default 1)", cliParams.setNumOfPingsToDo )
    
    # Define a help message
    Script.setUsageMessage( '\n'.join( [ __doc__,
                                         'Usage:',
                                         '  %s [option|cfgfile] <system name to ping>+' % Script.scriptName,
                                         '  Specifying a system is mandatory' ] ) )
    
    # Parse the command line and initialize DIRAC
    Script.parseCommandLine( ignoreErrors = False )

    # Get the list of services
    servicesList = Script.getPositionalArgs()

    # Check and process the command line switches and options
    if len( servicesList ) == 0:
      Script.showHelp()
      exit(1)

Let's follow the example step by step. First, we import the required modules from DIRAC. 
*S_OK* and *S_ERROR* are the default way DIRAC modules return values or errors. The *Script* module 
is the initialization and command line parser that scripts use to initialize themselves. 
**No other DIRAC module should be imported here**.

Once the required modules are imported, a *Params* class is defined. This class holds the values 
for all the command switches together with all their default values. When the class is instantiated, 
the parameters get the default values in the constructor function. It also has a set of functions 
that will be called for each switch that is specified in the command line. We'll come back to that later.

Then the list of valid switches and what to do in case they are called is defined using *registerSwtch()* method of the
Scripts module. Each switch definition has 4 parameters:

#. Short switch form. It has to be one letter. Optionally it can have ':' after the letter. 
   If the switch has ':' it requires one parameter with the switch. A valid combination for the previous 
   example would be '-r -p 2'. That means show raw results and make 2 pings.
#. Long switch form. '=' is the equivalent of ':' for the short form. The same combination of command switches in a long form
   will look like '--showRaw --numPings 2'.
#. Definition of the switch. This text will appear in the script help.
#. Function to call if the user uses the switch in order to process the switch value

There are several reserved switches that DIRAC uses by default and cannot be overwritten by the script. Those are:

* *-h* and *--help* show the script help
* *-d* and *--debug* enables debug level for the script. Note that the forms *-dd* and *-ddd* are accepted
  resulting in increasingly higher verbosity level
* *-s* and *--section* changes the default section in the configuration for the script
* *-o* and *--option* set the value of an option in the configuration
* *-c* and *--cert* use certificates to connect to services

All the command line arguments that are not corresponding to the explicitly defined switches are returned
by the *getPositionalArguments()* function.

After defining the switches, the *parseCommandLine()* function has to be called. This method not only parses 
the command line options but also initializes DIRAC collecting all the configuration data. 
**It is absolutely important to call this function before importing any other DIRAC module**. 
The callbacks defined for the switches will be called when parsing the command line if necessary. 
*Even if the switch is not supposed to receive a parameter, the callback has to receive a value*.
Switches without callbacks defined can be obtained with *getUnprocessedSwitches()* function.

**4.** Once the command line has been parsed and DIRAC is properly initialized, the rest of the required 
DIRAC modules can be imported and the script logic can take place::

    #Import the required DIRAC modules
    from DIRAC.Interfaces.API.DIRAC import DIRAC
    from DIRAC import gLogger
    #Do stuff... depending on cliParams.raw, cliParams.pingsToDo and servicesList
    
    def executeCommandLogic()
      # Do stuff
      gLogger.notice('This is the result of the command')
      
    if __name__ == "__main__":
      
      executeCommandLogic()  
    
Having understood the logic of the script, there are few good practices that must be followed:

* Use *DIRAC.exit( exitCode )* instead of *sys.exit( exitCode )*
* Encapsulate the command code into functions / classes so that it can be easily tested
* Usage of *gLogger* instead of *print* is mandatory. The information in the normal command execution 
  must be printed out in the NOTICE logging level.  
* Use the *if __name__ == "__main__"* close for the actual command execution to avoid running the script 
  when it is imported.

Example command
-----------------

Applying all the above recommendations, the command implementation can look like this yet another example::

    #!/usr/bin/env python
    
    """
      dirac-my-great-script
      
        This script prints out how great is it, shows raw queries and sets the
        number of pings.
        
        Usage:
          dirac-my-great-script [option|cfgfile] <Arguments>
        Arguments:
          <service1> [<service2> ...]  
    """
    
    from DIRAC           import S_OK, S_ERROR, gLogger, exit as DIRACExit
    from DIRAC.Core.Base import Script
    
    __RCSID__ = '$Id$'
    
    cliParams  = None
    switchDict = None
   
    class Params:
      '''
        Class holding the parameters raw and pingsToDo, and callbacks for their
        respective switches.
      '''
      
      def __init__( self ):
        self.raw = False
        self.pingsToDo = 1
      
      def setRawResult( self, value ):
        self.raw = True
        return S_OK()
    
      def setNumOfPingsToDo( self, value ):
        try:
          self.pingsToDo = max( 1, int( value ) )
        except ValueError:
          return S_ERROR( "Number of pings to do has to be a number" )
        return S_OK()
     
    def registerSwitches():
      '''
        Registers all switches that can be used while calling the script from the
        command line interface.
      '''
    
      #Some of the switches have associated a callback, defined on Params class.
      cliParams = Params()
    
      switches = [
                  ( '', 'text=', 'Text to be printed' ),
                  ( 'u', 'upper', 'Print text on upper case' ),
                  ( 'r', 'showRaw', 'Show raw result from the query', cliParams.setRawResult ),
                  ( 'p:', 'numPings=', 'Number of pings to do (by default 1)', cliParams.setNumOfPingsToDo )
                 ]
    
      # Register switches
      for switch in switches:
        Script.registerSwitch( *switch )
        
      #Define a help message
      Script.setUsageMessage( __doc__ )
    
    def parseSwitches():
      '''
        Parse switches and positional arguments given to the script
      '''
          
      #Parse the command line and initialize DIRAC
      Script.parseCommandLine( ignoreErrors = False )

      #Get the list of services
      servicesList = Script.getPositionalArgs()

      gLogger.info( 'This is the servicesList %s:' % servicesList )

      # Gets the rest of the 
      switches = dict( Script.getUnprocessedSwitches() )

      gLogger.debug( "The switches used are:" )
      map( gLogger.debug, switches.iteritems() )
     
      switches[ 'servicesList' ] = servicesList
     
      return switches

    def main():
      '''
        This is the script main method, which will hold all the logic.
      '''
    
      # let's do something
      if not len( switchDict[ 'servicesList' ] ):
        gLogger.error( 'No services defined' )
        DIRACExit( 1 ) 
      gLogger.notice( 'We are done' )  
    
    if __name__ == "__main__":

      # Script initialization
      registerSwitches()
      switchDict = parseSwitches()
      
      #Import the required DIRAC modules
      from DIRAC.Interfaces.API.Dirac import Dirac
       
      # Run the script
      main()
   
      # Bye
      DIRACExit( 0 )
    