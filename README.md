# TeXamator (v.3.0.alpha)

This programm is distributed under the GPLv3. If you need help using it, please visit :
http://alexisfles.ch/en/texamator/texamator.html
or contact me by email :
alexis.flesch@gmail.com


---------------------------- WARNING --------------------------------------------

This is an alpha version. It has not been tested enough to ensure that it will work flawlessly.

That being said, it can be installed alongside the develop version (2.4.2) : they don't save preferences in the same directories.

Please note that you now NEED to produce a pdf in order for TeXamator to preview your exercises (dvi and png are not supported anymore).


---------------------------- Instructions --------------------------------------------

You need the following to run this programm :
- latex
- python3-pyqt5
- python3-poppler-qt5

To launch the program you can double-click on the file "texamator.py" or open a shell,
hop to the directory and type "python texamator.py". This last method is preferred
because it will let you see LaTeX running in the background and catch errors.

------------------------------- Credits -----------------------------------------------

* Most of the icons used are from the crystal diamond icon 2.85 theme :
http://www.kde-look.org/content/show.php/Crystal+Diamond+Icons?content=45576
which is released under LGPL (version not specified to my knowledge)

* Pavel Fric is responsible for the czech translation :
http://fripohled.blogspot.com/

* German translation supported by Martin Zinser (zinser@zinser.no-ip.info)

* Bernard Remond (NBRemond@laposte.net) is reponsible for the new feature "footer" !

* I am responsible for all the bugs... Send me an email if you find one !!

------------------------------ Special features --------------------------------------

* Right clicking on the tree will expand/collapse everything under the element

* Ctrl+C on an exercise (or more) in the tree or in the list will copy the source code
to the clip board

* A double click on an exercise in the list of exercises will let you edit it.
