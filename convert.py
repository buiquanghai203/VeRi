import os
from xml.dom.minidom import parse

vehicleids = []

def convert_annotation(input_fp, output_fp, subdir):
    in_file = open(input_fp)
    list_file = open(output_fp, 'w')
    tree = parse(in_file)

    root = tree.documentElement

    for item in root.getElementsByTagName("Item"):  
        label = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        if item.hasAttribute("imageName"):
            name = item.getAttribute("imageName")
        if item.hasAttribute("vehicleID"):
            vehicleid = item.getAttribute("vehicleID")
            if vehicleid not in vehicleids :
                vehicleids.append(vehicleid)
            vid = vehicleids.index(vehicleid)
        if item.hasAttribute("colorID"):
            colorid = int (item.getAttribute("colorID"))
            label[colorid-1] = '1'
        if item.hasAttribute("typeID"):
            typeid = int (item.getAttribute("typeID"))
            label[typeid+9] = '1'
        label = ','.join(label)
        list_file.write(os.path.join(subdir, name)  + "\t" + label + "\n")

    list_file.close()

convert_annotation('train_label.xml', 'train_list.txt', 'image_train')  #imagename vehiclenum colorid typeid
convert_annotation('test_label.xml', 'test_list.txt', 'image_test')