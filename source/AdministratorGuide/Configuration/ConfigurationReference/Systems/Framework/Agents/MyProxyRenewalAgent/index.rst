Systems / Framework / <SETUP> / Agents / MyProxyRenewalAgent - Sub-subsection
=============================================================================

Proxy Renewal agent is the key element of the Proxy Repository which maintains the user proxies alive.


The attributes of this agent are showed in the table below:

+------------------+------------------------------------------+---------------------+
| **Name**         | **Description**                          | **Example**         |
+------------------+------------------------------------------+---------------------+
| *MinValidity*    | Proxy Minimal validity time expressed in | MinValidity = 10000 |
|                  | seconds                                  |                     |
+------------------+------------------------------------------+---------------------+
| *PollingTime*    | Polling time in seconds                  | PollingTime = 1800  |
+------------------+------------------------------------------+---------------------+
| *ValidityPeriod* | The period for which the proxy will be   | ValidityPeriod = 15 |
|                  | extended. The value is in hours          |                     |
+------------------+------------------------------------------+---------------------+
