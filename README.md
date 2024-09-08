# TeXamator

This programm is distributed under the GPLv3. It was meant for Linux but can work under Mac OS (see issues for hints) and works with Windows 11/wslg.

## What is TeXamator?

TeXamator is an opensource software that was designed at helping one deal with an exercises database (hence the name (t)exam-ator).

Once configured, it will open all your .tex files in a given directory (recursively) and look for exercises (or anything you want it to). For example, you can ask it to look for the tags `\begin{exercice}` and `\end{exercice}`

Then, it will show you everything in a tree (which corresponds to the tree view of your folder) and let you expand/collapse folders. When you will click on a tex file in the tree, it will compile all the exercises it found in that particular file and show you a preview on the right. If you want, you can select one (or more) exercises from that file to add it to a list (in the middle of the window). Finally, you will be able to export all the exercises you selected to a .tex file or to a pdf.

![Screenshot 1](/md_files/cap1.png)

## A typical session

Once TeXamator is fully configured, creating an exercise sheet is very easy and using TeXamator will save you a lot of time. Here is what you will typically do.

Open TeXamator and click the "Look for exercises" button (or the corresponding button in your language if you have changed it). It will show you the exercises on your hard drive, let you preview them (when clicking on a tex file) and let you add them to the file you will export (see screenshot below). There is a "search" field that can come in handy. You can use quotes and the minus sign. For example, to search "sparse matrix" but not "equation", you could type : _"sparse matrix" -equation_

![Screenshot 1](/md_files/cap1.png)

When you're done, you can ask for a preview of the exercises you have selected using the "preview" button.

![Screenshot 2](/md_files/cap2.png)


You can use the up and down arrows to change the order of the exercises if you want, remove exercises using the "-" button or event edit exercises if you want to customize them (this will not change the source file).

If you have a (La)TeX editor opened, you can use the Ctrl+C capabilities of TeXamator (on the tree or the list, on multiple or single elements) to copy the source code of the selected exercises to your clipboard.

If you prefer, you can use the "export" button to either create a tex file containing the exercises you have selected of create a pdf. TeXamator will ask you what header to use (you can have as many custom configs as you want) and will let you edit one last time the sources before exporting.

![Screenshot export](/md_files/export.png)

## Help

### Installing

Before you can use TeXamator, you need the followings to be installed on your computer:

* latex
* python3-pyqt5
* python3-poppler-qt5


Download the latest version, extract it anywhere on your computer and open a shell. Then, cd to the directory and just do : 
```
$ python3 texamator.py
```
Or, if you prefer, you can simply double click on the file _texamator.py_. But, always prefer launching the application in a shell to see LaTeX running in the background : it will be easier to catch compilation errors and correct them.


### Getting started

The first time your run TeXamator, it will start a wizard to help you configure it. If, for some reason, you want to remove all your preferences, just find the folder `.texamator` in your home directory and delete it.

The wizard will ask you to give it a .tex file and try to guess the tags you use for your exercises. It will probably grab unuseful stuff like `\begin{cases}...\end{cases}`: remove them at the next step.

Note that you can't start an exercise with, say, `\exercise{`, and end it with `}`. Why? Because it would take too long to count the opening and closing braces. Instead, you should use `\begin{exercise}` and `\end{exercise}` for example. Or `\startexercise` and `\endexercise`.

That's it ! You're ready to go. If everything doesn't work as expected, keep reading.

### Preferences window

#### Basics

Nothing much to say about this tab. You can customize the default pdf viewer when exporting, the folder where you store your tex files and the default folder in which you will save your exercises sheets.

![Screenshot basic settings](/md_files/basics.png)

#### Tags

In this tab, you can tell TeXamator how you declare your exercises in your tex files. Add as many tags as you want.

A little world about how TeXamator works. It opens (recursively) all the tex files in a given directory. When it reads a tex file, it will start recording text as soon as it will find an opening tag ("What comes before an exercise") and stop recording as soon as it will find a closing tag ("What comes after an exercise"). That's why you cannot use things like `\exercise{this is an exercise}` with TeXamator: you will probably have curly braces inside your exercise and TeXamator won't be able to tell which curly brace corresponds to the end of the exercise (it will stop at the first `}`). I could implement it, but it would make TeXamator (too) slow.

Here is my personnal config:

![Screenshot tags settings](/md_files/tags.png)

#### Compilation

In this tab, you can set-up how LaTeX is run in the background. There are a few default settings, and you should probably use one of them. If you want to use pdflatex then I strongly suggest that you use the **Default (pdflatex)** config. If you prefer using LaTeX, you can go for the **Alternative (latex)** config.

You can customize the compilation sequence to suit your needs. TeXamator creates a folder **/tmp/partielator** and a file **file.tex** in that folder. In the compilation sequences, **!file** is a shortcut for **/tmp/partielator/file.tex** but you shouldn't worry about that as TeXamator will chdir to **/tmp/partielator** for you, so you can write simple commands like **pdflatex file.tex**.

For example, if you need to run LaTeX, then dvi2ps and then ps2pdf, you can use this sequence:

* latex file.tex
* dvi2ps file.tex
* ps2pdf file.ps

Or, if you want to ignore compilation errors, you can use

* latex -interaction=nonstopmode file.tex

You can create as many configurations as you want but cannot edit the ones shipped with the program. When exporting your work to a pdf file, you will be asked for the compilation sequence you want to use: this is the place to create a custom one for exportation (if needed). For example, when exporting a pdf, you might want to run pdflatex twice to get references right.

![Screenshot compilation](/md_files/compilation.png)

#### Preamble-postamble

TeXamator needs to know how to compile your exercises. To show you a preview of, say, an exercise sheet from the directory tree, it will create a file **/tmp/partielator/file.tex** and put the exercises in that file. But before, it will write a header that you can customize here.

You probably use a few `\newcommands` in your exercise sheets: you should write them here, otherwise you will encounter some compilation errors. If you use the exam class, maybe you will want to add `\begin{questions}` just after `\begin{document}`. Here is an example of a very basic configuration:


In this tab, you can also customize what TeXamator will append after your exercises before compiling the file **/tmp/partielator/file.tex**. You don't have to write anything here if you don't need to. But, if you use the exam class, you might want to add `\end{questions}` here. Here is my personnal config.

Note that you can add as many configurations as needed: they will come in handy when exporting files. I personnaly have one to export to a beamer document which is very useful when I am with my students and need to give them something to work on.

### Tips

Here are a few tips to use TeXamator:

* Don't search for exercises in "~/" because TeXamator also looks into hidden folders.
* The search functionality is not case sensitive. It works a la firefox.
* The search field will automatically transform accents in TeX format for you. Thus, if you enter _théorie_ it will look for _théorie_ and _th\'eorie_.
* Right clicking on an element of the tree will expand the tree under this element.
* Layout is customizable by clicking on the two vertical grips.
* A double click on an exercise in the list of exercises will let you edit it.
* Ctrl+C on one (or more) exercise will copy its source code to the clipboard.
* You can select multiple elements (even entire folders) on the tree and add them with the "+" button.


## TeXamator and AMC

### Introduction

#### What is AMC?

AMC is a great software that helps you build multiple choices questionnaires with LaTeX. More information is available online here : http://home.gna.org/auto-qcm/

If you want to work with AMC, you should go to the parameters window and enable AMC. Plus, you should probably keep on reading these pages !

Here is a preview of what you can achieve:

![Screenshot AMC](/md_files/capAMC.png)


#### Two possibilities

TeXamator is not able to look for tags that end with `}`: it would take a (very) long time to count opening and closing braces when searching for exercises and make the program (very) slow. You have to choose between two options. You can either ask TeXamator to look for these tags:
```latex
\begin{question} ... \end{question}
\begin{questionmult} ... \end{questionmult}
```
But that would mean losing the elements names. Or, you can stop using
```latex
\element{foo}{
            bar
        }
```
and use instead
```latex
\begin{qcm}{foo}
    bar
\end{qcm}
```
In order to do so, you need to create a new environment (qcm) to replace the usual `\element` macro. One way to do it is to put these macros in your preamble:
```latex
\NewEnviron{qcm}[1]{%
  \def\arg{#1}%
  \expandafter\element\expandafter\arg\expandafter{\BODY}}

\makeatletter
\renewcommand{\element}[2]{%
  \AMC@prepare@element{#1}%
  \global\csname #1@\romannumeral\AMCtok@k\endcsname={#2}%
}
\makeatother
```

#### A script

Going through all your existing tex files to change them would take forever. Good news, I wrote a script to modify all your tex files (actually to create new ones) so that `\element{foo}{bar}` will become `\begin{qcm}{foo}bar\end{qcm}`. You can find it here: https://github.com/alexisflesch/AMC-element

## Credits

* Most of the icons used are from the crystal diamond icon 2.85 theme :
http://www.kde-look.org/content/show.php/Crystal+Diamond+Icons?content=45576
which is released under LGPL (version not specified to my knowledge)

* Pavel Fric is responsible for the czech translation :
http://fripohled.blogspot.com/
* German translation supported by Martin Zinser (zinser@zinser.no-ip.info)
* Bernard Remond (NBRemond@laposte.net) is reponsible for the new feature "footer" !
* Greek translation supported by Emmanuil Tsioptsias (https://emtsiopt.sites.sch.gr/)
* I am responsible for all the bugs. Open an issue if you find one !
