#!/bin/bash

# ubeda@cern.ch
#-------------------------------------------------------------------------------

# Needs ( arguments )
# o $DIRACVERSION
#-------------------------------------------------------------------------------
if [ -z $1 ]
then
  echo no given DIRAC version, setting integration
  DIRACVERSION=integration
else
  DIRACVERSION=$1
fi

#DIRACVERSION is used by conf.py to declare the sphynx variable |release| 
export DIRACVERSION=$DIRACVERSION

# Create a temporary directory where to place all code
tmpdir=`mktemp -d`
echo Temporary directory: $tmpdir

#-------------------------------------------------------------------------------
# DIRAC

DIRAC_GITHUB=https://github.com/DIRACGrid/DIRAC/archive/
# Let's download DIRAC
echo Downloading DIRAC from $DIRAC_GITHUB$DIRACVERSION.zip 
wget $DIRAC_GITHUB$DIRACVERSION.zip --no-check-certificate --directory-prefix $tmpdir -q

unzip -q $tmpdir/$DIRACVERSION.zip -d $tmpdir
mv $tmpdir/DIRAC-* $tmpdir/DIRAC
rm $tmpdir/$DIRACVERSION.zip

echo DIRAC downloaded successfully to $tmpdir/DIRAC 

# Export tmpdir on PYTHONPATH so that we can import DIRAC
export PYTHONPATH=$PYTHONPATH:$tmpdir

#-------------------------------------------------------------------------------
# DIRACDocs

diracDocsVersion=buildClientsDOC

DIRACDocs_GITHUB=https://github.com/ubeda/DIRACDocs/archive/$diracDocsVersion.zip
# Let's download DIRACDocs
echo Downloading DIRACDocs from $DIRACDocs_GITHUB 
wget $DIRACDocs_GITHUB --no-check-certificate --directory-prefix $tmpdir -q

unzip -q $tmpdir/$diracDocsVersion.zip -d $tmpdir
mv $tmpdir/DIRACDocs-$diracDocsVersion $tmpdir/DIRACDocs
rm $tmpdir/$diracDocsVersion.zip

echo DIRACDocs downloaded successfully to $tmpdir/DIRACDocs

#-------------------------------------------------------------------------------
# Generate scripts documentation

scriptsDIR=$tmpdir/scripts
mkdir $scriptsDIR

# We have to mock quite few things now...

python $tmpdir/DIRACDocs/Tools/buildScriptsDOC.py scriptsDIR

#DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#make -C $DIR/.. html

#-------------------------------------------------------------------------------
#EOF