# DumpLumi
Dump luminosity vs run/LS in a root file

Where:

    /afs/cern.ch/user/a/amassiro/work/CMG/DisappearingTracks/CMSSW_9_4_6_patch1/src/DumpLumi
 
 
BrilCalc
====

Documentation: https://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html

Pdmv: https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV2017Analysis



    export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.1.7/bin:$PATH
    
    brilcalc lumi -u /pb -i missingLumiSummary.json
    
    brilcalc lumi --help
    
    brilcalc lumi --begin 297046 --end 306462 -u /fb \
        -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt \
        --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json  \
        -o  dump.lumi.txt

        
Transform csv into root file
====

    python csv2root.py  dump.lumi.txt  dump.lumi.root

    
Simple draw
====

    r99t dump.lumi.root
    tree->Draw("lumi_rec:run")


