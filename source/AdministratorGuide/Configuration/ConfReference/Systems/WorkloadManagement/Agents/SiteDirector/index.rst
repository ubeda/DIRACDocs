Systems / WorkloadManagement / <INSTANCE> / Agents / SiteDirector - Sub-subsection
==================================================================================

Site director is in charge of submit pilot jobs to special Computing Elements.
 
 Special attributes for this agent are:
 
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+
| **Name**              | **Description**                        | **Example**                                                       | |
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+
| *CETypes*             | List of CEs types allowed to submit    | CETypes = CREAM                                                   | |
|                       | pilot jobs                             |                                                                   | |
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+
| *CEs*                 | List of CEs to submit pilot jobs       | CEs = ce01.in2p3.fr                                               | |
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+
| *GenericPilotDN*      | Generic pilot DN used to submit the    | GenericPilotDN =  /O=GRID-FR/C=FR/O=CNRS/OU=CPPM/CN=Vanessa Hamar | |
|                       | pilot jobs                             |                                                                   | |
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+
| *GenericPilotGroup*   | DIRAC group used to submit the pilot   | GenericPilotGroup = dirac_pilot                                   | |
|                       | jobs                                   |                                                                   | |
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+
| *GetPilotOutput*      | Boolean value used to indicate the     | GetPilotOutput = True                                             | |
|                       | pilot output will be or not retrieved  |                                                                   | |
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+
| *GridEnv*             | Path where is located the file to      | GridEnv = /usr/profile.d/grid-env                                 | |
|                       | load Grid Environment Variables        |                                                                   | |
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+
| *MaxQueueLength*      | Maximum number of pilots jobs in queue | MaxQueueLength = 86400*3                                          | |
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+
| *SendPilotAccounting* | Boolean value than indicates if the    | SendPilotAccounting = yes                                         | |
|                       | pilot job will send information for    |                                                                   | |
|                       | accounting                             |                                                                   | |
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+
| *Site*                | Sites name list where the pilots will  | Site =                                                            | |
|                       | be submitted                           |                                                                   | |
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+
| *UpdatePilotStatus*   | Attribute used to define if the status | UpdatePilotStatus = True                                          | |
|                       | of the pilot will be updated           |                                                                   | |
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+
| *WorkDirectory*       | Working Directory in the CE            | WorkDirectory = /tmp                                              | |
+-----------------------+----------------------------------------+-------------------------------------------------------------------+-+

