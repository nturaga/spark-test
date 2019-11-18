import hail as hl

hl.utils.get_movie_lens('data/')

users = hl.read_table('data/users.ht')
