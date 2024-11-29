import os

#############################################################################
## Concatenate single files from different configurations
#############################################################################

#tm2eblist = ['sgrc_1_S1.ms']
#tm1eblist = ['sgrc_1_S1.ms', 'sgrc_1_S2.ms']
#semipasslist = ['sgrc_1_S1.ms']

#contlist = ['../member.uid___A001_X1590_X2a76/maps/'+eb for eb in tm2eblist]+['../member.uid___A001_X1590_X2a74/maps/'+eb for eb in tm1eblist]+['../semipass/maps/'+eb for eb in semipasslist]

#myvis = 'sgrc1_TM12.ms'
#concat(vis=contlist, concatvis=myvis, timesort=True)
#listobs(vis=myvis, listfile=myvis+'.listobs')

## Recalculate the statistical weights, and note that corrected datacolumn does not exist
#statwt(datacolumn='data', vis=myvis)

##############################################################################
## Image line emission
##############################################################################

## cd /reduction/xingpan/ALMA/SgrC/2021.1.00286.S/science_goal.uid___A001_X1590_X2a72/group.uid___A001_X1590_X2a73/member.uid___A001_X1590_X2a74/maps

## Restore Unflagged data
myvis_list = ["sgrc_1_S1.ms", "sgrc_1_S2.ms", "sgrc_2_S1.ms", "sgrc_2_S2.ms"]

for myvis in myvis_list:
  flagmanager(vis=myvis, mode='restore', versionname='before_cont_flags')


myvis_list = ["sgrc_1_S1.ms", "sgrc_1_S2.ms", "sgrc_2_S1.ms", "sgrc_2_S2.ms"]
# Line-free channels, extreme line rich, very hard to identify line-free channels
fc = '0:1345~1425;1510~1600;1700~1780,1:710~770;1250~1320;1440~1510,2:80~130;220~240;1600~1650,3:1080~1110;1350~1470'

## The uvcontsub command has been updated, we should use new parameters now
for myvis in myvis_list:
    uvcontsub(vis=myvis,
        outputvis=myvis+".line",
        fitspec=fc, 
        fitorder=0)

## cd /reduction/xingpan/ALMA/SgrC/2021.1.00286.S/science_goal.uid___A001_X1590_X2a72/group.uid___A001_X1590_X2a73/member.uid___A001_X1590_X2a76/maps

## Restore Unflagged data
myvis_list = ["sgrc_1_S1.ms", "sgrc_2_S1.ms"]

for myvis in myvis_list:
  flagmanager(vis=myvis, mode='restore', versionname='before_cont_flags')


myvis_list = ["sgrc_1_S1.ms", "sgrc_2_S1.ms"]
# Line-free channels, extreme line rich, very hard to identify line-free channels
fc = '0:1345~1425;1510~1600;1700~1780,1:710~770;1250~1320;1440~1510,2:80~130;220~240;1600~1650,3:1080~1110;1350~1470'

## The uvcontsub command has been updated, we should use new parameters now
for myvis in myvis_list:
    uvcontsub(vis=myvis,
        outputvis=myvis+".line",
        fitspec=fc, 
        fitorder=0)
