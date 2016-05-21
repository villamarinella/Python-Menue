#!/bin/bash
## Menue 

if [ -z "$1" ]
  then
    echo "Kein Parameter, daher Abbruch"
    exit 1
fi

if [ $1 = "A" ]
    then
          echo "Licht 1 an"
## codesend 123456          
elif [ $1 = "B"  ]
      then
           echo "Licht 1 aus"
## codesend 123456          
elif [ $1 = "C"  ]
      then
      echo "Licht 2 an"     
## codesend 123456          
elif [ $1 = "D"  ]
      then
      echo "Licht 2 aus"    
## codesend 123456          
elif [ $1 = "E"  ]
      then
      echo "Navit starten"     
## cd /navit
## navit
elif [ $1 = "F"  ]
      then
      echo "Starten Foto"     
      python foto.py
elif [ $1 = "R"  ]
      then
      python calculator.py     
elif [ $1 = "V"  ]
      then
      echo "Starten Video"     
      python video.py
elif [ $1 = "N"  ]
      then
      echo "Starten File / editor"    
      python file.py
else

echo "Unbekannter Parameter"
fi
exit 0

