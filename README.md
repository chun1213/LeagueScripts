# LeagueScripts
League OCR using opencv and tesseract
It continously screenshots the area of the screen that holds the healthbar of the dragon when activated and passes the data in the form of a matrix into the tesseract API which then sends back the text to be 
compared to the current smite damage level. If the health is less than the smite damage, then the "smite" command is auto outputed to the user's keyboard.  
