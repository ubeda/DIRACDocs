=============================================
:mod:`ResourceStatusSystem.Client` -- Clients
=============================================

.. topic:: Resource Status System Clients
  
  - ResourceStatusClient 
     - `ResourceStatusClient.insertSite`_
     - `ResourceStatusClient.updateSite`_
     - `ResourceStatusClient.getSite`_
     - `ResourceStatusClient.deleteSite`_
     - `ResourceStatusClient.getSitePresent`_
     - `ResourceStatusClient.insertService`_
     - `ResourceStatusClient.updateService`_
     - `ResourceStatusClient.getService`_
     - `ResourceStatusClient.deleteService`_    
     - `ResourceStatusClient.getServicePresent`_
     - `ResourceStatusClient.insertResource`_
     - `ResourceStatusClient.updateResource`_
     - `ResourceStatusClient.getResource`_
     - `ResourceStatusClient.deleteResource`_
     - `ResourceStatusClient.getResourcePresent`_
     - `ResourceStatusClient.insertStorageElement`_
     - `ResourceStatusClient.updateStorageElement`_
     - `ResourceStatusClient.getStorageElement`_
     - `ResourceStatusClient.deleteStorageElement`_
     - `ResourceStatusClient.getStorageElementPresent`_
     - `ResourceStatusClient.insertGridSite`_
     - `ResourceStatusClient.updateGridSite`_
     - `ResourceStatusClient.getGridSite`_
     - `ResourceStatusClient.deleteGridSite`_
     - `ResourceStatusClient.insertElementStatus`_
     - `ResourceStatusClient.updateElementStatus`_
     - `ResourceStatusClient.getElementStatus`_
     - `ResourceStatusClient.deleteElementStatus`_
     - `ResourceStatusClient.insertElementScheduledStatus`_
     - `ResourceStatusClient.updateElementScheduledStatus`_
     - `ResourceStatusClient.getElementScheduledStatus`_
     - `ResourceStatusClient.deleteElementScheduledStatus`_
     - `ResourceStatusClient.insertElementHistory`_
     - `ResourceStatusClient.updateElementHistory`_
     - `ResourceStatusClient.getElementHistory`_
     - `ResourceStatusClient.deleteElementHistory`_
     - `ResourceStatusClient.getValidElements`_
     - `ResourceStatusClient.getValidStatuses`_
     - `ResourceStatusClient.getValidStatusTypes`_
     - `ResourceStatusClient.getValidSiteTypes`_
     - `ResourceStatusClient.getValidServiceTypes`_
     - `ResourceStatusClient.getValidResourceTypes`_
     - `ResourceStatusClient.addOrModifySite`_
     - `ResourceStatusClient.addOrModifyService`_
     - `ResourceStatusClient.addOrModifyResource`_
     - `ResourceStatusClient.addOrModifyStorageElement`_
     - `ResourceStatusClient.addOrModifyGridSite`_
     - `ResourceStatusClient.modifyElementStatus`_
     - `ResourceStatusClient.removeElement`_
     - `ResourceStatusClient.getServiceStats`_
     - `ResourceStatusClient.getResourceStats`_
     - `ResourceStatusClient.getStorageElementStats`_
     - `ResourceStatusClient.getGeneralName`_
     - `ResourceStatusClient.getGridSiteName`_
     - `ResourceStatusClient.getTokens`_
     - `ResourceStatusClient.setToken`_
     - `ResourceStatusClient.setReason`_
     - `ResourceStatusClient.setDateEnd`_
     - `ResourceStatusClient.whatIs`_
     - `ResourceStatusClient.getStuffToCheck`_
     - `ResourceStatusClient.getMonitoredStatus`_
     - `ResourceStatusClient.getMonitoredsStatusWeb`_
  - ResourceManagementClient
     - `ResourceManagementClient.insertEnvironmentCache`_
     - `ResourceManagementClient.updateEnvironmentCache`_
     - `ResourceManagementClient.getEnvironmentCache`_
     - `ResourceManagementClient.deleteEnvironmentCache`_
     - `ResourceManagementClient.insertPolicyResult`_
     - `ResourceManagementClient.updatePolicyResult`_
     - `ResourceManagementClient.getPolicyResult`_
     - `ResourceManagementClient.deletePolicyResult`_
     - `ResourceManagementClient.insertClientCache`_
     - `ResourceManagementClient.updateClientCache`_
     - `ResourceManagementClient.getClientCache`_
     - `ResourceManagementClient.deleteClientCache`_
     - `ResourceManagementClient.insertAccountingCache`_
     - `ResourceManagementClient.updateAccountingCache`_
     - `ResourceManagementClient.getAccountingCache`_
     - `ResourceManagementClient.deleteAccountingCache`_
     - `ResourceManagementClient.insertUserRegistryCache`_
     - `ResourceManagementClient.updateUserRegistryCache`_
     - `ResourceManagementClient.getUserRegistryCache`_
     - `ResourceManagementClient.deleteUserRegistryCache`_
     - `ResourceManagementClient.addOrModifyEnvironmentCache`_
     - `ResourceManagementClient.addOrModifyPolicyResult`_
     - `ResourceManagementClient.addOrModifyClientCache`_
     - `ResourceManagementClient.addOrModifyAccountingCache`_
     - `ResourceManagementClient.addOrModifyUserRegistryCache`_
  - JobsClient
     - `JobsClient.getJobsSimpleEff`_
  - PilotsClient
     - `PilotsClient.getPilotsSimpleEff`_   

------------------------------------------------------------
:mod:`Client.ResourceStatusClient` -- Resource Status Client
------------------------------------------------------------

**Source code:** Client.ResourceStatusClient.py_

.. module:: DIRAC.ResourceStatusSystem.Client.ResourceStatusClient
.. autoclass:: ResourceStatusClient
   :members:  

--------------------------------------------------------------------
:mod:`Client.ResourceManagementClient` -- Resource Management Client
--------------------------------------------------------------------

**Source code:** Client.ResourceManagementClient.py_

.. module:: DIRAC.ResourceStatusSystem.Client.ResourceManagementClient
.. autoclass:: ResourceManagementClient
   :members:  

---------------------------------------
:mod:`Client.JobsClient` -- Jobs Client
---------------------------------------

**Source code:** Client.JobsClient.py_

.. module:: DIRAC.ResourceStatusSystem.Client.JobsClient
.. autoclass:: JobsClient
   :members:  
   
-------------------------------------------
:mod:`Client.PilotsClient` -- Pilots Client
-------------------------------------------

**Source code:** Client.PilotsClient.py_

.. module:: DIRAC.ResourceStatusSystem.Client.PilotsClient
.. autoclass:: PilotsClient
   :members:  
   
.. _Client.ResourceStatusClient.py : https://github.com/ubeda/DIRAC/blob/rssPermissions/ResourceStatusSystem/Client/ResourceStatusClient.py
.. _Client.ResourceManagementClient.py : https://github.com/ubeda/DIRAC/blob/rssPermissions/ResourceStatusSystem/Client/ResourceManagementClient.py
.. _Client.PilotsClient.py : https://github.com/ubeda/DIRAC/blob/rssPermissions/ResourceStatusSystem/Client/PilotsClient.py
.. _Client.JobsClient.py : https://github.com/ubeda/DIRAC/blob/rssPermissions/ResourceStatusSystem/Client/JobsClient.py

.. _JobsClient.getJobsSimpleEff: #DIRAC.ResourceStatusSystem.Client.JobsClient.JobsClient.getJobsSimpleEff 
.. _PilotsClient.getPilotsSimpleEff: #DIRAC.ResourceStatusSystem.Client.PilotsClient.PilotsClient.getPilotsSimpleEff

.. _ResourceStatusClient.insertSite: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.insertSite
.. _ResourceStatusClient.updateSite: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.updateSite
.. _ResourceStatusClient.getSite: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getSite
.. _ResourceStatusClient.deleteSite: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.deleteSite
.. _ResourceStatusClient.getSitePresent: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getSitePresent
.. _ResourceStatusClient.insertService: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.insertService
.. _ResourceStatusClient.updateService: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.updateService
.. _ResourceStatusClient.getService: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getService
.. _ResourceStatusClient.deleteService: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.deleteService
.. _ResourceStatusClient.getServicePresent: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getServicePresent   
.. _ResourceStatusClient.insertResource: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.insertResource
.. _ResourceStatusClient.updateResource: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.updateResource
.. _ResourceStatusClient.getResource: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getResource
.. _ResourceStatusClient.deleteResource: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.deleteResource
.. _ResourceStatusClient.getResourcePresent: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getResourcePresent
.. _ResourceStatusClient.insertStorageElement: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.insertStorageElement
.. _ResourceStatusClient.updateStorageElement: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.updateStorageElement
.. _ResourceStatusClient.getStorageElement: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getStorageElement
.. _ResourceStatusClient.deleteStorageElement: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.deleteStorageElement
.. _ResourceStatusClient.getStorageElementPresent: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getStorageElementPresent
.. _ResourceStatusClient.insertGridSite: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.insertGridSite
.. _ResourceStatusClient.updateGridSite: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.updateGridSite
.. _ResourceStatusClient.getGridSite: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getGridSite
.. _ResourceStatusClient.deleteGridSite: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.deleteGridSite
.. _ResourceStatusClient.insertElementStatus: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.insertElementStatus
.. _ResourceStatusClient.updateElementStatus: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.updateElementStatus
.. _ResourceStatusClient.getElementStatus: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getElementStatus
.. _ResourceStatusClient.deleteElementStatus: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.deleteElementStatus
.. _ResourceStatusClient.insertElementScheduledStatus: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.insertElementScheduledStatus
.. _ResourceStatusClient.updateElementScheduledStatus: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.updateElementScheduledStatus     
.. _ResourceStatusClient.getElementScheduledStatus: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getElementScheduledStatus
.. _ResourceStatusClient.deleteElementScheduledStatus: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.deleteElementScheduledStatus
.. _ResourceStatusClient.insertElementHistory: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.insertElementHistory
.. _ResourceStatusClient.updateElementHistory: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.updateElementHistory
.. _ResourceStatusClient.getElementHistory: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getElementHistory
.. _ResourceStatusClient.deleteElementHistory: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.deleteElementHistory
.. _ResourceStatusClient.getValidElements: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getValidElements
.. _ResourceStatusClient.getValidStatuses: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getValidStatuses
.. _ResourceStatusClient.getValidStatusTypes: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getValidStatusTypes
.. _ResourceStatusClient.getValidSiteTypes: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getValidSiteTypes
.. _ResourceStatusClient.getValidServiceTypes: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getValidServiceTypes
.. _ResourceStatusClient.getValidResourceTypes: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getValidResourceTypes
.. _ResourceStatusClient.addOrModifySite: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.addOrModifySite
.. _ResourceStatusClient.addOrModifyService: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.addOrModifyService
.. _ResourceStatusClient.addOrModifyResource: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.addOrModifyResource
.. _ResourceStatusClient.getValidStatuses: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getValidStatuses
.. _ResourceStatusClient.addOrModifyStorageElement: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.addOrModifyStorageElement     
.. _ResourceStatusClient.addOrModifyGridSite: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.addOrModifyGridSite
.. _ResourceStatusClient.modifyElementStatus: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.modifyElementStatus
.. _ResourceStatusClient.removeElement: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.removeElement
.. _ResourceStatusClient.getServiceStats: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getServiceStats
.. _ResourceStatusClient.getResourceStats: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getResourceStats
.. _ResourceStatusClient.getStorageElementStats: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getStorageElementStats
.. _ResourceStatusClient.getGeneralName: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getGeneralName
.. _ResourceStatusClient.getGridSiteName: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getGridSiteName    
.. _ResourceStatusClient.getTokens: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getTokens
.. _ResourceStatusClient.setToken: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.setToken
.. _ResourceStatusClient.setReason: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.setReason
.. _ResourceStatusClient.setDateEnd: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.setDateEnd
.. _ResourceStatusClient.whatIs: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.whatIs
.. _ResourceStatusClient.getStuffToCheck: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getStuffToCheck
.. _ResourceStatusClient.getMonitoredStatus: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getMonitoredStatus
.. _ResourceStatusClient.getMonitoredsStatusWeb: #DIRAC.ResourceStatusSystem.Client.ResourceStatusClient.ResourceStatusClient.getMonitoredsStatusWeb
       
          
.. _ResourceManagementClient.insertEnvironmentCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.insertEnvironmentCache
.. _ResourceManagementClient.updateEnvironmentCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.updateEnvironmentCache
.. _ResourceManagementClient.getEnvironmentCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.getEnvironmentCache     
.. _ResourceManagementClient.deleteEnvironmentCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.deleteEnvironmentCache     
.. _ResourceManagementClient.insertPolicyResult: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.insertPolicyResult     
.. _ResourceManagementClient.updatePolicyResult: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.updatePolicyResult     
.. _ResourceManagementClient.getPolicyResult: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.getPolicyResult          
.. _ResourceManagementClient.deletePolicyResult: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.deletePolicyResult     
.. _ResourceManagementClient.insertClientCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.insertClientCache     
.. _ResourceManagementClient.updateClientCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.updateClientCache
.. _ResourceManagementClient.getClientCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.getClientCache     
.. _ResourceManagementClient.deleteClientCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.deleteClientCache     
.. _ResourceManagementClient.insertAccountingCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.insertAccountingCache          
.. _ResourceManagementClient.updateAccountingCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.updateAccountingCache     
.. _ResourceManagementClient.getAccountingCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.getAccountingCache     
.. _ResourceManagementClient.deleteAccountingCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.deleteAccountingCache     
.. _ResourceManagementClient.insertUserRegistryCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.insertUserRegistryCache     
.. _ResourceManagementClient.updateUserRegistryCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.updateUserRegistryCache
.. _ResourceManagementClient.getUserRegistryCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.getUserRegistryCache     
.. _ResourceManagementClient.deleteUserRegistryCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.deleteUserRegistryCache
.. _ResourceManagementClient.addOrModifyEnvironmentCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.addOrModifyEnvironmentCache          
.. _ResourceManagementClient.addOrModifyPolicyResult: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.addOrModifyPolicyResult
.. _ResourceManagementClient.addOrModifyClientCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.addOrModifyClientCache     
.. _ResourceManagementClient.addOrModifyAccountingCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.addOrModifyAccountingCache
.. _ResourceManagementClient.addOrModifyUserRegistryCache: #DIRAC.ResourceStatusSystem.Client.ResourceManagementClient.ResourceManagementClient.addOrModifyUserRegistryCache          
 