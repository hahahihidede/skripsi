import subprocess


subprocess.call(['curl', '-X', 'POST', "https://api.thebigbox.id/sms-notification/1.0.0/messages", '-H', 
"accept: application/x-www-form-urlencoded", '-H', "x-api-key: 2y2XT6ELcv16nD92H4mTpktqdF2sEChk", '-H',
 "Content-Type: application/x-www-form-urlencoded", '-d', "msisdn="+ pelanggaranBaru + '&content=' + kirim])