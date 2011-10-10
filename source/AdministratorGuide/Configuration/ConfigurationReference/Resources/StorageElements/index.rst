Resources / StorageElement - Subsections
========================================

All the storages elements available for the users are described in this subsection.

+---------------------------------------------+--------------------------------------------------+-----------------------------+
| **Name**                                    | **Description**                                  | **Example**                 |
+---------------------------------------------+--------------------------------------------------+-----------------------------+
| *DefaultProtocols*                          | Default protocols than can be used to interact   | DefaultProtocols = rfio     |
|                                             | with the storage elements.                       | DefaultProtocols += file    |
|                                             |                                                  | DefaultProtocols += root    |
|                                             |                                                  | DefaultProtocols += gsiftp  |
+---------------------------------------------+--------------------------------------------------+-----------------------------+
| *SITE-disk*                                 | Subsection. DIRAC name for the storage element   | CPPM-disk                   |
+---------------------------------------------+--------------------------------------------------+-----------------------------+
| *SITE-disk/BackendType*                     | Type of storage element. Possible values are:    | BackendType = dpm           |
|                                             | dmp, DISET                                       |                             |
+---------------------------------------------+--------------------------------------------------+-----------------------------+
| *SITE-disk/AccessProtocol.<#>*              | Subsection. Access protocol number               | AccessProtocol.1            |
+---------------------------------------------+--------------------------------------------------+-----------------------------+
| *SITE-disk/AccessProtocol.<#>/Access*       | Access type to the resource                      | Access = Remote             |
+---------------------------------------------+--------------------------------------------------+-----------------------------+
| *SITE-disk/AccessProtocol.<#>/Host*         | Storage element fully qualified hostname         | Host = se01.in2p3.fr        |
+---------------------------------------------+--------------------------------------------------+-----------------------------+
| *SITE-disk/AccessProtocol.<#>/Path*         | Path in the SE just before the VO directory      | Path = /dpm/in2p3.fr/home   |
+---------------------------------------------+--------------------------------------------------+-----------------------------+
| *SITE-disk/AccessProtocol.<#>/Port*         | Port number to access the data                   | Port = 8446                 |
+---------------------------------------------+--------------------------------------------------+-----------------------------+
| *SITE-disk/AccessProtocol.<#>/Protocol*     | Protocol to be used to interact with the SE      | Protocol = srm              |
+---------------------------------------------+--------------------------------------------------+-----------------------------+
| *SITE-disk/AccessProtocol.<#>/ProtocolName* | Protocol name to be used to interact with the SE | ProtocolName = SRM2         |
+---------------------------------------------+--------------------------------------------------+-----------------------------+
| *SITE-disk/AccessProtocol.<#>/WSUrl*        | URL from WebServices                             | WSUrl = /srm/managerv2?SFN= |
+---------------------------------------------+--------------------------------------------------+-----------------------------+
