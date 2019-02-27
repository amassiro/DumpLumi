import sys
import csv

from ROOT import TTree, TFile
from array import array


print " ", sys.argv[1], " --> ", sys.argv[2]

new_file = TFile(sys.argv[2], "RECREATE")

new_tree = TTree ("tree", "tree")

run      = array( 'i', [ 0 ] )
fill     = array( 'i', [ 0 ] )
lumi_del = array( 'f', [ 0 ] )
lumi_rec = array( 'f', [ 0 ] )

new_tree.Branch( 'run',      run,      'run/I'      )
new_tree.Branch( 'fill',     fill,     'fill/I'     )
new_tree.Branch( 'lumi_del', lumi_del, 'lumi_del/F' )
new_tree.Branch( 'lumi_rec', lumi_rec, 'lumi_rec/F' )


#         dump.lumi.txt
with open(sys.argv[1]) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for row in csv_reader:
    #print row
    if not row[0].startswith('#') :
      run_fill = row[0].split(':')
      run[0]  = int(run_fill[0])
      fill[0] = int(run_fill[1])
      lumi_del[0] = float(row[4])
      lumi_rec[0] = float(row[5])
      #print " run:lumi_rec = ", run[0], " : ", lumi_rec[0]
      new_tree.Fill()

new_tree.Write()
new_file.Close()
    


    