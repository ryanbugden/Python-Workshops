f = CurrentFont()

# Loop though all layers
for l in f.layers:
    # Construct a file path for each new layer otf
    base_path = f.path.replace(".ufo", "")
    full_path = base_path + "-" + l.name + ".otf"
    # Generate the OTF
    f.generate("otfcff", path=full_path, layerName=l.name)
    print(f"Generated {l.name} as an OTF at {full_path}.")
