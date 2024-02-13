import damask
import numpy as np
#Импорт ориентаций из файла
ori = np.loadtxt('Cu_orient.txt') 
#Запись ориентаций из файла в переменную конфигурации
config = damask.ConfigMaterial().material_add(O=damask.Rotation.from_quaternion(ori, accept_homomorph=True),phase='Cu',homogenization='SX') 
print(f'configuration is{" " if config.is_valid else " not "}valid\n')
#Запись параметров материала в переменную конфигурации
config['phase']['Cu'] = damask.ConfigMaterial.load('CuNb.yaml')
config['homogenization']['SX'] = {'N_constituents':1,'mechanical':{'type':'pass'}}
config.save()
config
#Импорт ориентаций из файла
ori = np.loadtxt('Nb_orient.txt') 
#Запись ориентаций из файла в переменную конфигурации
config = damask.ConfigMaterial().material_add(O=damask.Rotation.from_quaternion(ori, accept_homomorph=True),phase='Nb',homogenization='SX') 
print(f'configuration is{" " if config.is_valid else " not "}valid\n')
#Запись параметров материала в переменную конфигурации
config['phase']['Nb'] = damask.ConfigMaterial.load('CuNb.yaml')
#Ввыод на экран
config
config['homogenization']['SX'] = {'N_constituents':1,'mechanical':{'type':'pass'}}
config.save()
config.save()
len(config['material'])
