import os

images_dir = "assets/images"
image_files = os.listdir(images_dir) if os.path.exists(images_dir) else []

target_htmls = ["index.html", "index2.html"]

for html_file in target_htmls:
    if os.path.exists(html_file):
        with open(html_file, "r") as f:
            content = f.read()
        
        for img in image_files:
            if img.startswith("."): continue
            
            # Typical src="", src='', url("..."), url('...'), url(...)
            content = content.replace(f'"{img}"', f'"assets/images/{img}"')
            content = content.replace(f"'{img}'", f"'assets/images/{img}'")
            content = content.replace(f'url({img})', f'url(assets/images/{img})')
        
        with open(html_file, "w") as f:
            f.write(content)
            
design_file = "references/design-system.html"
if os.path.exists(design_file):
    with open(design_file, "r") as f:
        content = f.read()
    content = content.replace("../white-medical/assets/", "white-medical/assets/")
    with open(design_file, "w") as f:
        f.write(content)

print("Done")
