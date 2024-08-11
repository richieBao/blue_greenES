# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:39:16 2024

@author: richie bao
"""
import os
from typing import Dict, List
import terracotta

from utils.args import args
from utils.misc.gadgets import get_all_file_paths
from utils.misc.database import accdb2df

DB_NAME = args.sqlite.sql_glc_terracotta
KEYS = ["type", "date","latlon"]

glc_path=args.data.glc_path
RASTER_FILES = get_all_file_paths(glc_path,pattern="*.tif")

DB_GLC_INFO_SOURCE=args.db.bng_db 
table_name='glc_categories'
glc_categories_df=accdb2df(DB_GLC_INFO_SOURCE,table_name)

category_map ={row['classification_system']:row['lcid'] for _,row in glc_categories_df.iterrows()}

def load(db_name:str,keys:List[str],raster_files:List[str],category_map:Dict):
    driver = terracotta.get_driver(db_name)
    
    # create the database file if it doesn't exist already
    if not os.path.isfile(db_name):
        driver.create(keys)
    
    # check that the database has the same keys that we want to load
    assert list(driver.key_names) == keys, (driver.key_names, keys)
    # connect to the database
    with driver.connect():
        for raster_path in raster_files:            
            metadata = driver.compute_metadata(
                raster_path,
                extra_metadata={'categories': category_map}
            )
            
            fn = os.path.basename(raster_path)
            if fn=="GLC_FCS30D_20002022_E105N35_Annual.tif":
                fn_info=fn.split('/')[-1].split('.')[0].split('_')
                key_values=['categorical',fn_info[2],fn_info[3]]
                # print(key_values)
                driver.insert(key_values, raster_path, metadata=metadata)   
            
    
if __name__ == "__main__":    
    load(DB_NAME, KEYS, RASTER_FILES,category_map)    
    
    
    '''
    terracotta optimize-rasters C:/Users/richi/omen_richiebao/omen_github/blue_greenES/data/GLC/original/*.tif -o C:/Users/richi/omen_richiebao/omen_github/blue_greenES/data/GLC/optimized/ --reproject True --compression auto --overwrite True --nproc -1
    https://terracotta-python.readthedocs.io/en/latest/cli-commands/optimize-rasters.html
    瓦片地图服务器
    '''
    
    