Systems / WorkloadManagement / <SETUP> / Agents / StalledJobAgent - Sub-subsection
==================================================================================

The StalledJobAgent hunts for stalled jobs in the Job database. Jobs in "running"state not receiving a 
heart beat signal for more than stalledTime seconds will be assigned the "Stalled" state.

+--------------------+------------------------------------------+------------------------------+
| **Name**           | **Description**                          | **Example**                  |
+--------------------+------------------------------------------+------------------------------+
| *FailedTimeHours*  | How many time in hours pass before a job | FailedTimeHours = 6          |
|                    | is declared as stalled                   |                              |
+--------------------+------------------------------------------+------------------------------+
| *StalledTimeHours* | How many time in hours pass before a job | Time in StalledTimeHours = 2 |
|                    | is declared as stalled                   |                              |
+--------------------+------------------------------------------+------------------------------+
