import os


class SettingsReader():

    def __init__(self, variables):
        """
        variables is a tuple of var_name, setting_name, type.
        var_name is the name of the environment variable.
        setting_name is the name for the setting in the returned dict
        type can be int, str, bool
        """

        for var_name, setting_name, type in variables:
            if not var_name in os.environ:
                raise Exception("Environment variable {} not set."
                                .format(var_name))

            var = os.environ[var_name]

            if type == str:
                setattr(self, setting_name, var)
            elif type == int:
                setattr(self, setting_name, int(var))
            elif type == bool:
                setattr(self, setting_name, var.lower()
                        in ["true", "yes", "on"])


if __name__ == "__main__":
    """
    Tests this script. Run test.sh to set the proper variables instead of
    running this manually.
    """

    c = SettingsReader([
                       ("A", "a", bool),
                       ("B", "b", bool),
                       ("C", "c", int),
                       ("D", "d", str),
                       ("E", "e", str),
                       ("F", "f", str),
                       ])

    assert(c.a is True)
    assert(c.b is False)
    assert(c.c == 17)
    assert(c.d == "18")
    assert(c.e == "yes")
    assert(c.f == "Some longer text")
