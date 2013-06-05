-----------------------------
New Request management System
-----------------------------

:author:  Krzysztof Daniel Ciba <Krzysztof.Ciba@NOSPAMgmail.com>
:date:    Fri, 28th May 2013
:version: first

Installation
------------

1. Login to host, install ReqDB::

  dirac-install-db ReqDB

2. Install ReqManagerHandler service::

  dirac-install-service RequestManagement/ReqManager

3. Install at least one ReqProxy service::

  dirac-install-service RequestManagement/ReqProxy

and modify CS by adding:

  Systems/RequestManagement/<Configuration>/URLs/ReqProxyURLs = <ReqProxy FQDN1>, <ReqProxy FQDN1>   

4. Install CleanReqDBAgent::

  dirac-install-agent RequestManagement/CleanReqDBAgent

5. Install RequestExecutingAgent::

  dirac-install-agent RequestManagement/RequestExecutingAgent

If one RequestExecutingAgent is not enough (and this is a working horse replacing DISETForwadingAgent, TransferAgent, RemovalAgent and RegistrationAgent),
put in place a few of those.


1. If VO is using FTS system, install FTSDB::

  dirac-install-db FTSDB

2. Stop DataManagement/TransferDBMonitor service and install FTSManagerHandler::

  runsvctrl d runit/DataManagement/TransferDBMonitor
  dirac-install-service DataManagement/FTSManager

3. Configure FTS sites using command dirac-dms-add-ftssite (not included in v6r9-pre1!!!)::

  dirac-dms-add-ftssite SITENAME FTSSERVERURL

In case of LHCb VO::

  dirac-dms-add-ftssite CERN.ch https://fts22-t0-export.cern.ch:8443/glite-data-transfer-fts/services/FileTransfer
  dirac-dms-add-ftssite CNAF.it https://fts.cr.cnaf.infn.it:8443/glite-data-transfer-fts/services/FileTransfer
  dirac-dms-add-ftssite PIC.es https://fts.pic.es:8443/glite-data-transfer-fts/services/FileTransfer
  dirac-dms-add-ftssite RAL.uk https://lcgfts.gridpp.rl.ac.uk:8443/glite-data-transfer-fts/services/FileTransfer
  dirac-dms-add-ftssite SARA.nl https://fts.grid.sara.nl:8443/glite-data-transfer-fts/services/FileTransfer
  dirac-dms-add-ftssite NIKHEF.nl https://fts.grid.sara.nl:8443/glite-data-transfer-fts/services/FileTransfer
  dirac-dms-add-ftssite GRIDKA.de https://fts-fzk.gridka.de:8443/glite-data-transfer-fts/services/FileTransfer
  dirac-dms-add-ftssite IN2P3.fr https://cclcgftsprod.in2p3.fr:8443/glite-data-transfer-fts/services/FileTransfer

4. Install CleanFTSDBAgent::

  dirac-install-agent DataManagement/CleanFTSDBAgent

5. Install FTSAgent::

  dirac-install-agent DataManagement/FTSAgent


Again, as in case of RequestExecutingAgent, if one instance is not enough, you can easily clone it to several instances. 


7. Once all requests from old version of system are processed, shutdown and remove agents:: 

  RequestManagement/DISETForwardingAgent
  RequestManagement/RequestCleaningAgent
  DataManagement/TransferAgent
  DataManagement/RegistrationAgent
  DataManagement/RemovalAgent

and services::

  RequestManagement/RequestManager
  RequestManagement/RequestProxy
  DataManagement/TransferDBMonitor

and dbs::

  RequestManagement/RequestDB
  DataManagement/TransferDB

