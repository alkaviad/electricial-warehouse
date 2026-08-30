try:
    import legacy
    import control_catalog_patch
    import control_descriptions_patch
    import control_cleanup_patch
    import extruder_location_label_patch
    import extruder_panels_patch
    import extruder_main_cabinet_patch
    import table_style_patch
    control_catalog_patch.apply(legacy)
    control_descriptions_patch.apply(legacy)
    control_cleanup_patch.apply(legacy)
    extruder_location_label_patch.apply(legacy)
    extruder_panels_patch.apply(legacy)
    extruder_main_cabinet_patch.apply(legacy)
    table_style_patch.apply(legacy)
except Exception:
    pass
