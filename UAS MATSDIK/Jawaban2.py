# Fungsi untuk menentukan apakah alarm akan berbunyi
def alarm_status(p, j, g):
    # P = pintu, J = jendela, G = gerakan
    # Alarm berbunyi jika salah satu dari kondisi berikut terpenuhi
    alarm = p or j or g
    return alarm

# Contoh input dari sensor (0 atau 1)
P = 1  # Pintu depan terbuka
J = 0  # Jendela tertutup
G = 1  # Gerakan terdeteksi

# Memeriksa status alarm
alarm = alarm_status(P, J, G)

if alarm:
    print("Alarm berbunyi!")
else:
    print("Alarm tidak berbunyi.")
