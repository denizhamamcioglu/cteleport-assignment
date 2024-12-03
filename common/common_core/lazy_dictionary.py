from collections.abc import Mapping


class LazyDictionary(Mapping):
    """
    Lazy dictionary implementation which allows to initiate dictionary values strictly when they are being requested and not during import or the initial call to the dictionary itself.
    """
    def __init__(self, *args, **kw):
        """
        Class constructor.
        Args:
            *args: Arguments.
            **kw: Keywords.
        """
        self._raw_dict = dict(*args, **kw)

    def __getitem__(self, key):
        """
        Retrieves a value associated with the given key.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The result of applying the function associated with the key to its argument.

        """
        func, arg = self._raw_dict.__getitem__(key)
        return func(arg)

    def __iter__(self):
        """
        Returns an iterator over the keys of the internal dictionary.

        Returns:
            An iterator over the keys of the internal dictionary.

        """
        return iter(self._raw_dict)

    def __len__(self):
        """
        Returns the number of key-value pairs in the internal dictionary.

        Returns:
            The number of key-value pairs in the internal dictionary.

        """
        return len(self._raw_dict)
