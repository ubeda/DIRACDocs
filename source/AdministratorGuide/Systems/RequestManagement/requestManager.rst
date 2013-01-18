----------------------------------
Request Manager and RequestProxies
----------------------------------

:author:  Krzysztof Daniel Ciba <Krzysztof.Ciba@NOSPAMgmail.com>
:date:    Fri, 18th Jan 2013
:version: first

Overview
--------

The RequestManager service is a handler for RequestDB using DISET protocol. It exposes all CRUD operations on requests (creating, reading, 
updating and deleting) plus several helper functions like getting requests/subrequest attributes, exposing some useful information 
to the web interface/scripts and so on.

The RequestProxy is a simple service which start to work only if RequestManager is down for some reason and newly created request cannot be
inserted to the RequestDB. To prevent loosing os such request, the RequestClient is trying automatically connect to one of the RequestProxies, where
the request is serialised to the XML and dumped ot the file int the local file system for further processing. A separate background thread in the 
RequestProxy instance will then try periodically to connect to the RequestManager, forwading saved request to the place they can 
be picked up and executed.  

.. image:: ../../../_static/Systems/RMS/RequestProxy-flow.png
   :alt: Request's forwarding in DIRAC.
   :align: center 

Installation
------------

For the proper request processing there should be only one central RequestManager 
service up and running - prefereably close to the hosts on which request processing 
agents (DISETForwardingAgent, RequestCleaningAgent from RequestManagement, TransferAgent, 
RegistrationAgent and RemovalAgent from DataManagement and so on) are running. 

For the RequestProxies situation is quite oposite: they should be installed in the several different places 
all over the world, preferably close to the biggest CEs or SEs used in the community. Take the LHCb VO as 
an example, where each of Tier1 is running its own RequestProxy. Please also notice that you have to have at 
least one RequesyProxy running somewhere for normal operation, preferably not on the node used by RequestManager 
service. 

Example configuration::

  Systems { 
    RequestManagement {
      Services {
        RequestManager {
          LogLevel = INFO
          HandlerPath = DIRAC/RequestManagementSystem/Service/RequestManagerHandler.py
          Port = 9143
          Protocol = dips
          Backend = mysql
          Authorization {
            Default = authenticated
          }
        RequestProxy {
          LogLevel = INFO
          HandlerPath = DIRAC/RequestManagementSystem/Service/RequestProxyHandler.py
          Port = 9161
          Protocol = dips
          Authorization {
            Default = authenticated
          }
        }
      }
      URLs {
        ## the only instance of RequestManagerHandler
        RequestManager = dips://<central>:9143/RequestManagement/RequestManager
        ## comma separated list to all RequestProxyHandlers
        RequestProxyURLs = dips://<hostA>:9161/RequestManagement/RequestProxy, dips://<hostB>:9161/RequestManagement/RequestProxy
      }
    }
  }

 
Don't forget to put correct FQDNs instead of <central>, <hostA>, <hostB> in above example!   


Upgrading from DIRAC v6r5
-------------------------

The DIRAC releases prior to v6r6 were using different model for request forwarding: each CE 
was able to run its own RequestManager (local), preferebly with the file backend (which BTW is obsolete now). 
Requests created by jobs were put to the local RequestDB using local RequestManager URL. A separate locally running 
ZuziaAgent [#]_ was picking them up and sending to the central RequestManager service.

For upgrading from the old to the new forwarding model you should follow this procedure:

* install and configure the RequestProxy service in all the places where ZuziaAgent is running, make sure 
  the port used by this service (9161) is visible to the outside world
* stop ZuziaAgent when no more requests are held in the local RequestDB
* stop local RequestManager
* update DIRAC configuration by adding RequestProxy FQDN to the RequestProxyURLs 
  and removing ZuziaAgent and local RequestManager sections 
  

.. rubric:: Footnotes
 
.. [#] Zuzia is a little Susan in Polish, the given name of a daugther of DIRAC team developer who had left the project a few years ago. 


