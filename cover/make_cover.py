import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
REPO=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F=os.path.expanduser('~/.fonts/')
DPI=300; PAGES=int(sys.argv[1]) if len(sys.argv)>1 else 54
BLEED=0.125; TW,TH=6.0,9.0
SPINE=PAGES*0.002252           # KDP white paper, B&W
W=round((BLEED*2+TW*2+SPINE)*DPI); H=round((TH+BLEED*2)*DPI)
px=lambda inch: round(inch*DPI)
BG=(154,177,193); TEAL=(0,128,129); NAVY=(24,38,54); WHITE=(255,255,255)
img=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(img)
front_x=px(BLEED+TW+SPINE)            # left edge of front panel (spine fold)
FW=W-front_x                          # front width incl. right bleed
import subprocess
def font(name,pt):
    # find Montserrat via fontconfig, so it works wherever the font is installed
    path=subprocess.run(['fc-match','-f','%{file}',f'Montserrat:style={name}'],capture_output=True,text=True).stdout
    return ImageFont.truetype(path or F+f'Montserrat-{name}.otf', round(pt*DPI/72))

# ---- photo band across bottom of front (crop from source photo, no upscaling needed)
band_h=px(3.75)
ph=Image.open(f'{REPO}/pearl-2045162_1920.jpg').convert('RGB')
s=max(FW/ph.width, band_h/ph.height); ph=ph.resize((round(ph.width*s),round(ph.height*s)),Image.LANCZOS)
ox=(ph.width-FW)//2; oy=ph.height-band_h
img.paste(ph.crop((ox,oy,ox+FW,oy+band_h)),(front_x,H-band_h))

# ---- front text (left/right inner margins measured from trim)
L=front_x+px(0.55); R=W-px(BLEED+0.55)
def text(xy,s,f,fill,anchor='la'): d.text(xy,s,font=f,fill=fill,anchor=anchor)
pt=100
while True:
    t=font('Black',pt)
    if d.textlength('Taster',font=t) <= px(4.7): break
    pt-=1
cap=-d.textbbox((0,0),'P',font=t,anchor='ls')[1]
b1=px(BLEED+0.95)+cap
text((L,b1),'Perl',t,WHITE,'ls')
b2=b1+round(cap*1.28)
text((L,b2),'Taster',t,WHITE,'ls')
text((L+px(0.04),b2+px(0.6)),'Your first two hours with Perl',font('Regular',22),WHITE,'ls')
text((R,b2+px(1.35)),'Dave Cross',font('Bold',32),WHITE,'rs')
print('title pt',pt,'title bottom in',round(b2/DPI,2))
# logo box bottom-right
lg=Image.open(f'{REPO}/cover.jpg').convert('RGB').crop((898,2357,1546,2500))
lw=px(1.7); lg=lg.resize((lw,round(lg.height*lw/lg.width)),Image.LANCZOS)
pad=px(0.06); bx=R-lw-pad; by=H-px(BLEED+0.45)-lg.height
d.rectangle((bx-pad,by-pad,bx+lw+pad,by+lg.height+pad),fill=WHITE); img.paste(lg,(bx,by))

# ---- 45-degree "Second Edition" flash across top-right corner (extends into bleed)
size=px(2.4); fl=Image.new('RGBA',(size*3,size*3),(0,0,0,0)); fd=ImageDraw.Draw(fl)
cx=cy=size*3//2; bh=px(0.56)
fd.rectangle((0,cy-bh//2,size*3,cy+bh//2),fill=TEAL+(255,))
fd.text((cx,cy-px(0.02)),'SECOND EDITION',font=font('ExtraBold',14.5),fill=WHITE,anchor='ms')
fd.text((cx,cy+px(0.19)),'Covers Perl v5.36',font=font('Medium',9),fill=WHITE,anchor='ms')
fl=fl.rotate(-45,resample=Image.BICUBIC)   # clockwise: band runs from the top edge down to the right edge
# position: band centre line crosses top trim at dist D from right trim corner
D=px(1.75); corner=(W-px(BLEED), px(BLEED))
mid=(corner[0]-D/2, corner[1]+D/2)
img.paste(fl,(round(mid[0]-fl.width/2),round(mid[1]-fl.height/2)),fl)

# ---- back cover
BL=px(BLEED+0.6); BR=px(BLEED+TW-0.6); y=px(BLEED+0.85)
hd=font('ExtraBold',21); bf=font('Regular',11.2); bb=font('SemiBold',11.2)
def wrap(s,f,width):
    words=s.split(); lines=[]; cur=''
    for w_ in words:
        tst=(cur+' '+w_).strip()
        if d.textlength(tst,font=f)<=width: cur=tst
        else: lines.append(cur); cur=w_
    lines.append(cur); return lines
def para(s,f=bf,fill=NAVY,gap=0.16,indent=0):
    global y
    for ln in wrap(s,f,BR-BL-indent):
        text((BL+indent,y),ln,f,fill,'la'); y+=round(f.size*1.42)
    y+=px(gap)
for ln in ['Learn enough Perl to write','useful programs—in about','two hours.']:
    text((BL,y),ln,hd,WHITE,'la'); y+=round(hd.size*1.2)
y+=px(0.3)
para("Perl is a powerful, flexible programming language that is installed on almost every computer. Perl Taster is a short, friendly introduction for people who have never written any Perl. It doesn't try to cover everything—just enough to get you writing real programs.")
para("You'll learn about:",bb,gap=0.06)
for b in ["scalars, arrays and hashes","input and output, and reading and writing files","making decisions and looping","Perl's most useful built-in functions","writing your own subroutines","the basics of regular expressions"]:
    text((BL+px(0.08),y),'•',bf,TEAL,'la'); para(b,gap=0.02,indent=px(0.28))
y+=px(0.14)
para("This second edition has been updated throughout for modern Perl. Every example uses the features of Perl 5.36—including say() and subroutine signatures—so you'll be learning Perl the way it is written today.")
y+=px(0.08)
para("Dave Cross has been a professional programmer since 1988 and has used Perl since 1996. He founded the London Perl Mongers in 1998 and is the author of Data Munging with Perl.",font('Italic',10.5),gap=0.1)
# small logo bottom-left of back; barcode area bottom-right left clear (KDP adds it: 2" x 1.2")
lg2=lg.resize((px(1.35),round(lg.height*px(1.35)/lg.width)),Image.LANCZOS)
by2=H-px(BLEED+0.45)-lg2.height; d.rectangle((BL-pad,by2-pad,BL+lg2.width+pad,by2+lg2.height+pad),fill=WHITE); img.paste(lg2,(BL,by2))
barcode=(px(BLEED+TW-0.25-2.0),H-px(BLEED+0.25+1.2),px(BLEED+TW-0.25),H-px(BLEED+0.25))
if '--guides' in sys.argv:
    g=ImageDraw.Draw(img)
    for x in (px(BLEED),px(BLEED+TW),front_x,W-px(BLEED)): g.line((x,0,x,H),fill=(255,0,0),width=3)
    for yy in (px(BLEED),H-px(BLEED)): g.line((0,yy,W,yy),fill=(255,0,0),width=3)
    g.rectangle(barcode,outline=(255,0,0),width=4)
out=sys.argv[2] if len(sys.argv)>2 else 'perl-taster-cover'
img.save(out+'.png'); img.save(out+'.pdf',resolution=DPI)
print(W,H,'spine in',round(SPINE,4),'y_end_back_text_in',round(y/DPI,2),'barcode_top_in',round(barcode[1]/DPI,2))
