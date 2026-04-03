

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
