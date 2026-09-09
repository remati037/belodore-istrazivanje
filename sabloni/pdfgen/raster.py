import sys, Quartz, os
from Quartz import CoreGraphics as CG
src="/Users/marko/Desktop/Marko/belodore-istrazivanje/03-isporuke/KLAUDS_analiza_trzista_i_preporuke.pdf"
out=sys.argv[1]; pages=[int(x) for x in sys.argv[2:]]
doc=CG.CGPDFDocumentCreateWithURL(Quartz.CFURLCreateFromFileSystemRepresentation(None, src.encode(), len(src.encode()), False))
os.makedirs(out, exist_ok=True)
scale=1.7
for n in pages:
    page=CG.CGPDFDocumentGetPage(doc,n)
    r=CG.CGPDFPageGetBoxRect(page, CG.kCGPDFMediaBox)
    w=int(r.size.width*scale); h=int(r.size.height*scale)
    cs=CG.CGColorSpaceCreateDeviceRGB()
    ctx=CG.CGBitmapContextCreate(None,w,h,8,0,cs,CG.kCGImageAlphaPremultipliedFirst|CG.kCGBitmapByteOrder32Host)
    CG.CGContextSetRGBFillColor(ctx,1,1,1,1); CG.CGContextFillRect(ctx,CG.CGRectMake(0,0,w,h))
    CG.CGContextScaleCTM(ctx,scale,scale)
    CG.CGContextDrawPDFPage(ctx,page)
    img=CG.CGBitmapContextCreateImage(ctx)
    url=Quartz.CFURLCreateFromFileSystemRepresentation(None, (out+"/p%02d.png"%n).encode(), len((out+"/p%02d.png"%n).encode()), False)
    d=Quartz.CGImageDestinationCreateWithURL(url,"public.png",1,None)
    Quartz.CGImageDestinationAddImage(d,img,None); Quartz.CGImageDestinationFinalize(d)
    print("p%02d"%n)
