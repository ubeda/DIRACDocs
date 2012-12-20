=================
RSS Configuration
=================

The basic configuration for the RSS is minimal, and must be placed under the Operations section,
preferably on Defaults subsection. ::

  /Operations/Defaults/RSSConfiguration2
                          /Config
                              State      = Active
                              RecordLogs = Active
                              /StatusTypes
                                  default = all
                                  StorageElement = ReadAccess,WriteAccess,CheckAccess,RemoveAccess   

--------------
Config section
--------------

This section is all you need to get the RSS working. The parameters are the following:
             
:State: < Active || InActive ( default if not specified ) > is the flag used on the ResourceStatus helper to switch between CS and RSS - during the transition from CS to RSS. If Active, RSS is used.
:RecordLogs: < Active ( default if not specified ) || InActive > allows the ResourceStatusDB to log into the <element>Log tables.
:StatusTypes: if a ElementType has more than one StatusType ( aka StorageElement ), we have to specify them here, Otherwise, "all" is taken as StatusType.

.. note :: To not interfere with previous RSSConfiguration it has been named RSSConfiguration2 on purpose.

