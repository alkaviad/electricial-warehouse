import extruder4_main_cabinet_inventory_patch
import extruder4_main_cabinet_full_data_patch
import extruder4_main_cabinet_cleanup_patch
import extruder4_main_cabinet_click_fix

def apply(legacy):
    extruder4_main_cabinet_inventory_patch.apply(legacy)
    extruder4_main_cabinet_full_data_patch.apply(legacy)
    extruder4_main_cabinet_cleanup_patch.apply(legacy)
    extruder4_main_cabinet_click_fix.apply(legacy)
