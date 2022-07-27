QUERIES = {
    'create_table': 'CREATE TABLE IF NOT EXISTS',
    'insert': 'INSERT OR IGNORE INTO',
    'random_dish': 'SELECT {} FROM dishes WHERE dish_type={} ORDER BY random() LIMIT 1',
}
