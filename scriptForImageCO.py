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

## Substract continuum emission
rawvis_list = ["sgrc1_TM12.ms", "sgrc2_TM12.ms"]

# Line-free channels

