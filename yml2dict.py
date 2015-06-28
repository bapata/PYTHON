import yaml
f = open('tree.yaml')
# use safe_load instead load
dataMap = yaml.safe_load(f)
f.close()
print dataMap
