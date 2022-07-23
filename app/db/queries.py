QUERIES = {
    'create table': 'CREATE TABLE IF NOT EXISTS',
    'insert': 'INSERT OR IGNORE INTO',
    'random dish': 'SELECT {} FROM dishes WHERE dish_type={} ORDER BY random() LIMIT {}',
}
