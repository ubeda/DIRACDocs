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

if [ -z "$LOCALDEBUG" ]
then
  DIRAC_GITHUB=https://github.com/DIRACGrid/DIRAC/archive/
  # Let's download DIRAC
  echo Downloading DIRAC from $DIRAC_GITHUB$DIRACVERSION.zip 
  wget $DIRAC_GITHUB$DIRACVERSION.zip --no-check-certificate --directory-prefix $tmpdir -q

  #unzip -q $tmpdir/$DIRACVERSION.zip -d $tmpdir
  unzip -q $tmpdir/DIRAC-*.zip -d $tmpdir
  mv $tmpdir/DIRAC-* $tmpdir/DIRAC
  #rm $tmpdir/$DIRACVERSION.zip
  rm $tmpdir/DIRAC-*.zip
  echo DIRAC downloaded successfully to $tmpdir/DIRAC
else  
  cp -r ~/git/DIRAC $tmpdir/DIRAC
  echo DIRAC copied successfully to $tmpdir/DIRAC
fi

# Export tmpdir on PYTHONPATH so that we can import DIRAC
export PYTHONPATH=$PYTHONPATH:$tmpdir

#-------------------------------------------------------------------------------
# DIRACDocs

if [ -z "$LOCALDEBUG" ]
then

  repo=DIRACGrid
  diracDocsVersion=master

  DIRACDocs_GITHUB=https://github.com/$repo/DIRACDocs/archive/$diracDocsVersion.zip
  # Let's download DIRACDocs
  echo Downloading DIRACDocs from $DIRACDocs_GITHUB 
  wget $DIRACDocs_GITHUB --no-check-certificate --directory-prefix $tmpdir -q

  unzip -q $tmpdir/$diracDocsVersion.zip -d $tmpdir
  mv $tmpdir/DIRACDocs-$diracDocsVersion $tmpdir/DIRACDocs
  rm $tmpdir/$diracDocsVersion.zip
  echo DIRACDocs downloaded successfully to $tmpdir/DIRACDocs
else
  cp -r ~/git/DIRACDocs $tmpdir/DIRACDocs
  echo DIRACDocs copied successfully to $tmpdir/DIRACDocs
fi

# Export tmpdir on PYTHONPATH so that we can import fakeEnvironment
export PYTHONPATH=$PYTHONPATH:$tmpdir/DIRACDocs/Tools

#-------------------------------------------------------------------------------
# Generate scripts documentation

scriptsDIR=$tmpdir/build/scripts
mkdir -p $scriptsDIR
codeDIR=$tmpdir/build/code
mkdir -p $codeDIR

python $tmpdir/DIRACDocs/Tools/buildScriptsDOC.py $scriptsDIR
python $tmpdir/DIRACDocs/Tools/buildCodeDOC.py $codeDIR

#-------------------------------------------------------------------------------
# Make html web pages from rst's

make -C $tmpdir/DIRACDocs html

echo $tmpdir

#-------------------------------------------------------------------------------
#EOF