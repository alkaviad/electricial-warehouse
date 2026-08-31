import extruder4_main_cabinet_inventory_patch
import extruder4_main_cabinet_navigation_fix

def apply(legacy):
    extruder4_main_cabinet_inventory_patch.apply(legacy)
    extruder4_main_cabinet_navigation_fix.apply(legacy)
