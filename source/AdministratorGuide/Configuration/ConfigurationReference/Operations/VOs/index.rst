Operations / VOs - Subsections
==============================

<VO_NAME> subsections allows to define pilot jobs versions for each setup defined for each VO supported by the server.

+-----------------------------------------------+----------------------------------------------+---------------------------+
| **Name**                                      | **Description**                              | **Example**               |
+-----------------------------------------------+----------------------------------------------+---------------------------+
| *<VO_NAME>*                                   | Subsection: Virtual organization name        | vo.formation.idgrilles.fr |
+-----------------------------------------------+----------------------------------------------+---------------------------+
| *<VO_NAME>/<SETUP_NAME>/*                     | Subsection: VO Setup name                    | Dirac-Production          |
+-----------------------------------------------+----------------------------------------------+---------------------------+
| *<VO_NAME>/<SETUP_NAME>/Version/*             | Subsection: Version  (Name fixed)            | Version                   |
+-----------------------------------------------+----------------------------------------------+---------------------------+
| *<VO_NAME>/<SETUP_NAME>/Version/PilotVersion* | DIRAC version to be installed for the pilots | PilotVersion = v6r0-pre7  |
|                                               | in the WNs                                   |                           |
+-----------------------------------------------+----------------------------------------------+---------------------------+
