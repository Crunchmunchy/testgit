#this is the readme file version for the container Yaml file
import yaml
f = open("newtest.yaml","r")
print(f.read())

a = open("newtest.yaml","a")
a.write("Tomahawk")

a.delete