from inc_noesis import *

def registerNoesisTypes():
	handle = noesis.register("NFS - Shift 2: Unleashed (PS3)", ".gtf")
	noesis.setHandlerTypeCheck(handle, noepyCheckType)
	noesis.setHandlerLoadRGBA(handle, noepyLoadRGBA)
	#noesis.logPopup()
	return 1

def noepyCheckType(data):
    return 1
	
def noepyLoadRGBA(data, texList):
    datasize = len(data) - 0x80        
    bs = NoeBitStream(data)
    bs.setEndian(NOE_BIGENDIAN)
    bs.seek(0x18, NOESEEK_ABS)
    imgFmt = bs.readUByte()
    print(imgFmt, "imgFmt")
    bs.seek(0x20, NOESEEK_ABS)
    imgWidth = bs.readUShort()            
    imgHeight = bs.readUShort()           
    bs.seek(0x80, NOESEEK_ABS)        
    data = bs.readBytes(datasize)      
    #DXT1
    if imgFmt == 0xA6 or imgFmt == 0x86:
        texFmt = noesis.NOESISTEX_DXT1
    #DXT5
    elif imgFmt == 0x88:
        texFmt = noesis.NOESISTEX_DXT5
    #unknown, not handled
    else:
        print("WARNING: Unhandled image format")
        return None
    texList.append(NoeTexture(rapi.getInputName(), imgWidth, imgHeight, data, texFmt))
    return 1