# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 18:09:03 2024

@author: richiebao
"""
import folium
from folium.plugins import Draw,MeasureControl,MiniMap,MousePosition
import os
import io

from utils.args import args

# dash.register_page(__name__,name="TEMP", path='/temp')

# JavaScript to change the "Export" button text to "Submit"
custom_button_script = """
<script>
// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', function() {
    // Find the "Export" button by its text content
    var exportButton = Array.from(document.getElementsByClassName('leaflet-control')[0].getElementsByTagName('a'))
        .find(el => el.textContent === 'Export');
    
    if (exportButton) {
        // Change the button text to "Submit"
        exportButton.textContent = 'Submit';
    }
});
</script>
"""


def plot_map():
    #ommited code
    coordinate = (34.237075,108.967996)
    m = folium.Map(location=coordinate, zoom_start=17, world_copy_jump=True, prefer_canvas=True)
    #ommited code
    
    m.add_child(MeasureControl())
    
    url1 ='http://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}'
    # url2 = "http://webst04.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}"
    
        
    folium.TileLayer(tiles = url1, name = "高德地图", attr='amap', control = True,show=True).add_to(m)    
    MousePosition().add_to(m)
    MiniMap(toggle_display=True).add_to(m)
    folium.plugins.Geocoder(position="bottomleft").add_to(m)    
    
    Draw(
        export=True,
        filename=args.workspace.draw_boundary_fn,
        position="topleft",
        draw_options={
            "polyline": True,
            "polygon":True,
            "rectangle": True,
            "circle": True,
            "circlemarker": True,
        },
        edit_options={
            "poly": {"allowIntersection": False},
            # 'edit': True,
            # 'remove': True,
            },
    ).add_to(m)   
    
    # data=io.BytesIO()
    # m.save(data,close_file=False)
    # Inject the JavaScript into the map
    # m.get_root().html.add_child(folium.Element(custom_button_script))


    # src_doc = m.get_root().render()  #obtain the HTML content 
    # return src_doc
    
    
    return m




if __name__=="__main__":
    pass