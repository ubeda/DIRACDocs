Resources / StorageElementGroups - Subsections
==============================================

All the storages elements groups available for the users are described in this subsection.

+----------+-----------------+-------------+
| **Name** | **Description** | **Example** |
+----------+-----------------+-------------+
| SE-USER | Default SEs to be used when uploading output data from Payloads| CERN-USER, PIC-USER, IN2P3-USER |
+----------+-----------------+-------------+
| Tier1-Failover | Failover SEs to be used if the OutputSE is not available at the end of the Payload execution | CERN-FAILOVER, IN2P3-FAILOVER |
+----------+-----------------+-------------+
| SE_Cleaning_List | SEs to be cleaned up when using the ReplicaManager cleanLogicalDirectory methods | [You should include all your SEs in this list] |
+----------+-----------------+-------------+
