import os
from time import sleep
def rtty(frq, text): # RTTY
  os.system("sudo /home/pi/rpitx/pirtty " + str(frq * 1000) + " 1000 '" + text + "'")
def cw(frq, text): # CW
  os.system("sudo /home/pi/rpitx/morse " + str(frq * 1000) + " 25 '" + text + "'")
def nfm(frq, audio): # Narrow-band FM
#  os.system("(while true; do cat '" + audio + "'; done) | csdr convert_i16_f \
#  | csdr gain_ff 1000 | csdr convert_f_samplerf 20833 \
#  | sudo ../rpitx/rpitx -i- -m RF -f " + str(frq))
  os.system("sudo sox -S " + audio + " " + audio + ".sox.wav rate -L -s 48000")
  sleep(0.5)
  os.system("sudo /home/pi/rpitx-1/pifm " + audio + ".sox.wav " + audio + ".ft")
  sleep(0.5)
  os.system("sudo /home/pi/rpitx/rpitx -i " + audio + ".ft -m RF -f " + str(frq) + " -c1")
def ft8(frq, message, slot, hz="1240"): # FT8
  os.system("sudo /home/pi/rpitx/pift8 -m '" + message + "' -f " + str(frq * 1000) + " -o " + str(hz) + " -s " + str(slot))
def carrier(frq, sec): #not working now
  proc = os.system("sudo /home/pi/rpitx/tune -f " + str(frq * 1000) + " -e")
  sleep(sec)
  os.kill(proc, 9)
def fmrds(frq, audio, rds_id, rds_name, rds_text): # Wide band broadcast FM with RDS
  os.system("sudo /home/pi/rpitx/pifmrds -freq " + str(frq / 1000.0) + " -audio '" + audio + "' -pi " + str(rds_id) + " -ps '" + rds_name + "' -rt '" + rds_text + "'")
def aprs(frq, callsign, destination, digis, msg_addressee, msg, type="message", symbolcode="[", symboltable="/", lat="", long="", do_tx=True): # APRS
  # msg_addressee is used as message addressee in message type, ignored in position, object name in object
  print("Generating AFSK WAV file...")
  def aprs_9count(call):
    length = len(call)
    dodat = 9 - length
    vysledek = ""
    pocet = range(0, dodat)
    for i in pocet:
      vysledek = vysledek + " "
    return vysledek
  if (type == "message"):
    os.system("sudo aprs -c " + callsign + " --destination " + destination + " -d " + digis + " -o outaprs.wav ':" + msg_addressee + aprs_9count(msg_addressee) + ":" + msg + "'")
  if (type == "position"):
    os.system("sudo aprs -c " + callsign + " --destination " + destination + " -d " + digis + " -o outaprs.wav '=" + lat + symboltable + long + symbolcode + " " + msg + "'")
  ## NOT WORKING if (type == "object"): 
    #os.system("sudo aprs -c " + callsign + " --destination " + destination + " -d " + digis + " -o outaprs.wav ';" + msg_addressee + "*" + lat + symboltable + long + symbolcode + " " + msg + "'")
  if (type == "status"):
    os.system("sudo aprs -c " + callsign + " --destination " + destination + " -d " + digis + " -o outaprs.wav '>" + msg + "'")
  if (do_tx == True):
    nfm(frq, "outaprs.wav")
