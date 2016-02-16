#!/usr/bin/env python

class Person:
	def __init__(self, name, last_name):
		self.name = name
		self.last_name = last_name

	def introduce(self):
		print("Hello my name is: " +
			self.name + " " + self.last_name)

	def set_age(self, age):
		sef.age = age

class Boss(Person):
	def set_salary(self, salary):
		self.salary = salary

	def get_money(self):
		return self.salary
	
	def introduce(self):
		Person.introduce(self)

		print("I make %d a year.\n" % self.salary)

boss = Boss("Jack", "Sparrow")

boss.set_salary(10000)

boss.introduce()
print("I make %d a yar\n" % boss.get_money())
