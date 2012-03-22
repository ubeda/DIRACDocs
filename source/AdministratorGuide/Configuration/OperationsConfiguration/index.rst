.. _dirac-operations-cs:

=========================================
Configuration of Operational Parameters
=========================================

Operational parameters are defined under */Operations* section. The */Operations* section has a different path for each VO and Setup combination. For instance for *VO=dirac* and *Setup=Production* the Operations configuration path would be */Operations/dirac/Production*. For single-VO installations the VO part of the path will be skipped and just use */Operations/Production*. If DIRAC doesn't find the parameter under that path, it will look also for */Operations/<vo name>/Default*. This way parameters can be defined for all Setups of a VO (for single-VO installations this path will be */Operations/Default*)

The following list contains what can be configured under */Operations*:

.. toctree::
   :maxdepth: 1

   JobScheduling/index

