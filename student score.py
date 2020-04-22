name= input('enter students name:  ')

print('\n Enter student scores \n ')

maths=int(input('Maths:  '))
english=int(input('English:  '))
chemistry=int(input('chemistry:  '))
physics=int(input('physics: '))
biology = int(input('Biology: '))

#function to calculate grade
def assign_grade(score):
	if score >= 70:
		assign_grade = 'A'
		print(assign_grade)
	elif score >= 60:
		assign_grade = 'B'
		print(assign_grade)
	elif score >= 50:
		assign_grade = 'C'
		print(assign_grade)
	elif score >= 40:
		assign_grade= 'D'
		print(assign_grade)
	else:
		assign_grade= 'F'
		print(assign_grade)
		
#function to calculate students average
def average(maths, english, chemistry, physics, biology):
	avg = (maths+english+chemistry+physics+biology)/5
	average = avg
	print (average)
	
print(f'result statement of {name}')

print('math:  ' )
assign_grade(maths)
print('\n')

print('English:  ' )
assign_grade(english)
print('\n')

print('Chemistry:  ' )
assign_grade(chemistry)
print('\n')

print('Physics:  ' )
assign_grade(physics)
print('\n')

print('Biology:  ' )
assign_grade(biology)
print('\n')

print (f'AVERAGE SCORE OF STUDENT \n {name}')
average(maths, english, chemistry, physics, biology)