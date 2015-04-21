envsettings
===========

Easily read settings from environment variables.  Reading settings from
environment variables allows complete isolation between application and
configuration data.

Read the Twelve-Factor App's relevant [section](http://12factor.net/config)
for more rationale behind this approach.

Usage
-----

The following example will read the environment variables into configuration
values host, port, and debug, cast to the expected type:

```
from envsettings import SettingsReader

r = SettingsReader([
    ("HOST", "host", str),
    ("PORT", "port", int),
    ("DEBUG", "debug", bool),
])

if r.debug:
   print("Running in debug mode")

myapp.run(r.host, r.port, debug=r.debug)
```

Boolean values can be either "true", "yes", or "on" and are treated in a
insensitive manner.

Contributing
------------

Any feedback is welcome, and please report any bugs you encounter on the
project's [issue tracker](https://git.barrera.io/hobarrera/envsettings/issues).

Patches or merge requests are welcome.

Licence
-------

envsettings is licensed under the ISC licence (functionally equivalent to the
MIT licence). See LICENCE.md for details.

Copyright (c) 2014 Hugo Osvaldo Barrera <hugo@barrera.io>
