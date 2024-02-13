import damask
import numpy as np
#Импорт ориентаций из файла
ori = np.loadtxt('Cu_orient.txt') 
#Запись ориентаций из файла в переменную конфигурации
config = damask.ConfigMaterial().material_add(O=damask.Rotation.from_quaternion(ori, accept_homomorph=True),phase='Cu',homogenization='SX') 
print(f'configuration is{" " if config.is_valid else " not "}valid\n')
