----------------------------------
Request Manager and RequestProxies
----------------------------------

:author:  Krzysztof Daniel Ciba <Krzysztof.Ciba@NOSPAMgmail.com>
:date:    Tue, 18th Jan 2013
:version: first and final

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
all over the world, preferably close to the biggest CEs or SEs used in the community. Take the LHCb VO as an example, where
each of Tier1 is running its own RequestProxy.

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
        ## the only one URL to RequestManagerHandler
        RequestManager = dips://<central>:9143/RequestManagement/RequestManager
        ## comma separated list to all RequestProxyHandlers
        RequestProxyURLs = dips://<hostA>:9161/RequestManagement/RequestProxy, dips://<hostB>:9161/RequestManagement/RequestProxy
      }
    }
  }

 
Don't forget to put correct FQDNs instead of <central>, <hostA>, <hostB> in above example!   

 


