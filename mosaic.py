#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Mosaic:
    
    def mosaic(image1, image2):
        
        image3 = resize_image(image1, image1.width/5, image1.height/5)
        image4 =resize_image(image2, image2.width/5, image2.height/5)
        
        # 縮小した画像で、画像が最も重なるとこのパラメタを概算
        j_min1, i_min1, t_min1 = get_min_params(image3, image4)
        
        # 元の画像でパラメタを計算
        j_min2, i_min2, t_min2 = get_min_params(image1, image2)
        
        # TODO double型に変換
        return j_min2, i_min2, t_min2
        
    def resize_image(image, width, height):
        
        res_image.width = width
        res_image.height = height
        
        #元の画像と新しい画像の大きさの比を計算
        step_x = image.width / width
        step_y = image.height / height
        
        # ピクセルのコピー
        for i in range(height):
            for j in range(width):
                r, g, b = 0
                count = 0
                for k in range(step_y*i, step_y*(i+1)-1):
                    for l in range(step_x*j, step_x(j+1)-1):
                        if( k >= image.height or l >= image.width):
                            continue
                        count += 1 
                        r += image.pixel[k][l].r
                        g += image.pixel[k][l].g
                        b += image.pixel[k][l].b
                res_image.pixel[i][j].r = r /count
                res_image.pixel[i][j].g = g /count
                res_image.pixel[i][j].b = b /count
        
        return res_image
    
    def get_min_params(image1, image2, xmin, xmax, ymin, ymax, tmin, tmax, tstep):
        
        return
        
        
            

