import extruder4_main_cabinet_inventory_patch
import extruder4_main_cabinet_full_data_patch

def apply(legacy):
    extruder4_main_cabinet_inventory_patch.apply(legacy)
    extruder4_main_cabinet_full_data_patch.apply(legacy)
