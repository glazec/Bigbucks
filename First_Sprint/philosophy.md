Watch 1 A Philosophy of Software Design (John Ousterhout, 2018)

Key words: deep module | complexity | modular design | software design | Strategic programming

Main points: 
In this talk, John synthesizes his experiences into an insightful and provocative discussion on how to (and how not to) design software.<br/>

The most important technique for achieving deep modules is information hiding.<br/>
 
Information hiding reduces complexity in two ways. First, it simplifies the interface to a module. The interface reflects a simpler, more abstract view of the module’s functionality and hides the details; this reduces the cognitive load on developers who use the module. Second, information hiding makes it easier to evolve the system. If a piece of information is hidden, there are no dependencies on that information outside the module containing the information, so a design change related to that information will affect only the one module.<br/>

The general-purpose approach provides a cleaner separation between the text and user interface classes, which results in better information hiding.<br/>
 
New user interface features can be added without creating new supporting functions in the text class.<br/>
 

General-purpose interfaces have many advantages over special-purpose ones.<br/>

They tend to be simpler, with fewer methods that are deeper. They also provide a cleaner separation between classes, whereas special-purpose interfaces tend to leak information between classes. Making your modules somewhat general purpose is one of the best ways to reduce overall system complexity.<br/>

Strengths and weaknesses: 
One strength is that John extracted some key points and highlighted them. <br/>
For instance-Red flag: Information leakage occurs when the same knowledge is used in multiple places, such as two different classes that both understand the format of a particular type of file.<br/>
One weakness is that more simple example and charts could be displayed to help readers understand.