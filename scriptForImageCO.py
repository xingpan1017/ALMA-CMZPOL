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

###############################################################################
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
  
#############################################################################
## cd /reduction/xingpan/ALMA/SgrC/2021.1.00286.S/science_goal.uid___A001_X1590_X2a72/group.uid___A001_X1590_X2a73/semipass/maps

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
  
##############################################################################
## Combine all the datasets to image CO
##############################################################################

tm2eblist = ['sgrc_1_S1.ms.line', 'sgrc_2_S1.ms.line']
tm1eblist = ['sgrc_1_S1.ms.line', 'sgrc_1_S2.ms.line', 'sgrc_2_S1.ms.line', 'sgrc_2_S2.ms.line']
semipasslist = ['sgrc_1_S1.ms.line', 'sgrc_2_S1.ms.line']

linelist = ['../member.uid___A001_X1590_X2a76/maps/'+eb for eb in tm2eblist]+['../member.uid___A001_X1590_X2a74/maps/'+eb for eb in tm1eblist]+['../semipass/maps/'+eb for eb in semipasslist]

# Image Parameters
cell = '0.04arcsec'
imsize = 960
weighting = 'briggs'
robust = 0.5
threshold = '0.1mJy'
imname = './line/sgrc_CO_3_2'
niter = 100000
pc = 'ICRS 17:44:40.391513 -29.28.14.567605'
restfreq = '345.7959899GHz'
start = '-150km/s'  ## Vsys ~-55 km/s
nchan = 200

tclean(vis = linelist,
  imagename=imname,
  specmode='cube',
  deconvolver = 'multiscale',
  spw = '2', ## Only select spw2 to image
  niter = niter,
  start = start,
  nchan = nchan,
  scales = [0,5,15,50],
  imsize=imsize,
  cell=cell,
  restfreq = restfreq,
  phasecenter = pc,
  threshold=threshold,  
  #nterms=2, 
  gridder='mosaic', 
  weighting=weighting,
  outframe = 'LSRK', 
  interactive = False,
  pblimit = 0.1,
  robust = robust,
  usemask = 'auto-multithresh',
  sidelobethreshold = 3.0,
  noisethreshold = 5.0,
  minbeamfrac = 0.3,
  lownoisethreshold = 1.5,
  negativethreshold = 0.0,
  pbmask = 0.3)

exportfits(imagename=imname+".image", fitsimage=imname+".image.fits", velocity=True, overwrite=True)
