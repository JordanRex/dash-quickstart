import pandas as pd

from itertools import product

###########################################################################################################################
## HELPER FUNCS ##
###########################################################################################################################


def expandgrid(*itrs):
    prod = list(product(*itrs))
    return {"Var{}".format(i + 1): [x[i] for x in prod] for i in range(len(itrs))}


def __my_flatten_cols(self, how="_".join, reset_index=True):
    how = (lambda iter: list(iter)[-1]) if how == "last" else how
    self.columns = (
        [how(filter(None, map(str, levels))) for levels in self.columns.values]
        if isinstance(self.columns, pd.MultiIndex)
        else self.columns
    )
    return self.reset_index() if reset_index else self


pd.DataFrame.my_flatten_cols = __my_flatten_cols
