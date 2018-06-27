#Just a simple bash file to turn all my ui files into python files
#using pyuic5. Will also erase all .pyc files.

pyrcc5 icones.qrc -o ../partielatormods/guis/icones_rc.py
pyuic5 --from-imports -o ../partielatormods/guis/guiabout.py -x apropos.ui
pyuic5 --from-imports -o ../partielatormods/guis/guiprefs.py -x preferences.ui
pyuic5 --from-imports -o ../partielatormods/guis/guiquit.py -x quitter.ui
pyuic5 --from-imports -o ../partielatormods/guis/guigui.py -x guigui.ui
pyuic5 --from-imports -o ../partielatormods/guis/guirandomize.py -x randomize.ui
pyuic5 --from-imports -o ../partielatormods/guis/guiedit.py -x edit.ui
pyuic5 --from-imports -o ../partielatormods/guis/guinewconf.py -x newconf.ui
pyuic5 --from-imports -o ../partielatormods/guis/guiexport.py -x export.ui
pyuic5 --from-imports -o ../partielatormods/guis/guiwizard.py -x wizard.ui
pyuic5 --from-imports -o ../partielatormods/guis/guidelete.py -x delete.ui
pyuic5 --from-imports -o ../partielatormods/guis/guishuffle.py -x shufflelist.ui
pyuic5 --from-imports -o ../partielatormods/guis/guiwarning.py -x warning.ui
pyuic5 --from-imports -o ../partielatormods/guis/guilangchange.py -x langchange.ui
pyuic5 --from-imports -o ../partielatormods/guis/guieditsource.py -x editsource.ui
pyuic5 --from-imports -o ../partielatormods/guis/guidepthwarning.py -x depthWarning.ui
pyuic5 --from-imports -o ../partielatormods/guis/guiwarningNewVersion.py -x warningNewVersion.ui
pyuic5 --from-imports -o ../partielatormods/guis/guiexportamc.py -x exportAMC.ui

pylupdate5 ../ts_files/TeXamator.pro

pyclean () {
        find .. -type f -name "*.py[co]" -delete
        find .. -type d -name "__pycache__" -delete
}

pyclean
