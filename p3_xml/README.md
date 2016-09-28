# XML Processing with Java

## 1. Introduction

While nowadays JSON is replacing XML in many data-interchange scenarios, XML is still a broadly used language, with unique features that still make it the first choice in some situations. The purpose of this assignment is to learn an easy way to process XML documents with Java. We will use JDOM, a library for enabling rapid development of XML applications. Though it's not necessary, you can take a look to [this article](http://unpetitaccident.com/pub/compeng/languages/JAVA/Tutorials/JDOM/simplify%20XML%20programming%20with%20jdom.pdf) to get more information about JDOM. 

*NOTE: You can use a different programming language (e.g. Python) and/or different libraries (there are [many for Java](https://en.wikipedia.org/wiki/Java_XML)). In that case, just jump to [Section 3](#3-lab-assignment).*

## 2. Setup

### 2.1 Booting the machine

Select the latest Ubuntu imatge (e.g. Ubuntu 14)

    user: alumne
    pwd: sistemes


### 2.2 Download the example and the libraries

Install git if necessary:

    sudo apt-get install git

Download the sources (if you already have the pti repository, just do a git pull to update it):

    cd $HOME       
    git clone https://gitlab.fib.upc.edu/pti/pti.git

    cd pti/p3_xml
    ls

### 2.3 Set the Java classpath and run the example

Set the Java classpath this way:

    export CLASSPATH=./xalan.jar:./xercesImpl.jar:./jdom.jar:.

Now build the example:

    javac Example.java

And run it:

    java Example

## 3 Lab assignment 

You have to program a console application that keeps information about car rentals in an XML file named carrental.xml. The application will accept just one parameter that will specify the action to be performed. After executing one action the application will finish. These are the actions that the application must provide:


### 3.1 reset

Command:

    java CarRental reset

The application will create a new XML document (in memory) with the following structure:
    
    <?xml version="1.0" encoding="UTF-8"?>
    <carrental>
    </carrental>

Once created, the application will save it to a file carrental.xml. If the file already exists, its previous contents will be lost.

### 3.2 new

Command:

    java CarRental new

The application will 1) Ask the user (through the console) the data of a new rental (car model, etc.); 2) Read the carrental.xml XML document into memory; 3) Add a new "rental" element to the document with the following structure :
    
    <?xml version="1.0" encoding="UTF-8"?>
    <carrental>
        <rental id="anyID">
          <make>Toyota</make>
          <model>Celica</model>
          <start>2016-09-24-06:00</start>
          <end>2016-09-26-06:00</end>
        </rental>
    </carrental>

And 4) the application will save new document including the new rental into carrental.xml.

### 3.3 list

Command:

    java CarRental list

The application will read the carrental.xml XML document into memory and pretty print it to the console.

### 3.4 xslt

Command:

    java CarRental xslt

The application will read the carrental.xml XML document into memory, transform it into HTML with an XSLT stylesheet and print it to the console. You can reuse the stylesheet from the example (example.xslt), but you will need to change it.




