#!/bin/csh
#
#***
#*** "#PBS" lines must come before any non-blank, non-comment lines ***
#***
#
# 1 node, 1 CPU per node (total 1 CPU), wall clock time of 30 hours
#
#PBS -l walltime=10:00:00,nodes=1:ppn=1
#
# merge STDERR into STDOUT file
#PBS -j oe
#
# send mail if the process aborts, when it begins, and
# when it ends (abe)


#

# 060000 pcap contains [130100, 130001) GMT
# its 1 second pickle in seconds(130001).pkl

if ($?PBS_JOBID) then
	echo "Starting" $PBS_JOBID "at" `date` "on" `hostname`
	echo ""
else
	echo "This script must be run as a PBS job"
	exit 1
endif

cd $PBS_O_WORKDIR

set hhmmss='131500'
set codedir='/n/fs/ugrad/ug12/ljose/git/random'
set rawfiledir='/n/fs/hhh/random/raw'
set T=10

time python secondsketcher.py $T $rawfiledir/dp-$hhmmss-$hhmmss-T$T.raw_ai
echo ""
echo "Done at " `date`
