# Some general ideas on utilization of design patterns in abjad #
===============================================================================

## SegmentMaker

The definition of SegmentMaker is something that gets called in every
segment.definition. It needs an interface to route music information that is
defined within the definition to the score object. 

Therefor the information sent by segment.definition should be conservative 
and the interface that accepts it in SegmentMaker liberal. 

In the simplest sense I want to have the SegmentMaker to: 
 + have a funnel for each context voice in the score
 + correctly parse leaves of the music streams that are intended for each context
 + keep track of global time
 + order timespans
 + keep track of segments
 + handle stylesheets

The segment definition should: 
 + prepare the music leaves into seperate, clearly identifiable streams 

