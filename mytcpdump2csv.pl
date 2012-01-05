#!/usr/bin/perl
# tcpdump -nnlr equinix-sanjose.dirA.20090416-130000.UTC.anon.pcap | ./my*pl "sport"
# tcpdump 3.9.4
# expects line like 08:00:00.000058 ip: 221.45.9.41.80 > 246.193.95.149.2150: . 2898260915:2898262375(1460) ack 1619891163 win 6432

use strict vars;
my $output=$ARGV[0];
my $DEBUG=1;
our ($dip,$sip,$sport,$dport);
my $linenum = 0;
while (<STDIN>) {
    $linenum = $linenum+1;
    chomp;
#    if (/(\d+:\d+:\d+\.\d+) \S+ (\d+\.\d+\.\d+\.\d+)\.(\d+) > (\d+\.\d+\.\d+\.\d+)\.(\d+):/){
    if (/(\S+) (\d+\.\d+.\d+\.\d+)(\.(\d+))? > (\d+\.\d+.\d+\.\d+)(\.(\d+))?:/) {
	#print $1, ",", $2, ",", $4 , ",",  $5, ",", $7;
	$sip = $2;
	$sport = $4;
	$dip = $5;
	$dport = $7;
    }
    else {
	print STDERR "ERROR $linenum: $_\n";
	next;
    }
    my @fields = split (" ",$_);
    my @tokens = split / /,$output;
    print ${shift(@tokens)};
    for my $token (@tokens) {
	print ','.$$token;
    }
    print "\n";
}
	
