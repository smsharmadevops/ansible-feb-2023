#!/usr/bin/python3

class Hello:
  def __init__(self):
      print('Hello constructor ...')

  def publicMethod(self,msg):
      print ( msg )

  def _protectedMethod(self,msg):
      print ( msg )

  def __privateMethod(self,msg):
      print ( msg )

  def invokePrivateMethod(self,msg):
      self.__privateMethod(msg)

hello = Hello()
hello.publicMethod ( 'Public method' )
hello._protectedMethod ( 'Protected method' )
hello.invokePrivateMethod( 'Private Method invoked via a Public method indirectly' )
