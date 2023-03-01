#!/usr/bin/python3

class Hello:
  def __init__(self):
      print('Hello constructor ...')

  def sayHello(self,msg):
      print ( msg )

hello = Hello()
hello.sayHello ( 'Hello Python !' )
