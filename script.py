#range start at 1, end at 1+last (max 101)
#img element will have src, alt, id - no

with open("README.md","w") as f:
    f.write('<body style="background-color: #1b1b29; color: antiquewhite;">')
    f.write('<h1>WALLPAPERS I COLLECTED FROM THE INTERNET</h1><br><p><a href="https://lemondiee.github.io/wallpapers">Wallpapers</a> are indexed according to file extention (jpg/jpeg/png), folders (starting from "1") and image number (1 to 100)</p> ')

    f.write('<h2>JPG</h2>')
    for i in range(1,7):
        for j in range(1,101):
            f.write(f'<img src="WALLPAPER/jpg/{i}/wallpaper ({j}).jpg" alt="wallpaper ({j})" id="jpg-{i}-{j}"/> <br>')
    for k in range(1,50):
        f.write(f'<img src="WALLPAPER/jpg/7/wallpaper ({k}).jpg" alt="wallpaper ({k})" id="jpg-7-{k}"/> <br>')

    f.write('<h2>JPEG</h2>')
    for l in range(1,7):
        f.write(f'<img src="WALLPAPER/jpeg/1/wallpaper ({l}).jpeg" alt="wallpaper ({l})" id="jpeg-1-{l}"/> <br>')

    f.write('<h2>PNG</h2>')
    for m in range(1,59):
        f.write(f'<img src="WALLPAPER/png/1/wallpaper ({m}).png" alt="wallpaper ({m})" id="png-1-{m}"/> <br>')
    
    f.write('<h2>Thanks for visiting <a href="https://lemondiee.github.io/wallpapers">my collection</a>. I donot own any of these. All are collected from Internet sources</h2>')
    f.write('</body>')
#Thanks. By @lemondiee