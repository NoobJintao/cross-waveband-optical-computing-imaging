import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

dir=r'F:\retrieved_process' ###input directory
def img_bits(choice):
    if choice=='8bit':
        img_path=dir+'/'+choice+'.jpg'
        img=plt.imread(img_path)
        img=img[:,:,0]
    elif choice=='16bit':
        img_path=dir+'/'+choice+'.fit'
        img=fits.open(img_path)
        img=img[0].data
    else:
        print("Note:please input 8bit or 16bit and ensure the prepared filenames are 8bit.jpg and 16bit.fit, respectively")
    img=img/np.max(img)*255
    size=img.shape[0]*img.shape[1]
    img_1D=img.reshape((1,size))
    d=1
    fre=[]
    x=np.arange(0,255,d)
    for i in range(255):
        new_img_1D=np.delete(img_1D,np.where(img_1D>i+d))
        new_img_1D=np.delete(new_img_1D,np.where(new_img_1D<=i))
        fre.append(new_img_1D.shape[0])
    plt.plot(x,fre,ls=':')
    plt.ylabel('The number of pixels')
    plt.xlabel('Gray value')
    plt.show()
    half_gray=round(255/2)
    fre_sel=fre[half_gray:]
    back_val=np.argmax(fre_sel)+half_gray
    img=img-back_val
    img=(img+abs(img))/2
    if choice=='8bit':
        img=img/np.max(img)*255
        im=plt.imshow(img,cmap='gray')
        plt.clim(0,255)
        cbar=plt.colorbar(im)
        cbar.set_ticks([0,255])
        cbar.ax.tick_params(labelsize=16)
        plt.xticks([0,1359],fontsize=16)
        plt.yticks([0,767],fontsize=16)   
        plt.show()
    elif choice=='16bit':
        img=img/np.max(img)*65535
        im=plt.imshow(img,cmap='gray')
        plt.clim(0,65535)
        cbar=plt.colorbar(im)
        cbar.set_ticks([0,65535])
        cbar.ax.tick_params(labelsize=16)
        plt.xticks([0,1359],fontsize=16)
        plt.yticks([0,767],fontsize=16)   
        plt.show()


###input '8bit' or '16bit'
img_bits('8bit')
img_bits('16bit')  

