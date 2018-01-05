# usb-wifi-connect

Bilgisayara bağlanan USB belleğin içerisindeki Wi-Fi yapılandırma dosyasını okuyup bilgisayarın Wi-Fi ağına bağlanmasını sağlayan bir script.

_A script which reads Wi-Fi configuration file from USB drives and connects to Wi-Fi networks using this information._

## Bağımlılıklar/Dependencies

* urllib
* subprocess

## Kullanım/Usage

```
./usb-wifi-connect start|stop|restart
```

## Yapılandırma dosyası hazırlama/Creating configuration file

* USB bellekte "wifi.txt" isimli bir dosya oluşturun. Dosya formatı şu şekilde olmalıdır:

```
ssid
parola
```

* _Create a file on USB drive named "wifi.txt" . The file must be like this:

```
ssid
password
```

## Lisanslar/Licenses

Bu yazılım GNU GPL v3+ ile lisanslanmıştır. 

```daemon.py``` modülü CC BY-SA ile lisanslanmıştır.

_This software is licensed under GNU GPL v3 or any later version._

_```daemon.py``` module is licensed under CC BY-SA._
