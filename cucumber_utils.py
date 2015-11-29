import datetime

# Utils
def get_splitted_columns(row):
	colums = row.strip().split("|")
	return [c.strip() for c in colums if c.strip()]

def get_rows(table):
	return table.strip().split("\n")

def get_column(row, sort_col):
	req_columns = get_splitted_columns(row)
	return req_columns[sort_col]	

def get_date(d):
	return datetime.datetime.strptime(d, "%Y-%m-%d").date()

def converted_md_arrays(table):
	return [get_splitted_columns(row) for row in get_rows(table)]

def doorder_cmp(x,y, sort_col, secondary_col, converter1, converter2): 	
	d1 = converter1(get_column(x, sort_col))
	d2 = converter1(get_column(y, sort_col))
	val = cmp(d1, d2)
	if not val: return cmp(converter2(get_column(x, secondary_col)), converter2(get_column(y, secondary_col)))
	return val

def column_cmp(x_row,y_row, col):
	return cmp(get_column(x_row, col), get_column(y_row, col))

def cfmtdate(date):
   d = datetime.datetime.strptime(date.strip(), "%Y-%m-%d").date()
   return d.strftime("%d-%m-%Y")

def get_uniq_with_order(arr):
    seen = []
    [seen.append(x) for x in arr if x not in seen]
    return seen	

def get_columns_of_table(table, col):
	return ([row[col] for row in table])

# logical 
def sort_by_reference(table_to_sort, reference_table, sortable_col, reference_col):
	mapped_rows = {}
	for row in table_to_sort:
		mapped_rows[row[sortable_col]] = row
	return [mapped_rows[row[reference_col]] for row in reference_table]

def sorted_actual_orders(table, sort_column):
	table_rows = table.split("\n")	
	order_num_col = 0
	table_rows.sort(lambda x,y: doorder_cmp(x,y, sort_column, order_num_col, get_date, lambda x: int(x)))
	return "\n".join(table_rows)

def print_rows_reversed(table_as_md_array):
	print_as_table_with_separator(table_as_md_array[::-1])

# Display Utils
def print_as_table_with_separator(table_as_md_array, seperator="|"):
	rows_joined = [seperator + seperator.join(row) + seperator for row in table_as_md_array]
	print "\n".join(rows_joined)

def pretty_print(array, joiner="\n"):
	print joiner.join(array)