Systems / RequestManagement / <INSTANCE> / Databases - Sub-subsection
==================================================================

Databases used by RequestManagement System. Note that each database is a separate subsection.

+--------------------------------+----------------------------------------------+----------------------+
| **Name**                       | **Description**                              | **Example**          |
+--------------------------------+----------------------------------------------+----------------------+
| *<DATABASE_NAME>*              | Subsection. Database name                    | RequestDB            |
| *<DATABASE_NAME>/DBName*       | Database name                                | DBName = RequestDB   |
| *<DATABASE_NAME>/Host*         | Database host server where the DB is located | Host = db01.in2p3.fr |
| *<DATABASE_NAME>/MaxQueueSize* | Maximum number of simultaneous queries to the DB per instance of the client | MaxQueueSize = 10    |
+--------------------------------+----------------------------------------------+----------------------+

The databases associated to RequestManagement System are:
- RequestDB