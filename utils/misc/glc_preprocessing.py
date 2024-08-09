# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:45:24 2024

@author: richiebao
"""
import rioxarray as rxr

from utils.args import args
from utils.misc.rasterShp4folium import raster4folium
from utils.misc.database import accdb2df

from matplotlib.colors import from_levels_and_colors
from matplotlib import colors
import matplotlib.patches as mpatches
import numpy as np
import matplotlib.pyplot as plt

from utils.args import args
from utils.misc.database import accdb2df


GLC_DATA_INDEX=args.raster.glc_data_index
YEAR_BAND_MAPPING=args.raster.glc_year_2000_2022_band_mapping

BNG_DB=args.db.bng_db


def glc_loading(city_name,year):
    fn=GLC_DATA_INDEX[city_name]
    band=YEAR_BAND_MAPPING[year]
    # band=1
    # glc=rxr.open_rasterio(fn,masked=True).squeeze()
    # print(glc.rio.crs)
    img,img_T,centre_lat, centre_lon,bounds_fin,meta=raster4folium(fn,band)
    # print(img,img_T,centre_lat, centre_lon,bounds_fin,meta)    
    # glc_categories=accdb2df(BNG_DB,table_name)
    return img,img_T,centre_lat, centre_lon,bounds_fin,meta
    
    
def glc_cmap(glc_categories_df):
    labels_cmap_dict={row['lcid']:(row['color_r']/255,row['color_g']/255,row['color_b']/255) for _,row in glc_categories_df.iterrows()}
    labels_cmap_dict_sorted=dict(sorted(labels_cmap_dict.items()))    
    # print(labels_cmap_dict_sorted)
    cmap, norm = from_levels_and_colors(list(labels_cmap_dict_sorted.keys())+[250], list(labels_cmap_dict_sorted.values()))
    
    # Generate some example data
    # data = np.random.choice(list(labels_cmap_dict_sorted.keys()),100).reshape((10,10))
    # print(data)
    # Create a plot using the colormap and normalization
    # plt.imshow(data, cmap=cmap, norm=norm)
    # plt.colorbar()  # Add a colorbar to the plot
    # plt.title('Discrete Levels with Custom RGB Colors')
    # plt.show()
    
    return cmap,norm    
  
    

if __name__=="__main__":
    # city_name="西安"
    # year=2022
    # table_name='glc_categories'
    # glc_loading(city_name,year,table_name)

    DB_GLC_INFO_SOURCE=args.db.bng_db #r"C:\Users\richi\omen_richiebao\omen_github\blue_greenES\database\bng_accdb.accdb"
    table_name='glc_categories'
    df=accdb2df(DB_GLC_INFO_SOURCE,table_name)
    cmap,norm=glc_cmap(df)