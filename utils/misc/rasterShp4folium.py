# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:25:30 2024

@author: richie bao
"""
import rasterio as rio
import folium
from pyproj import Transformer 
import geopandas as gpd
import branca
import numpy as np


dst_crs="EPSG:4326"

def raster4folium(in_path,band=1):
    with rio.open(in_path) as src:
        img=src.read(band)
        img=np.expand_dims(img,axis=0)
        src_crs=src.crs#src.crs['init'].upper()
        
        # print(src_crs)
        min_lon,min_lat,max_lon,max_lat=src.bounds
        meta=src.meta
 
    ## Conversion from UTM to WGS84 CRS
    bounds_orig=[[min_lat,min_lon],[max_lat,max_lon]]
    bounds_fin = []
    for item in bounds_orig:
        lat = item[0]
        lon = item[1]
        
        proj = Transformer.from_crs(src_crs, dst_crs, always_xy=True) # int(src_crs.split(":")[1])  ;int(src_crs.split(":")[1])
        lon_n, lat_n = proj.transform(lon, lat)
        bounds_fin.append([lat_n, lon_n])
        
    # Finding the centre latitude & longitude
    centre_lon = bounds_fin[0][1] + (bounds_fin[1][1] - bounds_fin[0][1])/2
    centre_lat = bounds_fin[0][0] + (bounds_fin[1][0] - bounds_fin[0][0])/2   
    # print("+++",img.shape)
    img_T=img.transpose(1, 2, 0)
    
    # print(meta)
    
    return img,img_T,centre_lat, centre_lon,bounds_fin,meta

def getEPSGFromRaster(in_path):
    with rio.open(in_path) as src:
        src_crs=src.crs #['init'].upper()

    # print('---',src_crs)
    return src_crs

def gpd4folium_(gdf,m,popupField=None):
    gdf4326=gdf.to_crs(epsg=4326)
    for _, row in gdf4326.iterrows():
        sim_geo = c
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j, ) # style_function=lambda x: {"fillColor": "orange"}
        if popupField:
            folium.Popup(row[popupField]).add_to(geo_j)
        geo_j.add_to(m)
        
        
    centroid=[(gdf4326.total_bounds[1]+gdf4326.total_bounds[3])/2,(gdf4326.total_bounds[0]+gdf4326.total_bounds[2])/2]
    return centroid


def gpd4folium(gdf,m,fields4popup=None,fields4tooltip=None,field4colormap=None,**kwargs):
    gdf4326=gdf.to_crs(epsg=4326)
    # gdf4326_original=gdf.to_crs(epsg=4326)
    # gdf4326=gdf4326_original.explode(index_parts=False)
    gdf4326['geometry']=gpd.GeoSeries(gdf4326["geometry"]).simplify(tolerance=0.001)
    # gdf4326.reset_index(inplace=True)
    # print("+++",gdf4326)
        
    args=dict(
        caption="colorbar",
        colors=["red", "orange", "lightblue", "green", "darkgreen"],
        popup_style="background-color: yellow;",
        popup_aliases=fields4popup,
        tooltip_aliases=fields4tooltip,
        tooltip_style="""
            background-color: #F0EFEF;
            border: 2px solid black;
            border-radius: 3px;
            box-shadow: 3px;
        """,
        tooltip_max_width=800,
        )
    args.update(kwargs)
    
    if field4colormap:
        gdf4326=gdf4326.astype({field4colormap:"float"})
        
        colormap = branca.colormap.LinearColormap(   
            vmin=gdf4326[field4colormap].astype("float").quantile(0.0),
            vmax=gdf4326[field4colormap].astype("float").quantile(1),
            colors=args["colors"],
            caption=args['caption'],
        )  
        colormap.add_to(m)    
        
    if fields4popup:
        if fields4popup[0]!='':
            popup = folium.GeoJsonPopup(
                fields=fields4popup,
                aliases=args["popup_aliases"],
                localize=True,
                labels=True,
                style=args["popup_style"],
            )    
        else:popup=None
    else:popup=None
        
        
    if fields4tooltip:
        if fields4tooltip[0]!='':
            tooltip = folium.GeoJsonTooltip(
                fields=fields4tooltip,
                aliases=args["tooltip_aliases"],
                localize=True,
                sticky=False,
                labels=True,
                style=args["tooltip_style"],
                max_width=args["tooltip_max_width"],
            )    
        else:tooltip=None
    else:tooltip=None
        
    # print('----------+++',tooltip,"+_",popup)
        
    g = folium.GeoJson(
        gdf4326, # .to_json()
        style_function=lambda x: {
            "fillColor": colormap(x["properties"][field4colormap]) # ["properties"]
            if field4colormap and x["properties"][field4colormap] is not None #["properties"]
            else "transparent",
            "color": "black",
            "fillOpacity": 0.4,
        },
        tooltip=tooltip,
        popup=popup,
    ).add_to(m)
        

    centroid=[(gdf4326.total_bounds[1]+gdf4326.total_bounds[3])/2,(gdf4326.total_bounds[0]+gdf4326.total_bounds[2])/2]
    return centroid


  

if __name__=="__main__":
    in_path=r"C:\Users\richi\omen_richiebao\omen_appDevelop\USDA_desktopAPP\USDA\data\raster\worlpop_populationCount_chn_ppp_2020_UNadj_constrained_clipped.tif"
    img,img_T,centre_lat, centre_lon,bounds_fin,meta=raster4folium(in_path)
    # print(img,img_T,centre_lat, centre_lon)
    # meta_str=''.join([f"\t{k}:{v}\n" for k,v in meta.items()])
    # print(meta_str)
    
    # getEPSGFromRaster(in_path)
