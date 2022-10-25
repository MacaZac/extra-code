import csv

#make the query
def count_records(schema, table_name):
    cur = conn.cursor()
    cur.execute("""
        select count(*)
        from """ + schema + '.' + table_name + """
        where partition_date = '2022-10-18'
        """)
    rows = cur.fetchall()
    return rows[0][0]
 
#control_range
with open("table_min_max_values.csv") as file:
    table_list = csv.reader(file)
    header = next(table_list)
    for schema,table_name,min_records,max_records in table_list:
        print('\n', schema, table_name)
        record_count= count_records(schema, table_name)
        if record_count >= int(min_records) * 0.90 and record_count <= int(max_records) * 1.50:
            print('parameters', min_records,max_records, 'record_count:', record_count, 'OK')
        else:
            print('parameters', min_records,max_records, 'record_count:', record_count, 'Not OK, check your table')
        
