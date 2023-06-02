
import argparse, os
os.environ['USE_PYGEOS'] = '0'
import geopandas

'''
useage:

python supertile_labelize.py --shapefile="path to my shapefile/shapefile.shp"

'''


parser = argparse.ArgumentParser(description='Adds column (tnum) to shapefile and populates it with unique index.')
parser.add_argument('--shapefile', type=str, help='Shapefile')
args = parser.parse_args()

#open shapefile with geopandas
df = geopandas.GeoDataFrame.from_file(args.shapefile)

#make list of numbers, starting with zero ending in length-1
# len(df.index) gives the # of rows in a geopandas dataframe
numbers_for_index = range(len(df.index))

#make new column and populate it with the list of numbers
#if the column already exists, it will be over-written.
df["tnum"] = numbers_for_index

#save shapefile
#if you don't want to save as the same name (worried about messing your data) then 
#you can make a new filename
# new_filename = args.shapefile.replace('.shp', '_numbered.shp')
# df.to_file(new_filename)
#
df.to_file(args.shapefile)  
