#Just a simple bash file to turn all my ui files into python files
#using pyuic4. Will also erase all .pyc files.

pyrcc4 icones.qrc -o ../partielatormods/guis/icones_rc.py
pyuic4 -o ../partielatormods/guis/guiabout.py -x apropos.ui
pyuic4 -o ../partielatormods/guis/guiprefs.py -x preferences.ui
pyuic4 -o ../partielatormods/guis/guiquit.py -x quitter.ui
pyuic4 -o ../partielatormods/guis/guigui.py -x guigui.ui
pyuic4 -o ../partielatormods/guis/guirandomize.py -x randomize.ui
pyuic4 -o ../partielatormods/guis/guiedit.py -x edit.ui
pyuic4 -o ../partielatormods/guis/guinewconf.py -x newconf.ui
pyuic4 -o ../partielatormods/guis/guiexport.py -x export.ui
pyuic4 -o ../partielatormods/guis/guiwizard.py -x wizard.ui
pyuic4 -o ../partielatormods/guis/guidelete.py -x delete.ui
pyuic4 -o ../partielatormods/guis/guishuffle.py -x shufflelist.ui
pyuic4 -o ../partielatormods/guis/guiwarning.py -x warning.ui
pyuic4 -o ../partielatormods/guis/guilangchange.py -x langchange.ui
pyuic4 -o ../partielatormods/guis/guieditsource.py -x editsource.ui
pyuic4 -o ../partielatormods/guis/guidepthwarning.py -x depthWarning.ui
pyuic4 -o ../partielatormods/guis/guiexportamc.py -x exportAMC.ui

pylupdate4 ../ts_files/TeXamator.pro

find ../ -type f -name "*.pyc" -exec rm -f {} \;
find ../ -type f -name "*.py~" -exec rm -f {} \;
