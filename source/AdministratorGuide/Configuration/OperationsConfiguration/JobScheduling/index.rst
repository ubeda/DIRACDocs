Job Scheduling
=========================================

The */Operations/<vo>/<setup>/JobScheduling* section contains all parameters that define DIRAC's behaviour when deciding what job has to be
executed. Here's a list of parameters that can be defined:

=========================  ========================================================  ===============================================================================================
Parameter                  Description                                               Default value
=========================  ========================================================  ===============================================================================================
taskQueueCPUTimeIntervals  Possible cpu time values that the task queues can have.   [360, 1800, 3600, 21600, 43200, 86400, 172800, 259200, 345600, 518400, 691200, 864000, 1080000]
-------------------------  --------------------------------------------------------  -----------------------------------------------------------------------------------------------
EnableSharesCorrection     Enable automatic correction of the priorities assigned    False
                           to each task queue based on previous history
-------------------------  --------------------------------------------------------  -----------------------------------------------------------------------------------------------
CheckJobLimits             Limit the amount of jobs running at sites based on        False
                           their attributes
-------------------------  --------------------------------------------------------  -----------------------------------------------------------------------------------------------
CheckMatchingDelay         Delay running a job at a site if another job has started  False
                           recently and the conditions are met
=========================  ========================================================  ===============================================================================================

Before enabling the correction of priorities, take a look at :ref:`jobpriorities`. Priorities and how to correct them is explained there.
The configuration of the corrections would be defined under *JobScheduling/ShareCorrections*.

Limiting the number of jobs running
====================================

Once *JobScheduling/EnableJobLimits* is enabled. DIRAC will check how many and what type of jobs are running at the configured sites. If
there are more than a configured threshold, no more jobs of that type will run at that site.
