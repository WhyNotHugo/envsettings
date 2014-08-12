pyenvsettings
=============

Easily read settings from environment variables.  Used to followed the advice given by the [twelve-factor methodology](http://12factor.net/config).

Usage
-----

```
c = SettingsReader([
                   ("VARIABLE_NAME", "setting_name", bool),
                   ("ANOTHER_VARIABLE", "another_setting", str),
                   ])

if c.setting_name:
   print(c.another_setting)
```

Copyright (c) 2014 Hugo Osvaldo Barrera <hugo@barrera.io>