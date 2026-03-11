import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    matches_df = pd.merge(anon_df, aux_df, on=['age', 'zip3', 'gender'])
    matches_df = matches_df[['anon_id', 'name']].rename(columns={'name': 'matched_name'})

    return matches_df


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    deanon_rate =  (matches_df['anon_id'].value_counts() == 1).sum() / len(anon_df)

    return deanon_rate
