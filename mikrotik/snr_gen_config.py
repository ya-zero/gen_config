# -*- coding: utf-8 -*-

from template import generate_cfg_from_template

template_file='snr/mikrotik_sector_template.txt'
yaml_file='snr_data/mikrotik.yaml'
#print (template_file,yaml_file)
config=generate_cfg_from_template(template_file,yaml_file)
print (config)

