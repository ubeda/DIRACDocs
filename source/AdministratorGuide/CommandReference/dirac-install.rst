====================
dirac-install
====================

2011-12-04 16:55:57 UTC dirac-install [NOTICE]  Processing installation requirements

Usage::

 r:  release=             : Release version to install

 l:  project=             : Project to install

 e:  extraModules=        : Extra modules to install (comma separated)

 t:  installType=         : Installation type (client/server)

 i:  pythonVersion=       : Python version to compile (25/24)

 p:  platform=            : Platform to install

 P:  installationPath=    : Path where to install (default current working dir)

 b   build                : Force local compilation

 g:  grid=                : lcg tools package version

 B   noAutoBuild          : Do not build if not available

 v   useVersionsDir       : Use versions directory

 u:  baseURL=             : Use URL as the source for installation tarballs

 V:  installation=        : Installation from which to extract parameter values

 X   externalsOnly        : Only install external binaries

Known options and default values from /defaults section of releases file

 Release = 

 Project = DIRAC

 ModulesToInstall = []

 ExternalsType = client

 PythonVersion = 26

 LcgVer = 

 UseVersionsDir = False

 BuildExternals = False

 NoAutoBuild = False

 Debug = False

