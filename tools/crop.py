import sys, json
from PIL import Image
import os
# Folder holding the PDF page renders (full-1.png ... full-5.png), made with:
#   pdftoppm -r 144 -png portfolio.pdf <folder>/full
S=os.environ.get('RENDERS_DIR', '.').rstrip('/') + '/'
crops = {
 'me':          (1,(158,1077,469,1544)),
 'tti-hero':    (2,(0,0,1600,755)),
 'tti-circle':  (2,(0,942,1600,1553)),
 'tti-layout':  (2,(0,1780,1600,2301)),
 'tti-content': (2,(108,2312,773,2679)),
 'tti-refine':  (2,(809,2769,1492,3183)),
 'tti-sustain': (2,(144,3218,1560,3956)),
 'sig-hero':    (3,(0,0,1600,707)),
 'sig-signs':   (3,(986,781,1562,1228)),
 'sig-process': (3,(93,1786,1525,2176)),
 'sig-pain':    (3,(93,2232,1525,2585)),
 'sig-goals':   (3,(93,2957,1525,3162)),
 'sig-wire':    (3,(93,4148,1525,4929)),
 'sig-style':   (3,(93,5096,1525,5760)),
 'sig-hifi':    (3,(93,5803,1525,7440)),
 'conta-hero':  (4,(0,467,1600,971)),
 'conta-a':     (4,(0,1025,1600,2900)),
 'conta-b':     (4,(0,2900,1600,4818)),
 'ds-hero':     (5,(0,0,1600,763)),
 'ds-color':    (5,(93,1060,1525,1488)),
 'ds-type':     (5,(93,1879,1525,2325)),
 'ds-icon':     (5,(93,2660,1525,3218)),
 'ds-button':   (5,(93,3720,1525,4420)),
 'ds-input':    (5,(93,4850,1525,5904)),
}
if len(sys.argv)>1 and sys.argv[1]=='sheet':
    names=list(crops)
    thumbs=[]
    for n in names:
        p,b=crops[n]; im=Image.open(f'{S}full-{p}.png').convert('RGB').crop(b); im.thumbnail((300,300)); thumbs.append(im)
    W=320*6; rows=(len(thumbs)+5)//6; sheet=Image.new('RGB',(W,rows*320),'white')
    for i,t in enumerate(thumbs): sheet.paste(t,((i%6)*320,(i//6)*320))
    sheet.save(S+'sheet.png')
else:
    out=sys.argv[1]
    import os; os.makedirs(out,exist_ok=True)
    for n,(p,b) in crops.items():
        im=Image.open(f'{S}full-{p}.png').convert('RGB').crop(b)
        im.save(f'{out}/{n}.webp','WEBP',quality=72,method=6)
        if n!='me':
            w=800; h=round(im.height*w/im.width)
            im.resize((w,h),Image.LANCZOS).save(f'{out}/{n}-sm.webp','WEBP',quality=72,method=6)
        print(n, im.size, os.path.getsize(f'{out}/{n}.webp')//1024,'KB')
