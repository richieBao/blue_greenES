# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:11:20 2024

@author: richie bao
"""
import os

from utils.misc.gadgets import AttrDict


__C=AttrDict() 
args=__C

__C.db=AttrDict() 
# __C.db.bng_db=f"database/bng_accdb.accdb" # r"C:\Users\richi\omen_richiebao\omen_github\blue_greenES\database\bng_accdb.accdb"
# __C.db.bng_db=r"C:\Users\richi\omen_richiebao\omen_github\blue_greenES\database\bng_accdb.accdb"
__C.db.bng_db= "database/bng_accdb.accdb" #"database/bng_accdb.accdb" 

__C.raster=AttrDict() 
__C.raster.glc_data_index={
    # "西安":f'data/GLC/GLC_FCS30D_20002022_E105N35_Annual.tif',
    "西安":f'C:/Users/richi/omen_richiebao/omen_github/blue_greenES/data/GLC/glc_xian.tif', # GLC_FCS30D_20002022_E105N35_Annual.tif
    # "西安":f'C:/Users/richi/omen_richiebao/omen_appDevelop/USDA_desktopAPP/USDA/data/raster/LC_2017_4_clipped.tif',
    }
__C.raster.glc_year_2000_2022_band_mapping={k:v for k,v in zip(range(2000,2024),range(1,24))}

__C.workspace=AttrDict()
__C.workspace.dir=r'C:/Users/richi/omen_richiebao/omen_github/blue_greenES_workspace'
__C.workspace.temp=os.path.join(args.workspace.dir,"temp")
__C.workspace.draw_boundary_fn=os.path.join(args.workspace.temp,'draw_boundary.geojson')

__C.map=AttrDict() 
__C.map.url_osm="https://tile.openstreetmap.org/{z}/{x}/{y}.png"
__C.map.url_gaode='http://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}'
__C.map.coordi_XAUAT=(34.237075,108.967996)
# __C.map.glc_tile_url="http://localhost:5000/singleband/20002022/E105N35/{z}/{x}/{y}.png?colormap=greys&stretch_range=[10,124.86]"
# __C.map.glc_tile_url="http://localhost:5000/singleband/categorical/20002022/E105N35/{z}/{x}/{y}.png?colormap=greys&stretch_range=[10,72]"
# __C.map.glc_tile_url="http://localhost:5000/singleband/categorical/20002022/E105N35/{z}/{x}/{y}.png?colormap=explicit&explicit_color_map="
# __C.map.glc_tile_url='''http://localhost:5000/singleband/categorical/20002022/E105N35/{z}/{x}/{y}.png?colormap=explicit&explicit_color_map={"51":"99d594","10":"2b83ba","11":"ffffff","200":"404040"}'''
__C.map.glc_tile_url='''http://localhost:5000/singleband/categorical/20002022/E105N35/{z}/{x}/{y}.png?'''


__C.sqlite=AttrDict()
__C.sqlite.sql_glc_terracotta=r"C:\Users\richi\omen_richiebao\omen_github\blue_greenES\database\sql_glc_terracotta.sqlite"

__C.data=AttrDict()
__C.data.glc_path=r'C:\Users\richi\omen_richiebao\omen_github\blue_greenES\data\GLC\optimized' #'data/GLC/original'


dirs=[args.workspace.temp]
for dir in dirs:
    os.makedirs(dir, exist_ok=True)

    
if __name__=="__main__":
    print(args.workspace.draw_boundary_fn)