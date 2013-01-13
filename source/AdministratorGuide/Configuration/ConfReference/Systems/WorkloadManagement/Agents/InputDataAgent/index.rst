Systems / WorkloadManagement / <INSTANCE> / Agents / InputDataAgent - Sub-subsection
=================================================================================

The Input Data Agent queries the file catalog for specified job input data and adds the relevant information to the 
job optimizer parameters to be used during the scheduling decision.

+---------------------+---------------------------------------+--------------------------------------------+
| **Name**            | **Description**                       | **Example**                                |
+---------------------+---------------------------------------+--------------------------------------------+
| *CheckFileMetadata* | Boolean than define if the file meta- | CheckFileMetadata = True                   |
|                     | must be checked                       |                                            |
+---------------------+---------------------------------------+--------------------------------------------+
| *FailedJobStatus*   | Define failed job status              | FailedJobStatus = Input Data Not Available |
+---------------------+---------------------------------------+--------------------------------------------+
| *PollingTime*       | Polling Time                          | PollingTime = 120                          |
+---------------------+---------------------------------------+--------------------------------------------+
