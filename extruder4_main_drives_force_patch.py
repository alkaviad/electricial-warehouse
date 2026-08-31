import extruder4_main_cabinet_inventory_patch

def apply(legacy):
    # Single main-cabinet UI owns both category tiles and their detail table.
    # Do not apply the old navigation/drives patch: it injected a second
    # drives table underneath contactors and other selected categories.
    extruder4_main_cabinet_inventory_patch.apply(legacy)
