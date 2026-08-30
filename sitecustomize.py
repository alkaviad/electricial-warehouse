try:
    import legacy
    import extruder_main_cabinet_patch
    extruder_main_cabinet_patch.apply(legacy)
except Exception:
    pass
