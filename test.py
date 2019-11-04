import os
import shutil

work_people = ['wjl', 'shf', 'hxj']

project_dir = ''

def divide_img_and_label(file_dir):
    img_dir = os.path.join(file_dir, 'JPEImages')
    label_dir = os.path.join(file_dir, 'Annotations')
    img_list = [os.path.join(img_dir, img) for img in os.listdir(img_dir)]
    num_of_banch = len(img_list) // len(work_people)
    for i in range(num_of_people):
        temp_img_list = img_list[i*num_of_banch:(i+1)*num_of_banch]
        people_dir = work_people[i]
        save_dir = os.path.join(file_dir, people_dir)
        os.makedirs(save_dir)
        for img in temp_img_list:
            label_name = os.path.splitext(os.path.split(img)[-1])[0] + '.xml'
            label_path = os.path.join(label_dir, label_name)
            shutil.copyfile(img, os.path.join(save_dir, os.path.split(img)[-1]))
            shutil.copyfile(label_path, os.path.join(save_dir, label_name))

if __name__ == '__main__':
    divide_img_and_label(project_dir)
