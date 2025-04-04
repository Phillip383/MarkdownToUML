




This piece of software will covert a markdown file into a UML diagram.
Distiguinshing the diagram type based on the heading element.

For example if the heading element is Class then it will be a class diagram.
The second heading element will be the name of the class.
The attributes and methods will be a list under the second heading element using the > character to denote a quote item.
The convertor will distinguish between an attribute and a method will the () in the list item.
To note the end of the diagram will be a double new line, or another heading element marking the beginning of the next diagram.
Other forms of UML diagrams will be added in the future.
Also, inheritance and composition syntax will need to be supported via some kind of notation.
A future feature will be to support other forms of diagrams such as relational database diagrams.
A supported editor with lsp support would be a nice addition with live preview of the diagram.

# Example
\# Class\n
\## (Person)\n

\> -name: String\n
\> -age: Int\n
\> -height: Float\n
\> +GetName(): String\n
\> +SetName(name: String): void\n
\> +GetAge(): Int\n
\> +SetAge(age: Int): void\n
\> +GetHeight(): Float\n
\> +SetHeight(height: Float): void\n

The software will be built using Python and the framework tkinter for the GUI. Supported platforms should be Windows and Linux. 
Macos will be added in the future, so keep this in mind during development. Test on a VM for now.
