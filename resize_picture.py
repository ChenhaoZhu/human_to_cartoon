import os
import cv2


def resize_img(DATADIR, data_k, img_size):
    w = img_size[0]
    h = img_size[1]
    path = DATADIR
    # 返回path路径下所有文件的名字，以及文件夹的名字，
    img_list = os.listdir(path)#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。

    for i in img_list:
        if i.endswith('.jpg'):#判断图片名称是否以".jpg"结尾
            print(i)
            # 调用cv2.imread读入图片，读入格式为IMREAD_COLOR
            img_array = cv2.imread((path + '/' + i), cv2.IMREAD_COLOR)
            # 调用cv2.resize函数resize图片
            new_array = cv2.resize(img_array, (w, h), interpolation=cv2.INTER_CUBIC)
            img_name = str(i)
            '''生成图片存储的目标路径'''
            # save_path =  'test_A/'
            save_path = 'datasets/horse2zebra/test/A/'
            if os.path.exists(save_path):
                print(i)
                '''调用cv.2的imwrite函数保存图片'''
                save_img = save_path + img_name
                cv2.imwrite(save_img, new_array)
            else:
                os.mkdir(save_path)
                save_img = save_path + img_name
                cv2.imwrite(save_img, new_array)


if __name__ == '__main__':

    # 设置图片路径
    # DATADIR = "D:\parcharm_project\Cycle_carton\datasets\horse2zebra\\test\A"
    DATADIR = "D:/Cycle_carton/Cycle_carton/datasets/horse2zebra/test/A"
    data_k = 'train_B'
    '''设置目标像素大小，此处设为512 * 512'''
    img_size = [96, 96]
    resize_img(DATADIR, data_k, img_size)
