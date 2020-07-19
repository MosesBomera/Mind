import os

class Util:
    def get_variable(env_variable, default=None):
        """
            Tries to get the specified environment variable,
            returns the variable or a RuntimeError.
        """
        if not os.getenv(env_variable, default):
            raise RuntimeError
        return os.getenv(env_variable, default)
