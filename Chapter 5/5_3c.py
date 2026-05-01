# Use [] to obtain the value assoicated with a key.
info = {"name":"Sandy", "occupation":"manager"}
print(info["name"])

# If key is not present in dictionary, an error is raised
# print(info["job"])

# An easier strategy is to use the method get.
# If the key is absent, the default value passed to get is returned
print(info.get("job", None))