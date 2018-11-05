import sys

from src import Analytics as processing_engine, DataTransformer as transformer
from src.DataFrameH1B import DF


def run(input_file, occupation_stat_file, state_stat_file):
    raw_data = DF.read_csv(input_file)
    data = transformer.standardize_col_names(raw_data)
    occupation_stats = processing_engine.get_occupation_stats(data)
    state_stats = processing_engine.get_state_stats(data)
    occupation_stats.to_csvfile(occupation_stat_file)
    state_stats.to_csvfile(state_stat_file)
run(sys.argv[1], sys.argv[2], sys.argv[3])