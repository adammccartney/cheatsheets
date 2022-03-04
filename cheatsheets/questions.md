## General (python) programming questions ##

* What way to classes inherit when the subclass has the same name as the super
  class?
  Answer: Because of the nature of python namesspaces (one per module) each
  class will always have a unique name, determined by their namespace. 
  - This question was actually poking at something at a higher level of oop 
    design patterns, and specifically related to the use of factory classes.
    The structure of the factory classes in abjad is that typically, something 
    like a SegmentMaker will have one abstract Factory definition, followed by
    one concrete Factory definition per Score. Each segment of the score will
    then contain one instance of the SegmentMaker class.      
  + Considering this pattern and borrowing on a little inspiration from a real
    factory (with workers and a production line): a useful way of understanding 
    what sort of layouts will work better for a concrete factory instance, it
    makes sense to understand the production workers and what they are capable
    or more interested in doing. In the case of Factory Classes, the workers
    are the data structures that will appear in the instantiation of a specific
    class.    

