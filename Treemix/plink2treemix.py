#!/usr/bin/python

import sys, os, gzip

if len(sys.argv) < 3:
	print("plink2treemix.py [gzipped input file] [gzipped output file]")
	print("ERROR: improper command line")
	exit(1)
infile = gzip.open(sys.argv[1])
outfile = gzip.open(sys.argv[2], "wt")


pop2rs = dict()
rss = list()
rss2 = set()

line = infile.readline()
line = infile.readline()
while line:
    line = line.strip().split()
    rs = line[1].decode("utf-8")
    pop = line[2].decode("utf-8")
    mc = line[6].decode("utf-8")
    total = line[7].decode("utf-8")
    if rs not in rss2: 
    	rss.append(rs)
    rss2.add(rs)
    if pop not in pop2rs:
        pop2rs[pop] =  dict()
    if rs not in pop2rs[pop]:
        pop2rs[pop][rs] = " ".join([mc, total])
    line = infile.readline()

pops = pop2rs.keys()
print(' '.join([x for x in pops]), end='\n', file=outfile)

for rs in rss:
    pop_tmp = []
    for pop in pops:
        tmp = pop2rs[pop][rs].split()
        c1 = int(tmp[0])
        c2 = int(tmp[1])
        c3 = c2-c1
        pop_tmp.append(",".join([str(c1), str(c3)]))
    print(' '.join([x for x in pop_tmp]),end='\n', file=outfile)


