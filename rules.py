# -*- coding: utf-8 -*-
import csv

def write_rule(uid, min_size_torrent=0.99, min_size_adopted=4000, \
min_num_adopted=100, min_seedingtime = 12.5, \
adoption_number_ratio = '1 1 adoption_number_ratio_function', \
adoption_size_ratio = '1 1 adoption_size_ratio_function', \
adoption_bonus_ratio = '1 0.8 0.6 0.3', \
code_official_group = '1 6 9 18 22 28 31 34 35', \
code_invalid_category = '402', salary_ratio = 1, \
size_for_salary_ratio = 1, addedtime_for_salary_ratio = 1, \
seedingtime_for_salary_ratio = 1, seeders_for_salary_ratio = 1, \
max_seeders_for_salary = 0, min_size_first_adoption_ratio = 0.5 ,comment = ''):

	""" Takes uid and optional assessment parameters. Save the
	customized assessment scheme to database."""
	
	# input bundle
	bundle = input('请输入数字1至5选择套餐：1.酱油 2.实习 3.正式 4.资深 5.特招, \
	其余输入视为默认输入,enter进入下一步')
	
	# prevent null input
	if bundle:
		if bundle == '1':
			min_size_adopted = 2048
			salary_ratio = 0.4
			comment = '酱油保种员'	
			print ('您选择了酱油保种员')
		elif bundle == '2':
			min_size_adopted = 4096
			salary_ratio = 0.6
			comment = '实习保种员'	
			print ('您选择了实习保种员')			
		elif bundle == '3':
			min_size_adopted = 6144
			salary_ratio = 0.8
			comment = '正式保种员'
			print ('您选择了正式保种员')
		elif bundle == '4':
			min_size_adopted = 8192
			comment = '资深保种员'
			print ('您选择了资深保种员')
		elif bundle == '5':
			min_size_adopted = 10240
			salary_ratio = 0.8
			comment = '特招保种员'
			print ('您选择了特招保种员')
	
	# create a set of exitsted uid
	existed_uid = set()
	
	# initialize min_size_first_adoption
    # confirm the parameters
	print ('请再次检查以下参数')
	print ('用户id:', uid, '\n', \
	'最小单种体积:', min_size_torrent, '\n', \
	'最少总认领体积:', min_size_adopted, '\n', \
	'最少总认领数:', min_num_adopted, '\n', \
	'最少做种时间:', min_seedingtime, '\n', \
	'认领名次合格种子数比例:', adoption_number_ratio, '\n', \
	'认领名次合格种子数体积比例:', adoption_size_ratio, '\n', \
	'认领名次魔力比例:', adoption_bonus_ratio, '\n', \
	'合格认领小组:', code_official_group, '\n', \
	'不合格认领分类:', code_invalid_category, '\n', \
	'工资比例:', salary_ratio, '\n', \
	'工资体积系数:', size_for_salary_ratio, '\n', \
	'工资种子寿命系数:', addedtime_for_salary_ratio, '\n', \
	'工资做种时间系数:', seedingtime_for_salary_ratio, '\n', \
	'工资做种人数系数:', seeders_for_salary_ratio, '\n', \
	'最多允许同伴数:', max_seeders_for_salary, '\n', \
	'最少第一认领占总体积比：', min_size_first_adoption_ratio, \
	'即第一认领最少体积为：',\
	min_size_first_adoption_ratio * min_size_adopted, 'GB', '\n', \
	'备注：', comment)
	
	confirm = str(input("Enter 'yes' if to proceed, otherwise exit"))
	


	
    # exit if not confirmed
	if confirm != 'yes':
		print ('Aborted!')
		return
	
	filename = 'rules'
	
	with open(filename, 'a', newline = '', encoding = 'utf-8') as f:
		fieldnames = ['用户id', '最小单种体积', '最少总认领体积', \
		'最少总认领数', '最少做种时间', \
		'认领名次合格种子数比例', '认领名次合格种子数体积比例', \
		'认领名次魔力比例', '合格认领小组', '不合格认领分类', \
		'工资比例', '工资体积系数',	'工资种子寿命系数', \
		'工资做种时间系数', '工资做种人数系数', '最多允许同伴数', \
		'最少第一认领占体积比', '备注']
	
		thewriter = csv.DictWriter(f, fieldnames = fieldnames)
    
        # decide to write or not to write the title
		if not (f.tell()):
			thewriter.writeheader()
	
		# get all the existed uid in a set to aovid dup rules
		rf = csv.DictReader(open(filename, encoding = 'utf-8'))
		for i in rf:
			existed_uid.add(i['用户id'])
		
		# in case input is a list
		if isinstance(uid, list):
			
			for this_uid in uid:
				
				if this_uid not in existed_uid:
					thewriter.writerow({'用户id':this_uid, \
					'最小单种体积': min_size_torrent, \
					'最少总认领体积': min_size_adopted, \
					'最少总认领数': min_num_adopted, \
					'最少做种时间': min_seedingtime, \
					'认领名次合格种子数比例': adoption_number_ratio, \
					'认领名次合格种子数体积比例': adoption_size_ratio, \
					'认领名次魔力比例': adoption_bonus_ratio, \
					'合格认领小组': code_official_group, \
					'不合格认领分类': code_invalid_category, \
					'工资比例': salary_ratio, \
					'工资体积系数': size_for_salary_ratio, \
					'工资种子寿命系数': addedtime_for_salary_ratio, \
					'工资做种时间系数': seedingtime_for_salary_ratio, \
					'工资做种人数系数': seeders_for_salary_ratio, \
					'最多允许同伴数': max_seeders_for_salary, \
					'最少第一认领占体积比': min_size_first_adoption_ratio, \
					'备注': comment})
					
				else:
					print ('错误！该id已设置规则!')
					
		# in case it's not a list
		else:
			if uid not in existed_uid:
				thewriter.writerow({'用户id':uid, \
				'最小单种体积': min_size_torrent, \
				'最少总认领体积': min_size_adopted, \
				'最少总认领数': min_num_adopted, \
				'最少做种时间': min_seedingtime, \
				'认领名次合格种子数比例': adoption_number_ratio, \
				'认领名次合格种子数体积比例': adoption_size_ratio, \
				'认领名次魔力比例': adoption_bonus_ratio, \
				'合格认领小组': code_official_group, \
				'不合格认领分类': code_invalid_category, \
				'工资比例': salary_ratio, \
				'工资体积系数': size_for_salary_ratio, \
				'工资种子寿命系数': addedtime_for_salary_ratio, \
				'工资做种时间系数': seedingtime_for_salary_ratio, \
				'工资做种人数系数': seeders_for_salary_ratio, \
				'最多允许同伴数': max_seeders_for_salary, \
				'最少第一认领占体积比': min_size_first_adoption_ratio, \
				'备注': comment})		
			else:
				print ('错误！',uid,'该id已设置规则!')