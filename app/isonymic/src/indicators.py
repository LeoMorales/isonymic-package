import pandas


def get_isonymy(surnames_i: pandas.Series) -> float:
    """Retorna las isonímia interna de una población segun sus apellidos.

    Args:
        surnames_i (pandas.Series): Apellidos de c/u de los miembros de una población

    Returns:
        float: Valor de la isonimia.
    """
    if not isinstance(surnames_i, pandas.Series):
        raise TypeError(
            f"Argument must be a pandas Series. Type found: {type(surnames_i)}"
        )

    # get surname | count dataframe
    surnames_i.name = "surname"

    df_surnames_i = (
        surnames_i.value_counts()
        .reset_index()
        .rename(columns=dict(index="surname", surname="counts"))
    )

    df_surnames_i["relative_frequency"] = df_surnames_i["counts"] / len(surnames_i)
    df_surnames_i["relative_frequency_squared"] = (
        df_surnames_i["relative_frequency"] ** 2
    )

    isonymy_value = df_surnames_i["relative_frequency_squared"].sum()

    return isonymy_value
