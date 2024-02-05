f = CurrentFont()

for l in f.layers:
    base_path = f.path.replace(".ufo", "")
    full_path = base_path + "-" + l.name + ".otf"
    
    f.generate("otf", path=full_path, layerName=l.name)
    
    print(f"Generated {l.name} as an OTF at {full_path}.")
