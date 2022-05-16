#Why functions need to be imported individually? Can't just import a module :S
#from xyz import abc -syntax implies to bring an individual function.

import MyModule
import MySubPackage.MySubModule

MyModule.modulefunc()
MySubPackage.MySubModule.submodulefunc()
MySubPackage.MySubModule.submodulefunc2()

