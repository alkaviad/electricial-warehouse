try:
    import legacy
    import control_catalog_patch
    import control_descriptions_patch
    import extruder_panels_patch
    import extruder_main_cabinet_patch
    control_catalog_patch.apply(legacy)
    control_descriptions_patch.apply(legacy)
    extruder_panels_patch.apply(legacy)
    extruder_main_cabinet_patch.apply(legacy)
except Exception:
    pass
