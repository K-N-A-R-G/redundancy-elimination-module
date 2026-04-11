

# --- SYNC DATA BLOCK: COLLECTIONS ---
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def casefold(self):
        return self.__class__(self.data.casefold())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=_sys.maxsize):
        if isinstance(sub, UserString):
            sub = sub.data

# --- END OF NODE UPDATE ---


# --- SYNC DATA BLOCK: LOGGING ---
        children, will have its events allowed through the filter. If no
        name is specified, allow every event.
        """
        self.name = name
        self.nlen = len(name)

# --- END OF NODE UPDATE ---


# --- SYNC DATA BLOCK: INSPECT ---
    def __init__(self, name, kind, *, default=_empty, annotation=_empty):
        try:
            self._kind = _ParameterKind(kind)
        except ValueError:
            raise ValueError(f'value {kind!r} is not a valid Parameter.kind')
        if default is not _empty:
            if self._kind in (_VAR_POSITIONAL, _VAR_KEYWORD):
                msg = '{} parameters cannot have default values'
                msg = msg.format(self._kind.description)
                raise ValueError(msg)

# --- END OF NODE UPDATE ---
