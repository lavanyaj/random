#!/bin/csh
#
#***
#*** "#PBS" lines must come before any non-blank, non-comment lines ***
#***
#
# 1 node, 1 CPU per node (total 1 CPU), wall clock time of 30 hours
#
#PBS -l walltime=50:00:00,nodes=5:ppn=5
#
# merge STDERR into STDOUT file
#PBS -j oe
#
# send mail if the process aborts, when it begins, and
# when it ends (abe)
#PBS -m abe
#PBS -M ljose@Princeton.EDU
#

# 060000 pcap contains [130000, 130001) GMT
# its 1 second pickle in seconds(130001).pkl

if ($?PBS_JOBID) then
	echo "Starting" $PBS_JOBID "at" `date` "on" `hostname`
	echo ""
else
	echo "This script must be run as a PBS job"
	exit 1
endif

cd $PBS_O_WORKDIR

set urlday='https://data.caida.org/datasets/passive-2009/equinix-sanjose/20090416-130000.UTC'
set hhmmss='130300'
set trace='equinix-sanjose.dirA.20090416'
set dir='/n/fs/hhh/random'
#set python='/n/fs/ugrad/ug12/ljose/Python-3.1.2/python' 
set suff='UTC.anon'
set N=5


echo "$hhmmss"

set tracefilename=$trace-$hhmmss.$suff
set tracefiledir=$dir/$trace
set tracefile=$tracefilename
set pcapfile=$tracefile.pcap
set gzfile=$pcapfile.gz
set codedir='/n/fs/ugrad/ug12/ljose/git/random'

#wget --directory-prefix=$tracefiledir --http-user=jrex@cs.princeton.edu --http-password=lavanya --no-check-certificate $urlday/$gzfile

#gunzip $tracefiledir/$gzfile
#echo "unzipped"

#rm $tracefiledir/$hhmmss-$hhmmss-$N.err.old
#rm $tracefiledir/$hhmmss-$hhmmss-$N.old

#mv $tracefiledir/$hhmmss-$hhmmss-$N.err $tracefiledir/$hhmmss-$hhmmss-$N.err.old
#mv $tracefiledir/$hhmmss-$hhmmss-$N $tracefiledir/$hhmmss-$hhmmss-$N.old

#(tcpdump -nnlr $tracefiledir/$pcapfile | $codedir/mytcpdump2csv.pl "dport" | python $codedir/rawpairs.py $N > $tracefiledir/$hhmmss-$hhmmss-$N.raw) >& $tracefiledir/$hhmmss-$hhmmss-$N.err

#time split -l 4000000 $tracefiledir/$hhmmss-$hhmmss-$N.raw $tracefiledir/$hhmmss-$hhmmss-$N.raw_

time python simplesketcher.py $N $tracefiledir/$hhmmss-$hhmmss-$N.raw_al

#(tcpdump -nnlr $tracefiledir/$pcapfile | $tracefiledir/mytcpdump2csv.pl "dport" | $tracefiledir/distinctNvectors.py $N > $tracefiledir/$tracefile.$N) #>& $tracefiledir/$tracefile.err

#tcpdump -nnr $dir/pcap/$trace/$trace-$hhmmss.$suff.pcap >$dir/dump/$trace/$trace-$hhmmss.$suff.dump
echo "dumped"

    # Usage:tcpdump -vttttnnelr /tmp/log.tcpdump | ./tcpdump2csv.pl ["field list"]
#rm $dir/pcap/$trace/$trace-$hhmmss.$suff.pcap

#$python $dir/code/counts.py $dir/dump/$trace/$trace-$hhmmss.$suff.dump

#echo "pkled"

#rm ${homedir}/dump/${year}/equinix-sanjose.dirA.20090917-06$MMMM.UTC.anon.dump
echo ""
echo "Done at " `date`
