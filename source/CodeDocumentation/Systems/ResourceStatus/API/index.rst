=======================================
:mod:`ResourceStatusSystem.API` -- APIs
=======================================

.. topic:: Resource Status System APIs
  
  - ResourceStatusAPI 
     - `ResourceStatusAPI.insertSite`_
     - `ResourceStatusAPI.updateSite`_
     - `ResourceStatusAPI.getSite`_
     - `ResourceStatusAPI.deleteSite`_
     - `ResourceStatusAPI.getSitePresent`_
     - `ResourceStatusAPI.insertService`_
     - `ResourceStatusAPI.updateService`_
     - `ResourceStatusAPI.getService`_
     - `ResourceStatusAPI.deleteService`_
     - `ResourceStatusAPI.getServicePresent`_
     - `ResourceStatusAPI.insertResource`_
     - `ResourceStatusAPI.updateResource`_
     - `ResourceStatusAPI.getResource`_
     - `ResourceStatusAPI.deleteResource`_
     - `ResourceStatusAPI.getResourcePresent`_
     - `ResourceStatusAPI.insertStorageElement`_
     - `ResourceStatusAPI.updateStorageElement`_
     - `ResourceStatusAPI.getStorageElement`_
     - `ResourceStatusAPI.deleteStorageElement`_
     - `ResourceStatusAPI.getStorageElementPresent`_
     - `ResourceStatusAPI.insertGridSite`_
     - `ResourceStatusAPI.updateGridSite`_
     - `ResourceStatusAPI.getGridSite`_
     - `ResourceStatusAPI.deleteGridSite`_
     - `ResourceStatusAPI.insertElementStatus`_
     - `ResourceStatusAPI.updateElementStatus`_
     - `ResourceStatusAPI.getElementStatus`_
     - `ResourceStatusAPI.deleteElementStatus`_
     - `ResourceStatusAPI.insertElementScheduledStatus`_
     - `ResourceStatusAPI.updateElementScheduledStatus`_
     - `ResourceStatusAPI.getElementScheduledStatus`_
     - `ResourceStatusAPI.deleteElementScheduledStatus`_
     - `ResourceStatusAPI.insertElementHistory`_
     - `ResourceStatusAPI.updateElementHistory`_
     - `ResourceStatusAPI.getElementHistory`_
     - `ResourceStatusAPI.deleteElementHistory`_
     - `ResourceStatusAPI.getValidElements`_
     - `ResourceStatusAPI.getValidStatuses`_
     - `ResourceStatusAPI.getValidStatusTypes`_
     - `ResourceStatusAPI.getValidSiteTypes`_
     - `ResourceStatusAPI.getValidServiceTypes`_
     - `ResourceStatusAPI.getValidResourceTypes`_
     - `ResourceStatusAPI.addOrModifySite`_
     - `ResourceStatusAPI.addOrModifyService`_
     - `ResourceStatusAPI.addOrModifyResource`_
     - `ResourceStatusAPI.addOrModifyStorageElement`_
     - `ResourceStatusAPI.addOrModifyGridSite`_
     - `ResourceStatusAPI.modifyElementStatus`_
     - `ResourceStatusAPI.removeElement`_
     - `ResourceStatusAPI.getServiceStats`_
     - `ResourceStatusAPI.getResourceStats`_
     - `ResourceStatusAPI.getStorageElementStats`_
     - `ResourceStatusAPI.getGeneralName`_
     - `ResourceStatusAPI.getGridSiteName`_
     - `ResourceStatusAPI.getTokens`_
     - `ResourceStatusAPI.setToken`_
     - `ResourceStatusAPI.setReason`_
     - `ResourceStatusAPI.setDateEnd`_
     - `ResourceStatusAPI.whatIs`_
     - `ResourceStatusAPI.getStuffToCheck`_
     - `ResourceStatusAPI.getMonitoredStatus`_
     - `ResourceStatusAPI.getMonitoredsStatusWeb`_
  - ResourceManagementAPI
     - `ResourceManagementAPI.insertEnvironmentCache`_
     - `ResourceManagementAPI.updateEnvironmentCache`_
     - `ResourceManagementAPI.getEnvironmentCache`_
     - `ResourceManagementAPI.deleteEnvironmentCache`_
     - `ResourceManagementAPI.insertPolicyResult`_
     - `ResourceManagementAPI.updatePolicyResult`_
     - `ResourceManagementAPI.getPolicyResult`_
     - `ResourceManagementAPI.deletePolicyResult`_
     - `ResourceManagementAPI.insertClientCache`_
     - `ResourceManagementAPI.updateClientCache`_
     - `ResourceManagementAPI.getClientCache`_
     - `ResourceManagementAPI.deleteClientCache`_
     - `ResourceManagementAPI.insertAccountingCache`_
     - `ResourceManagementAPI.updateAccountingCache`_
     - `ResourceManagementAPI.getAccountingCache`_
     - `ResourceManagementAPI.deleteAccountingCache`_
     - `ResourceManagementAPI.insertUserRegistryCache`_
     - `ResourceManagementAPI.updateUserRegistryCache`_
     - `ResourceManagementAPI.getUserRegistryCache`_
     - `ResourceManagementAPI.deleteUserRegistryCache`_
     - `ResourceManagementAPI.addOrModifyEnvironmentCache`_
     - `ResourceManagementAPI.addOrModifyPolicyResult`_
     - `ResourceManagementAPI.addOrModifyClientCache`_
     - `ResourceManagementAPI.addOrModifyAccountingCache`_
     - `ResourceManagementAPI.addOrModifyUserRegistryCache`_

------------------------------------------------------------
:mod:`API.ResourceStatusAPI` -- Resource Status API
------------------------------------------------------------

**Source code:** API.ResourceStatusAPI.py_

.. module:: DIRAC.ResourceStatusSystem.API.ResourceStatusAPI
.. autoclass:: ResourceStatusAPI
   :members:  

------------------------------------------------------------
:mod:`API.ResourceManagementAPI` -- Resource Management API
------------------------------------------------------------

**Source code:** API.ResourceManagementAPI.py_

.. module:: DIRAC.ResourceStatusSystem.API.ResourceManagementAPI
.. autoclass:: ResourceManagementAPI
   :members:     
   
.. _API.ResourceStatusAPI.py : https://github.com/ubeda/DIRAC/blob/rssPermissions/ResourceStatusSystem/API/ResourceStatusAPI.py
.. _API.ResourceManagementAPI.py : https://github.com/ubeda/DIRAC/blob/rssPermissions/ResourceStatusSystem/API/ResourceManagementAPI.py


.. _ResourceManagementAPI.insertEnvironmentCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.insertEnvironmentCache
.. _ResourceManagementAPI.updateEnvironmentCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.updateEnvironmentCache
.. _ResourceManagementAPI.getEnvironmentCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.getEnvironmentCache     
.. _ResourceManagementAPI.deleteEnvironmentCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.deleteEnvironmentCache     
.. _ResourceManagementAPI.insertPolicyResult: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.insertPolicyResult     
.. _ResourceManagementAPI.updatePolicyResult: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.updatePolicyResult     
.. _ResourceManagementAPI.getPolicyResult: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.getPolicyResult          
.. _ResourceManagementAPI.deletePolicyResult: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.deletePolicyResult     
.. _ResourceManagementAPI.insertClientCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.insertClientCache     
.. _ResourceManagementAPI.updateClientCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.updateClientCache
.. _ResourceManagementAPI.getClientCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.getClientCache     
.. _ResourceManagementAPI.deleteClientCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.deleteClientCache     
.. _ResourceManagementAPI.insertAccountingCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.insertAccountingCache          
.. _ResourceManagementAPI.updateAccountingCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.updateAccountingCache     
.. _ResourceManagementAPI.getAccountingCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.getAccountingCache     
.. _ResourceManagementAPI.deleteAccountingCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.deleteAccountingCache     
.. _ResourceManagementAPI.insertUserRegistryCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.insertUserRegistryCache     
.. _ResourceManagementAPI.updateUserRegistryCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.updateUserRegistryCache
.. _ResourceManagementAPI.getUserRegistryCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.getUserRegistryCache     
.. _ResourceManagementAPI.deleteUserRegistryCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.deleteUserRegistryCache
.. _ResourceManagementAPI.addOrModifyEnvironmentCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.addOrModifyEnvironmentCache          
.. _ResourceManagementAPI.addOrModifyPolicyResult: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.addOrModifyPolicyResult
.. _ResourceManagementAPI.addOrModifyClientCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.addOrModifyClientCache     
.. _ResourceManagementAPI.addOrModifyAccountingCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.addOrModifyAccountingCache
.. _ResourceManagementAPI.addOrModifyUserRegistryCache: #DIRAC.ResourceStatusSystem.API.ResourceManagementAPI.ResourceManagementAPI.addOrModifyUserRegistryCache          
