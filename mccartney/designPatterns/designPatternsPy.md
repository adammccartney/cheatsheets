### Some common design patterns implemented in Python ###
===============================================================================

## Factory Method

Overview of factory method implementation in python: 
<https://realpython.com/factory-method-python/>


 Is a creational design pattern used to make a concrete implementation of a
 common interface 
 
 Seperates process of creation from the code that depends on the interface

 For example: 
     a program for formalized score control requires an Score object that has 
     an interface that allows us to add notes/rhythms/markups. The concrete 
     implementation of this interface is identified by the number of
     instruments and staffs that will be used in the score.
     In abjad a score object becomes a type of Global Container, an object that
     effectively connects all of the musical information. This information is
     coordinated on two 'axes' 

 + vertically, *n* context voices are stacked examples might include: 
   - voice Dynamics context
   - voice Music context
   - voice Markup context

 + horizontally, *n* segments are positioned one after another. These segments
   are controlled using timespans
