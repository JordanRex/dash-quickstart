###############################################################################################################
"""
Dictionaries can be of 2 types
1. Where the options and values are same (in data)
2. Where the options and values are different (from data)

How to
1. Create list and then call opts function with method = "alike" to generate options dict
2. Create opts and vals lists, then call opts function with method = "unlike" to generate options dict
"""

from dbconfig.sqlite3_script import pd_from_sql

###############################################################################################################


def opts_fn(lst1, lst2=None, method="alike"):
    if method == "alike":
        if isinstance(lst1, list):
            if len(lst1) > 0:
                return [{"label": x, "value": x} for x in lst1]
    else:
        if (isinstance(lst1, list)) & (isinstance(lst2, list)):
            if (len(lst1) > 0) & (len(lst2) > 0) & (len(lst1) == len(lst2)):
                return [{"label": x, "value": y} for x, y in zip(lst1, lst2)]
    return None  # all other cases


######################################################

opts_zones_lst = list(
    (pd_from_sql("select Zone from site_zone_mapping"))["Zone"].unique()
)
opts_zone = opts_fn(opts_zones_lst)
