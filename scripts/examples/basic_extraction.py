import microtaspy.segmentation as mseg
import skimage.io as skio

path = '/mnt/seaside/rsl/DataSetForTim/2D_Data/Kiwimagi12082017/CytationData/170811_112033_Plate 3/'

g = skio.imread(path + 'B5_02_2_6_GFP_001.tif')
r = skio.imread(path + 'B5_02_3_6_Texas Red_001.tif')
b = skio.imread(path + 'B5_02_4_6_TagBFP_001.tif')

# segment in green channel, compute intensities in green, red, and blue with green mask
df,_,_ = mseg.get_events(g,(g,r,b),['g','r','b'])
